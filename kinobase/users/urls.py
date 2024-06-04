from django.urls import path 
from . import views


app_name = "users"

urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("register/", views.CustomRegisterView.as_view(), name="register"),
    path("profile/", views.CustomUserProfileView.as_view(), name="profile")
]
