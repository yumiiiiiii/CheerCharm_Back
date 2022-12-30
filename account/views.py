from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *
from rest_framework import views
from rest_framework.response import Response 


# Create your views here.

class SignUpView(views.APIView):
    def post(self, request):
        serializer=UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'회원가입 성공', 'data':serializer.data})
        return Response({'message':'회원가입 실패', 'error':serializer.errors})

class LoginView(views.APIView):
    def post(self, request):
        serializer=UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            return Response({'message':"로그인 성공", 'data':serializer.data})
        return Response({'message':"로그인 실패", 'data':serializer.errors})

