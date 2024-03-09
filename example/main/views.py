from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,H
# Create your views here.


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