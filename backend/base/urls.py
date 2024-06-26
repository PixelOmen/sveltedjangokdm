from django.urls import path
from django.urls import re_path
from django.conf import settings
from django.views.static import serve

from . import views

urlpatterns = [
    path('api/public_leaf', views.ServePublicLeafFile.as_view(), name='public_leaf'),
    path('api/sample_files', views.ServeSampleFiles.as_view(), name='sample_files'),
    
    path('api/login', views.LoginToken.as_view(), name='login'),
    path('api/logout', views.LogoutToken.as_view(), name='logout'),
    path('api/signup', views.SignUpView.as_view(), name='signup'),
    path('api/test_token', views.TestToken.as_view(), name='test_token'),

    path('api/add_user_cert', views.CreateCert.as_view(), name='add_user_cert'),
    path('api/add_user_dkdm', views.CreateDKDM.as_view(), name='add_user_dkdm'),

    path('api/get_user_certs', views.CertList.as_view(), name='get_user_certs'),
    path('api/get_user_dkdms', views.DKDMList.as_view(), name='get_user_dkdms'),

    path('api/certs/<int:pk>', views.CertDetail.as_view(), name='cert_detail'),
    path('api/dkdms/<int:pk>', views.DKDMDetail.as_view(), name='dkdm_detail'),
    path('api/kdm/<str:job_id>', views.ServeKDMFile.as_view(), name='kdm_file'),

    path('api/submit_job', views.SubmitJob.as_view(), name='submit_job'),

    path('', views.SvelteAppView.as_view(), name='svelte_app'),
    path('kdm', views.SvelteAppView.as_view(), name='svelte_app'),
    path('about', views.SvelteAppView.as_view(), name='svelte_app'),
    path('login', views.SvelteAppView.as_view(), name='svelte_app'),
    path('signup', views.SvelteAppView.as_view(), name='svelte_app'),
    path('logout', views.SvelteAppView.as_view(), name='svelte_app'),
    re_path(r'^(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]