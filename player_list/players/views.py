from typing import Any
from django.shortcuts import render
from django.views.generic import ListView 
from django.views.generic.base import View

# Create your views here.
from .models import *


class HomePageView(ListView):
    model = Player
    template_name = "index.html"
    # context_object_name = "players"
    
    # SELECT * FROM table_name
    # Model.objects.all()
    # object_list - data list 
    
    def get_queryset(self):
        return super().get_queryset()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tournaments"] = Tournament.objects.all()
        context["clubs"] = Club.objects.all()
        return context


class FilterView(View):
    
    def get(self, request):
        tournament_name = request.GET.get("tournaments")
        club_name = request.GET.get("clubs")
        tournament = Tournament.objects.get(name=tournament_name)
        club = Club.objects.get(name=club_name)
        pos = request.GET.get("postions")
        if pos:
            players = Player.objects.filter(club=club,position=pos)
        else:
            players = Player.objects.filter(club=club)
        
        data = {
            "object_list":players
        }
        return render(request,"filter.html",context=data)
    
    
    def post(self, request):
        pass
    