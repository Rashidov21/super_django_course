from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
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


def custom_logout(request):
    logout(request)
    return redirect("/")


class ProfileView(View):
    
    
    def get(self, request):
        form = ServiceCreateForm()
        if request.user.service:
            print("OK")
        services = ServiceType.objects.all()
        return render(request, "auth/settings.html", {"services": services,"form":form})
    
    def post(self, request):
        form = ServiceCreateForm(request.POST,user=request.user)
        if form.is_valid():
            form.save()
            return redirect("/")
        
        return render(request, "auth/settings.html")
    
    
    
    


#   image = request.FILES.get("image")
#         title = request.POST.get("title")
#         address = request.POST.get("address")
#         orientation = request.POST.get("orientation")
#         phone_1 = request.POST.get("phone_1")
#         phone_2 = request.POST.get("phone_2")
#         description = request.POST.get("description")
#         service_types = request.POST.getlist("service_types")
#         from_time = request.POST.get("from_time")
#         to_time = request.POST.get("to_time")
#         hours24 = request.POST.get("24hours")
#         du = request.POST.get("du")
#         se = request.POST.get("se")
#         chor = request.POST.get("chor")
#         pay = request.POST.get("pay")
#         jum = request.POST.get("jum")
#         shan = request.POST.get("shan")
#         yak = request.POST.get("yak")