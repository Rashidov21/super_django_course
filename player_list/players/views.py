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
        qs = Player.objects.select_related("club").all()
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tournaments"] = Tournament.objects.all()
        context["clubs"] = Club.objects.all()
        
        # for player in Player.objects.all():
        #     player.age = player.get_player_age()
        #     player.save()
        
        return context


class FilterView(View):
    
    def get(self, request):
        # tournament_name = request.GET.get("tournaments")
        # tournament = Tournament.objects.get(name=tournament_name)
        # from_age = int(request.GET.get("from_age"))
        # to_age = int(request.GET.get("to_age"))
        height = int(request.GET.get("height"))
        weight = int(request.GET.get("weight"))
        # club_name = request.GET.get("clubs")
        # club = Club.objects.get(name=club_name)
        # pos = request.GET.get("postions")
        # if pos:
        #     players = Player.objects.filter(club=club,position=pos)
        # if all([from_age,to_age]):
        #     players = Player.objects.filter(age__range=(from_age,to_age))
        
        if all([height,weight]):
            players = Player.objects.filter(height__gte=height, weight__gte=weight)
        
        data = {
            "object_list":players
        }
        return render(request,"filter.html",context=data)
    
    
    def post(self, request):
        pass
    