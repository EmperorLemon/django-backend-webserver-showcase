from django.contrib.auth.models import User

from rest_framework import status as http_status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LoginSerializer, SignupSerializer
from .utils.login_utils import attempt_login

# Create your views here.
class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data.get("email")
            password = serializer.validated_data.get("password")

            response, status = attempt_login(request=request, username=email, password=password)

            return Response(data=response, status=status)
        
        return Response(serializer.errors, status=http_status.HTTP_400_BAD_REQUEST)
    
class SignupView(APIView):
    serializer_class = SignupSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user_data: dict = {
                "first_name": serializer.validated_data.get("first_name"),
                "last_name": serializer.validated_data.get("last_name"),
                "username": serializer.validated_data.get("username"),
                "email_address": serializer.validated_data.get("email_address"),
            }
