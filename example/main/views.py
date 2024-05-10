from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,H
from django.views.generic import ListView
# Create your views here.


class TestListView(ListView):
    pass

def home_page_view(request):
    return HttpResponse("<h2>Home Page</h2>")


def about(request):
    return HttpResponse("<h2>About Page</h2>")


def contact(request):
    return HttpResponse("<h2>Contact Page</h2>")


def product_detail(request,product_id):
    
    return HttpResponse(f"<h2>Product N= {product_id}</h2>")


def super_page(request):
    return HttpResponseRedirect('/contact/')