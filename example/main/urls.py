from django.urls import path 
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home_page_view, name="home"),
    path('about/', views.about),
    path('contact/', views.contact),
    
    path('product/<int:product_id>', views.product_detail),
    
    path('super/',views.super_page)
]
