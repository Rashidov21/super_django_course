import sqlite3

from django.shortcuts import render
import datetime
# from .parser_data import get_player_data
from .models import Players

# Create your views here.


def main():
    pl = Players.objects.all()
    for i in pl:
        print(i.dr)
        i.age = 2023 - int(str(i.dr).split("-")[0])
        i.save()


def home(request):
    main()
    # print(get_player_data())
    template_name = 'home.html'
    return render(request, template_name)
