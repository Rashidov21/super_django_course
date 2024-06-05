from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages

from django.views.generic import View

from movie.models import Movie
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
        print(image)
        email = request.POST.get("email")
        name = request.POST.get("name")
        password = request.POST.get("password")
        password_confirmation = request.POST.get("password_confirmation")
        
        user = request.user
        if image:
            user.profile.image = image
            user.profile.save()
            messages.success(request,"Profile image set")
        if email:
            user.email = email
            user.save()
            messages.success(request,"User email set")
        if name:
            user.first_name = name
            user.save()
            messages.success(request,"User firstname set")
            
        if password and password_confirmation:
            if password == password_confirmation:
                user.set_password(password)
                user.save()
                messages.success(request,"Password changed")
        else:
            pass
        return render(request,"auth/profile.html")


class ProfileHistoryView(LoginRequiredMixin,View):
    
    def get(self,request):
        context = {}
        context["object_list"] = self.request.user.profile.history.all()
        return render(request,"history.html", context=context)
    
    
    
class ProfileClearHistoryView(LoginRequiredMixin,View):
    
    def get(self,request):
        request.user.profile.history.clear()
        return HttpResponseRedirect("/users/profile/history/")
    
    
class ProfileFavoritesView(LoginRequiredMixin,View):
    
    def get(self,request):
        context = {
            "object_list":self.request.user.profile.favorites.all()
        }
        return render(request,"favorites.html", context=context)
    
class AddToFavoritesView(LoginRequiredMixin,View):
    
    def get(self,request,movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        profile = request.user.profile
        
        if profile.favorites.filter(id=movie_id).exists():
            profile.favorites.remove(movie)
            messages.info(request,"Movie deleted")
        else:
            profile.favorites.add(movie)
            messages.info(request,"Movie added")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    

class ProfileClearFavoritesView(LoginRequiredMixin,View):
    
    def get(self,request):
        request.user.profile.favorites.clear()
        return HttpResponseRedirect("/users/profile/favorites/")