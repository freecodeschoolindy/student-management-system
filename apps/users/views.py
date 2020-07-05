from django.contrib.auth import get_user_model
from rest_framework import serializers, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from apps.submissions.models import StudentSubmission
from apps.projects.models import Project
from .permissions import ObjectPermission


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'is_student')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        is_student = validated_data.pop('is_student')
        user = get_user_model().objects.create_user(**validated_data)
        user.is_student = is_student
        user.save()
        return user


class AssignmentSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(
                queryset=Project.objects.all())
    student = serializers.PrimaryKeyRelatedField(
                queryset=get_user_model().objects.all())

    class Meta:
        model = StudentSubmission
        fields = ('id', 'project', 'student',
                  'url', 'feedback', 'approved')
        read_only_fields = ['feedback', 'approved']


@permission_classes([IsAuthenticated])
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


@permission_classes([IsAuthenticated])
class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = StudentSubmission.objects.all()
    serializer_class = AssignmentSerializer


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
