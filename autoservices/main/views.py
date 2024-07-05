from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from .models import Category

class HomePageView(ListView):
    template_name = "index.html"
    model = Category