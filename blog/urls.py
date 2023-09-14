from django.urls import path
from . import views
urlpatterns = [
    path("", views.PostListView.as_view(), name='blog'),
    path('gen/', views.generate_data)
]
