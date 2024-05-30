from django.urls import path
from django.urls import re_path
from django.conf import settings
from django.views.static import serve

from .views import test_response, SvelteAppView

urlpatterns = [
    path('test/', test_response),
    path('', SvelteAppView.as_view(), name='svelte_app'),
    path('kdm/', SvelteAppView.as_view(), name='svelte_app'),
    re_path(r'^(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]