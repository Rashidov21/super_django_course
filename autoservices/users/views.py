from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
# Create your views here.


class CustomUserRegisterView(CreateView):
    model = User
    fields = "__all__"
    template_name = "auth/register.html"
    success_url = "/"