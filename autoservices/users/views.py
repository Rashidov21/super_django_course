from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.urls import reverse_lazy
from django.views.generic import View, CreateView
from .models import CustomUser
from .forms import CustomUserCreationForm
from main.forms import ServiceCreateForm
# Create your views here.
from main.models import Service,ServiceType,Category

class CustomUserRegisterView(CreateView):
    model = CustomUser
    # fields = ("last_name","first_name","phone","email", "password")
    form_class = CustomUserCreationForm
    template_name = "auth/register.html"
    success_url = "/users/login/"
    
                
             
class CustomMasterRegisterView(View):
    
    def get(self, request):
        return render(request, "auth/register.html", {"form": CustomUserCreationForm()})
    
    def post(self, request):
        service_name = request.POST.get("service_name")
        print(service_name)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            user = form.save()
            print("User created")
            s = Service.objects.create(user=user,
                                   title=service_name,
                                   category=Category.objects.get(id=9)
                                   )
            s.save()
            print("Service created")
            authenticate(request, user)
            login(request, user)
            print("User logged in")
            return redirect("/")
        return redirect("/")