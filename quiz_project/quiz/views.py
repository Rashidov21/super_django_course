from django.shortcuts import render
from .models import Answer ,Category, Question
# Create your views here.
def home_page(request):
    return render(request,"index.html")

def quiz_page(request):
    Question = Answer.objects.all()
    context = {
        'questions':Question,
    }
    return render(request,"quiz.html" , context)


def result_page(request):
    return render(request,"result.html")