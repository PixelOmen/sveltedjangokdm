from rest_framework import serializers
from django.contrib.auth.models import User

from . import models

def format_errors(serializer) -> str:
    error_str = ''
    for error_type in serializer.errors:
        err_partial = f"{error_type}: "
        for error in serializer.errors[error_type]:
            err_partial += error + '\n'
        error_str += err_partial
    return error_str

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')

class CertSerializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = models.Cert
        fields = '__all__'

class DKDMSerializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = models.DKDM
        fields = '__all__'

class KDMSerializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = models.KDM
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Job
        fields = '__all__'