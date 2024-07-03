from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import CustomUser
from .forms import CustomUserCreationForm
# Create your views here.


class CustomUserRegisterView(CreateView):
    model = CustomUser
    # fields = ("last_name","first_name","phone","email", "password")
    form_class = CustomUserCreationForm
    template_name = "auth/register.html"
    success_url = "/users/login/"
    