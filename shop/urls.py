from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', index, name='index')
]
