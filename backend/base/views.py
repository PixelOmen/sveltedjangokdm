import os
from pathlib import Path

from django.conf import settings
from django.utils import timezone
from django.core.files import File
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

from . import serializers, models, services


class SvelteAppView(TemplateView):
    template_name = 'index.html'



class ServePublicLeafFile(APIView):
    def get(self, request):
        file_path = os.path.join(settings.MEDIA_ROOT + '/public/public_leaf.pem')
        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='public_leaf.pem')
        else:
            return Http404('File not found!')

class ServeSampleFiles(APIView):    
    def get(self, request):
        file_path = os.path.join(settings.MEDIA_ROOT + '/public/Sample_Files.zip')
        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='Sample_Files.zip')
        else:
            return Http404('File not found!')
        
class ServeKDMFile(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    
    def get(self, request, job_id):
        job = get_object_or_404(models.Job, id=job_id)
        if job.user != request.user:
            return Response({'detail': 'Forbidden!'}, status=status.HTTP_403_FORBIDDEN)
        if not job.kdm or not job.kdm.display_name or not os.path.exists(job.kdm.file.path):
            return Response({'detail': 'KDM not found!'}, status=status.HTTP_404_NOT_FOUND)
        return FileResponse(open(job.kdm.file.path, 'rb'), as_attachment=True, filename=job.kdm.display_name)




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
        print(type(request.data['file']), flush=True)
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
    

class SubmitJob(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def _set_job_error(self, job: models.Job, status: str, error: str):
        job.status = status
        job.error = error
        job.completed_at = timezone.now()
        job.save()

    def post(self, request):
        request.data['outputDir'] = str(Path(settings.MEDIA_ROOT) / 'output' / str(request.user.id))
        serializer = serializers.JobSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {'detail': serializers.format_errors(serializer)},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        jobinstance: models.Job = serializer.save() #type: ignore
        data = dict(serializer.data)
        data['cert'] = get_object_or_404(models.Cert, id=data['cert']).file.path
        data['dkdm'] = get_object_or_404(models.DKDM, id=data['dkdm']).file.path
        jobid = jobinstance.id

        try:
            kdmresponse = services.dcpomatic.process_request(data, str(jobid))
        except Exception as e:
            self._set_job_error(jobinstance, 'error', str(e))
            return Response(
                {'detail': f'Job failed: {e}'},
                 status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        services.filecleanup.delete_after_delay(kdmresponse.kdm_path, 30)
        if kdmresponse.status == 'ok':
            data = {
                'file': File(open(kdmresponse.kdm_path, 'rb'), name=kdmresponse.kdm_name),
                'display_name': kdmresponse.kdm_name,
                'user': request.user.id
            }
            kdmserializer = serializers.KDMSerializer(data=data)
            if not kdmserializer.is_valid():
                self._set_job_error(jobinstance, 'error', serializers.format_errors(kdmserializer))
                return Response(
                    {'detail': f'Job failed: {serializers.format_errors(kdmserializer)}'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            kdm: models.KDM = kdmserializer.save() #type: ignore
            jobinstance.status = 'completed'
            jobinstance.completed_at = timezone.now()
            jobinstance.kdm = kdm
            jobinstance.save()
            kdm_url = f'/api/kdm/{jobid}'
            display_name = kdm.display_name + '.xml' if kdm.display_name else None
            return Response(
                {
                    'detail': 'Job completed successfully!',
                    'kdm_url': kdm_url,
                    'display_name': display_name
                },
                status=status.HTTP_201_CREATED
            )
        else:

            jobinstance.status = 'error'
            jobinstance.error = kdmresponse.error
            jobinstance.completed_at = timezone.now()
            jobinstance.save()
            return Response({'detail': f'Job failed: {kdmresponse.error}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)