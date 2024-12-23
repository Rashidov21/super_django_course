from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Category,Post,Comments
from django.db.models import Max

# Create your views here.
def home(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    paginator = Paginator(posts,5)
    page_number = request.GET.get("page")
    page_objects = paginator.get_page(page_number)
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        category = Category.objects.get(id=int(request.POST.get("category")))
        if all([title,content,category]):
            Post.objects.create(title=title, content=content, category=category)
            messages.success(request,"Post created !")
            
    return render(request,"index.html", context={"categories":categories, "page_obj":page_objects})


def detail(request,post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        comment = request.POST.get("comment")
        Comments.objects.create(
            name=name,
            email=email,
            comment=comment,
            post=post
        )
        messages.success(request,"Comment created successfully !")
    else:
        messages.success(request,"Sorry, something went wrong !")
       
        
    return render(request,"detail.html", context={"post":post})


def add_votes(request,post_id):
    post = Post.objects.get(id=post_id)
    
    
    request.session.modified = True
    try:
        voted_posts = request.session["vote_list"]
    except:
        voted_posts = request.session["vote_list"] = []
    if post.id in voted_posts:
        voted_posts.remove(post.id)
        post.votes -= 1
        post.save()
        messages.info(request,"You removed your vote")
    else:
        voted_posts.append(post.id)
        post.votes += 1
        post.save()
        messages.info(request,"You added your vote")

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def filter_vote(request,filter_by_what):
    if filter_by_what.lower() == "by_votes":
        categories = Category.objects.all()
        posts = Post.objects.annotate(Max("votes")).order_by("-votes__max")
        paginator = Paginator(posts,5)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return render(request,"index.html", context={"categories":categories, "page_obj":page_obj})
    else:
        return redirect("/")