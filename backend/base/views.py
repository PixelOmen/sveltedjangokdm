import os

from django.conf import settings
from django.contrib.auth.models import User
from django.http import FileResponse, Http404
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from . import serializers, models


class SvelteAppView(TemplateView):
    template_name = 'index.html'


class ServePublicLeafView(APIView):
    def get(self, request):
        file_path = os.path.join(settings.MEDIA_ROOT + '/public/public_leaf.pem')
        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='public_leaf.pem')
        else:
            return Http404('File not found!')

class TestToken(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def get(self, request):
        return Response({'detail': f"Passed token test! {request.user.email}"})



class AddCert(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def post(self, request):
        file_name = request.data['file'].name
        exists = models.Cert.objects.filter(user=request.user.id, display_name=file_name).exists()
        if exists:
            return Response(
                {'detail': 'Cert already exists!'},
                  status=status.HTTP_400_BAD_REQUEST
            )
        request.data['user'] = request.user.id
        serializer = serializers.CertSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Cert uploaded successfully!'}, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {'detail': serializers.format_errors(serializer)},
                status=status.HTTP_400_BAD_REQUEST
            )

class AddDKDM(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def post(self, request):
        file_name = request.data['file'].name
        exists = models.DKDM.objects.filter(user=request.user.id, display_name=file_name).exists()
        if exists:
            return Response(
                {'detail': 'DKDM already exists!'},
                 status=status.HTTP_400_BAD_REQUEST
            )
        request.data['user'] = request.user.id
        serializer = serializers.DKDMSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'DKDM uploaded successfully!'}, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {'detail': serializers.format_errors(serializer)},
                 status=status.HTTP_400_BAD_REQUEST
            )



class CertList(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def get(self, request):
        certs = models.Cert.objects.filter(user=request.user.id)
        serializer = serializers.CertSerializer(certs, many=True)
        return Response(serializer.data)
    
class DKDMList(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def get(self, request):
        dkdms = models.DKDM.objects.filter(user=request.user.id)
        serializer = serializers.DKDMSerializer(dkdms, many=True)
        return Response(serializer.data)



class CertDetail(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def get(self, request, pk):
        cert = get_object_or_404(models.Cert, id=pk)
        serializer = serializers.CertSerializer(cert)
        return Response(serializer.data)

    def delete(self, request, pk):
        cert = get_object_or_404(models.Cert, id=pk)
        cert.delete()
        return Response({'detail': 'Cert deleted successfully!'}, status=status.HTTP_200_OK)
    
class DKDMDetail(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def get(self, request, pk):
        dkdm = get_object_or_404(models.DKDM, id=pk)
        serializer = serializers.DKDMSerializer(dkdm)
        return Response(serializer.data)

    def delete(self, request, pk):
        dkdm = get_object_or_404(models.DKDM, id=pk)
        dkdm.delete()
        return Response({'detail': 'DKDM deleted successfully!'}, status=status.HTTP_200_OK)




class LoginToken(APIView):
    def post(self, request):
        user = get_object_or_404(User, username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response(
                {'detail': 'Invalid username/password'},
                status=status.HTTP_400_BAD_REQUEST
            )
        token = Token.objects.get_or_create(user=user)
        serializer = serializers.UserSerializer(instance=user)
        return Response({'token': token[0].key, 'user': serializer.data})
    
class LogoutToken(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def post(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, Token.DoesNotExist):
            pass
        return Response({'detail': 'Logout successful!'}, status=status.HTTP_200_OK)



class SignUpView(APIView):
    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return Response(
                {'token': token.key, 'user': serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {'detail': serializers.format_errors(serializer)},
                status=status.HTTP_400_BAD_REQUEST
        )