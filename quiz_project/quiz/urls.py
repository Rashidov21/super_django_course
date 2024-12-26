from django.urls import path 
from . import views

app_name = "quiz"

urlpatterns = [
    path('',views.home_page, name="home"),
    path('quiz/',views.quiz_page, name="quiz"),
    path('result/',views.result_page, name="result")
]
