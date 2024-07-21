from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView

# Create your views here.
class LoginView(APIView):
    def get(self, request):
        return Response(data={"message" : "Hello World!"}, status=status.HTTP_200_OK)
