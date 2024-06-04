from django.urls import path
from django.urls import re_path
from django.conf import settings
from django.views.static import serve

from . import views

urlpatterns = [
    path('api/test_post', views.TestPostView.as_view(), name='test_post'),
    path('api/public_leaf', views.ServePublicLeafView.as_view(), name='public_leaf'),    
    path('api/login', views.LoginView.as_view(), name='login'),
    path('api/logout', views.Logoutview.as_view(), name='logout'),
    path('api/signup', views.SignUpView.as_view(), name='signup'),
    path('api/test_token', views.IsAuthView.as_view(), name='test_token'),

    path('', views.SvelteAppView.as_view(), name='svelte_app'),
    path('kdm', views.SvelteAppView.as_view(), name='svelte_app'),
    path('login', views.SvelteAppView.as_view(), name='svelte_app'),
    path('signup', views.SvelteAppView.as_view(), name='svelte_app'),
    path('logout', views.SvelteAppView.as_view(), name='svelte_app'),
    re_path(r'^(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]