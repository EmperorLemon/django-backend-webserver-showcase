from rest_framework.urls import path
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView

from .views import LoginView, SignupView

urlpatterns = [path("auth/login/", LoginView.as_view(), name="login"),
               path("auth/sign-up/", SignupView.as_view(), name="sign-up"),
               path("auth/verify-token/", TokenVerifyView.as_view(), name="verify-token"),
               path("auth/refresh-token/", TokenRefreshView.as_view(), name="refresh-token"),
               ]