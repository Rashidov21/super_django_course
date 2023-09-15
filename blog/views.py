<<<<<<< Updated upstream
from django.shortcuts import render , HttpResponse
from django.views.generic import ListView
from faker import Faker
=======
from typing import Any
from django.shortcuts import render, HttpResponse
import json
from django.utils.text import slugify
from django.views.generic import ListView
from .models import Post, Category, Tag
import random
from faker import Faker
from django.contrib.auth.models import User
>>>>>>> Stashed changes


# def generate_posts():
#     fake = Faker()
#     title = fake.text(100)
#     body = {'delta':fake.text(1000)}
#     views = fake.random.randint(1,600)
#     up = fake.random.randint(1,700)
#     down = fake.random.randint(1,700)
#     categories = Category.objects.all()
#     tags = Tag.objects.all()
#     for i in range(20):
#         try:
#             creating =  Post.objects.create(
#                 title = title,
#                 slug = slugify(title),
#                 body = json.dumps(body),
#                 up = up,
#                 down = down,
#                 views = views,) 
#         except Exception as error:
#             creating.slug = slugify(fake.text(100))
#         else:
#             print("ok ok ")
#         creating.category = random.choice(categories)
#         for i in range(random.randint(1,4)):
#             creating.tag.add(random.choice(tags))
#         creating.save()
# generate_posts()
fake = Faker()
# Create your views here.
class PostListView(ListView):
    model = Post
<<<<<<< Updated upstream


def generate_data(request):
    fake = Faker()
    # for i in range(10):
        # Post.objects.create()
    return HttpResponse("<span>done</span>")
=======
    
    def get_context_data(self):
        context = super().get_context_data()

        return context
    
list_icons = [
    'fab fa-js','fab fa-python','fab fa-google', 'fas fa-mug-hot', 'fas fa-cat', 'fas fa-cloud', 
    'fas fa-heart', 'fas fa-check', 'fas fa-bomb', 'fab fa-facebook'
]
def test(request):
    posts = Post.objects.all()
    for i in posts:
        # i.title = fake.text(100)
        # i.author = User.objects.last()
        # i.body = fake.text(600)
        i.icon = random.choice(list_icons)
        i.save()
    return HttpResponse("salom")
>>>>>>> Stashed changes
