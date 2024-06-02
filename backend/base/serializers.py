from rest_framework import serializers
from django.contrib.auth.models import User

from .models import KDMCert

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')

class KDMCertSerializer(serializers.ModelSerializer):
    class Meta:
        model = KDMCert
        fields = ('__all__')