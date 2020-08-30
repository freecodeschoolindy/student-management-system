from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from .models import Certificate


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')


@permission_classes([IsAuthenticated])
class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
