from django.contrib.auth.models import User

from rest_framework import status as http_status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LoginSerializer
from .utils.login_utils import attempt_login

# Create your views here.
class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")

            response, status = attempt_login(request=request, username=username, password=password)

            return Response(data=response, status=status)
        
        return Response(serializer.errors, status=http_status.HTTP_400_BAD_REQUEST)
