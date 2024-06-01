from django.http import HttpResponse
from django.middleware.csrf import get_token
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.decorators import api_view



class SvelteAppView(TemplateView):
    template_name = 'index.html'

@csrf_exempt
def get_csrf_token(request):
    get_token(request)
    return HttpResponse("CSRF cookie set")



@api_view(['GET'])
def test_token(request):
    return Response({'message': 'Login successful!'})

# add decorator not requiring csrf token
@api_view(['POST'])
def login(request):
    return Response({'message': 'Login successful!'})

@api_view(['POST'])
def signup(request):
    return Response({'message': 'Login successful!'})
