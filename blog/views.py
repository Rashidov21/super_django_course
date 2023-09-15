from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render , HttpResponse
from django.views.generic import ListView
from faker import Faker

from .models import Post

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
    paginate_by = 20
    
    def get_queryset(self) -> QuerySet[Any]:
        qs = super().get_queryset()
        qs = Post.objects.filter(active=True).select_related("category","author").prefetch_related("tag")
        return qs


def generate_data(request):
    fake = Faker()
    # for i in range(10):
        # Post.objects.create()
    return HttpResponse("<span>done</span>")
