from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages

from django.views.generic import View

from .models import Profile
from .forms import CustomLoginForm
# Create your views here.



class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = "auth/login.html"



class CustomRegisterView(View):
    
    def get(self,request):
        return render(request,"auth/registration.html")
    
    
    def post(self,request):
        username = request.POST.get("email").split("@")[0].lower()
        email = request.POST.get("email")
        name = request.POST.get("name")
        password = request.POST.get("password")
        password_confirmation = request.POST.get("password_confirmation")
    
        
        if password == password_confirmation:
            u = User.objects.create(
                username=username,
                first_name=name,
                email=email ,
                password=password)
            Profile.objects.create(user=u)
            # xozir hosil bolgan user object ni topish uchun 
            authenticate(request,username=u.username, password=u.password)
            # tizimga kirgizish uchun
            login(request,u)
            messages.success(request,"OK")
            return redirect("/")
        else:
            messages.error(request,"Wrong password")
            return render(request,"auth/registration.html")
            
            
            
class CustomUserProfileView(LoginRequiredMixin,View):
    
    def get(self,request):
        
        return render(request,"auth/profile.html")
    
    def post(self,request):
        image = request.FILES.get("avatar_file")
        email = request.POST.get("email")
        name = request.POST.get("name")
        password = request.POST.get("password")
        password_confirmation = request.POST.get("password_confirmation")
        
        user = request.user
  
        user.profile.image = image
        user.email = email
        user.name = name
        if password and password_confirmation:
            if password == password_confirmation:
                user.set_password(password)
                user.save()
        else:
            pass
        return render(request,"auth/profile.html")
        