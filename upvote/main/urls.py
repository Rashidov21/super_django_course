from django.urls import path 
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home, name="home"),
    path("detail/<int:post_id>", views.detail, name="detail"),
    path("add/vote/<int:post_id>", views.add_votes, name="add_votes"),
    path("filter/<str:filter_by_what>", views.filter_vote, name="filter")
]
