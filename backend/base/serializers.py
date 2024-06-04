from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Cert

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')

class KDMCertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cert
        fields = ('__all__')