from django.http import JsonResponse
from django.views import View
from rest_auth.registration.views import SocialLoginView                   
from allauth.socialaccount.providers.kakao import views as kakao_views     
from allauth.socialaccount.providers.oauth2.client import OAuth2Client     
import requests                       
from django.shortcuts import redirect 
from .models import User 

# class kakaoSignInView(View):
#     def get(self, request):
#         app_key='0ca829c4de0a85a9f97a2b5735c7d4ae'
#         redirect_uri='http://127.0.0.1:8000/accounts/kakao/login/callback/'
#         kakao_auth_api='http://kauth.kakao.com/oauth/authorize?response_type=code'
#         return redirect(
#             f'{kakao_auth_api}&client_id={app_key}&redirect_uri={redirect_uri}'
#         )

# class kakaoSignInCallBackView(View):
#     def get(self, request):
#         auth_code=request.GET.get('code')
#         kakao_token_api='https://kauth.kakao.com/oauth/token'
#         data={
#             'grant_type':'authorization_code',
#             'client_id':'0ca829c4de0a85a9f97a2b5735c7d4ae',
#             'redirection_uri':'http://127.0.0.1:8000/accounts/kakao/login/callback/',
#             'code':auth_code,
#         }
#         token_response=requests.post(kakao_token_api, data=data)

#         access_token=token_response.json().get('aceess_token')

#         user_info_response=requests.get('https://kapi.kakao.com/v2/user/me', headers={'Authorization':f'Bearer ${access_token}'})

#         return JsonResponse({"user_info":user_info_response.json()})

# import os
# import json
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))   # 프로젝트/accounts

# with open(os.path.join(BASE_DIR, 'accounts\secrets.json'), 'rb') as secret_file:
#     secrets = json.load(secret_file)



# class kakaoSignInView(View):
#     def get(self, request):
#         app_rest_api_key = secrets['KAKAO']["REST_API_KEY"]
#         redirect_uri = "http://localhost:8000/accounts/kakao/login/callback"
#         kakao_auth_api="https://kauth.kakao.com/oauth/authorize?response_type=code"
#         return redirect(
#             f'{kakao_auth_api}&client_id={app_rest_api_key}&redirect_uri={redirect_uri}')

# class kakaoSignInCallBackView(View):
#     def get(self, request):
#         auth_code=request.GET.get('code')
#         kakao_token_api='https://kauth.kakao.com/oauth/token'
#         data={
#             'grant_type':'authorization_code',
#             'client_id':secrets['KAKAO']["REST_API_KEY"],
#             'redirection_uri':'http://127.0.0.1:8000/accounts/kakao/login/callback/',
#             'code':auth_code,
#         }        
#         token_response=requests.post(kakao_token_api, data=data)

#         access_token=token_response.json().get('aceess_token')

#         user_info_response=requests.get('https://kapi.kakao.com/v2/user/me', headers={'Authorization':f'Bearer ${access_token}'})

#         return JsonResponse({"user_info":user_info_response.json()})


# class KakaoToDjangoLogin(SocialLoginView): 
#     adapter_class = kakao_views.KakaoOAuth2Adapter  
#     client_class = OAuth2Client 

        