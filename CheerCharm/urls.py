"""CheerCharm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url

from accounts.views import *
from cheers.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url('rest-auth/', include('rest_auth.urls')),
    url('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('django.contrib.auth.urls')),

    #파일 다운로드
    path('cheers/download/<int:image_id>/',
         FileDownloadView.as_view(), name="download"),

    # 소셜 로그인
    # path('accounts/kakao/login/', kakaoSignInView.as_view(), name='kakao_login'),
    # path('accounts/kakao/login/callback/', kakaoSignInCallBackView.as_view(), name='kakao_callback'),
    # path('accounts/profile/', KakaoSignInCallbackView.as_view(), name='kakao_login_callback'),
    # path('accounts/kakao/login/todjango', KakaoToDjangoLogin.as_view(), name='kakao_todjango_login'),


]
