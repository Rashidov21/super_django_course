from django.urls import path

from . import views

app_name = "players"

urlpatterns = [
    path("", views.HomePageView.as_view(), name='home'),
    path("filter/", views.FilterView.as_view(), name="filter"),
    path("dynamic/", views.dynamic, name="dynamic")
]

