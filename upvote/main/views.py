from django.shortcuts import render
from django.contrib import messages
from .models import Category,Post

# Create your views here.
def home(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        category = Category.objects.get(id=int(request.POST.get("category")))
        if all([title,content,category]):
            Post.objects.create(title=title, content=content, category=category)
            messages.success(request,"Post created !")
            
    return render(request,"index.html", context={"categories":categories, "posts":posts})


def detail(request):
    return render(request,"detail.html")