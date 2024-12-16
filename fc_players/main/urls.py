from django.urls import path 
from . import views

app_name = 'main'

urlpatterns = [
    path("", views.index, name="index"),
    path('add/', views.add, name="add"),
    path("club-players/<int:club_id>/", views.club_players, name="club_players"),
    path("positions/<str:position>/", views.player_postions, name="player_postions"),
    path("country/<str:country_code>", views.player_country, name="player_country"),
]