from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


app_name = "users"


urlpatterns = [
    path("login/", auth_views.LoginView.as_view(
        template_name="auth/login.html"
    ), name="login"),
    
    path("register/", views.CustomUserRegisterView.as_view(), name='register')
]
