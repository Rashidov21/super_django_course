from django.urls import path 
from . import views

app_name = "api"

urlpatterns = [
    path("list/", views.PlayerAPIList.as_view(), name="list"),
    path("detail/<int:pk>/", views.PlayerAPIDetail.as_view(), name="detail"),
]
