from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,"index.html", context={"status":400})


def contact(request):
    return render(request,"contact.html")