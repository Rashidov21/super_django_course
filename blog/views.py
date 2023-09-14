from django.shortcuts import render , HttpResponse
from django.views.generic import ListView
from faker import Faker

from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post


def generate_data(request):
    fake = Faker()
    # for i in range(10):
        # Post.objects.create()
    return HttpResponse("<span>done</span>")