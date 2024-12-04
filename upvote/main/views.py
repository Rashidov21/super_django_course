from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def home(request):
    # return JsonResponse({"status":404})
    return render(request,"index.html", context={"status":400})