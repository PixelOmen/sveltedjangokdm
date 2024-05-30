from django.urls import path

from .views import test_response, csrf_token

urlpatterns = [
    path('test/', test_response),
    path('csrf-token/', csrf_token),
]