from django.shortcuts import render,redirect
from .models import Club, Player
# Create your views here.


def index(request):
    players = Player.objects.all()
    clubs = Club.objects.all()
    return render(request, 'index.html', context={'players': players,"clubs":clubs})


def add(request):
    clubs = Club.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        date_of_bith = request.POST.get('date')
        country = request.POST.get('country')
        club = request.POST.get('club')
        position = request.POST.get('position')
        height = request.POST.get('height')
        weight = request.POST.get('weight')

        Player.objects.create(
            name=name,
            date_of_bith=date_of_bith,
            country=country,
            club=Club.objects.get(id=int(club)),
            position=position,
            height=float(height),
            weight=float(weight),
        )
        return redirect("/")
    return render(request, 'add.html', context={'clubs': clubs})


def club_players(request, club_id):
    players = Player.objects.filter(club=club_id)
    return render(request, 'index.html', context={'players': players})

def player_postions(request,position):
    players = Player.objects.filter(position=position)
    return render(request, 'index.html', context={'players': players})

def player_country(request,country_code):
    players = Player.objects.filter(country=country_code)
    return render(request, 'index.html', context={'players': players})