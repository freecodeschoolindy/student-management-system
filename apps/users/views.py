from rest_framework import serializers, viewsets
from django.contrib.auth import get_user_model

from apps.submissions.models import StudentSubmission
from apps.projects.models import Project


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


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = StudentSubmission.objects.all()
    serializer_class = AssignmentSerializer
