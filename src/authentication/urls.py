from django.urls import path

from .views import LoginView

urlpatterns = [path("auth/login/", LoginView.as_view(), name="login"),
               path("auth/token/verify/", name="verify-token")]