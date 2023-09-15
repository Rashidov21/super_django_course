from django.urls import path
from . import views
urlpatterns = [
    path("", views.PostListView.as_view(), name='blog'),
<<<<<<< Updated upstream
    path('gen/', views.generate_data)
=======
    path('test/', views.test, name='test')
>>>>>>> Stashed changes
]
