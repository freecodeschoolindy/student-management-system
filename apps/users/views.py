from rest_framework import serializers, viewsets
from django.contrib.auth import get_user_model

from apps.submissions.models import StudentSubmission


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
    class Meta:
        model = StudentSubmission
        fields = ('id', 'project_id', 'url', 'feedback', 'approved')


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = StudentSubmission.objects.all()
    serializer_class = AssignmentSerializer
