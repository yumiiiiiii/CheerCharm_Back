from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *
from rest_framework.status import *
from rest_framework import views
from rest_framework.response import Response
 

#jwt를 위해 추가함, install PyJWT
import jwt, datetime
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import AuthenticationFailed


# Create your views here.

class SignUpView(views.APIView):
    def post(self, request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'회원가입 성공', 'data':serializer.data})
        return Response({'message':'회원가입 실패', 'error':serializer.errors})

class LoginView(views.APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception = True)
        token = serializer.validated_data
        return Response({"token":token}, status=HTTP_200_OK)

    #     username=request.data['username']
    #     password=request.data=['password']


    #     #username은 unique하므로 username을 필터로 사용함.
    #     user = User.objects.filter(username=username).first()
    #     serialize_user = UserSerializer(user)
    #     json_user = JSONRenderer().render(serialize_user.data)

    #     if user is None :
    #         return AuthenticationFailed('User does not found!')

    #     # is same?
    #     if not user.check_password(password) :
    #         return AuthenticationFailed("Incorrect password!")

    #     ## JWT 구현 부분
    #     payload = {
    #     'id' : user.id,
    #     'exp' : datetime.datetime.now() + datetime.timedelta(minutes=60), #토큰만료시간
    #     'iat' : datetime.datetime.now() #토큰생성시간
    #     }

    #     token = jwt.encode(payload,"secretJWTkey",algorithm="HS256")

    #     res = Response()
    #     res.set_cookie(key='jwt', value=token, httponly=True)
    #     res.data = {
    #         'jwt' : token,
    #         "message" : 'login success'
    #     }

    #     return res

    # def get(self,req):
    #     token = req.COOKIES.get('jwt')

    #     if not token :
    #       raise AuthenticationFailed('UnAuthenticated!')

    #     try :
    #       payload = jwt.decode(token,'secretJWTkey',algorithms=['HS256'])

    #     except jwt.ExpiredSignatureError:
    #       raise AuthenticationFailed('UnAuthenticated!')

    #     user = User.objects.filter(id=payload['id']).first()
    #     serializer = UserSerializer(user)

    #     return Response(serializer.data)


    

