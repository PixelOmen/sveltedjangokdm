from django.urls import path
from django.urls import re_path
from django.conf import settings
from django.views.static import serve

from . import views

urlpatterns = [
    path('api/test_post', views.test_post, name='test_post'),    
    path('api/login', views.login, name='login'),
    path('api/logout', views.logout, name='logout'),
    path('api/signup', views.signup, name='signup'),
    path('api/test_token', views.is_auth, name='test_token'),

    path('', views.SvelteAppView.as_view(), name='svelte_app'),
    path('kdm', views.SvelteAppView.as_view(), name='svelte_app'),
    path('login', views.SvelteAppView.as_view(), name='svelte_app'),
    path('signup', views.SvelteAppView.as_view(), name='svelte_app'),
    path('logout', views.SvelteAppView.as_view(), name='svelte_app'),
    re_path(r'^(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]