from rest_framework import generics
from .serializers import PlayerListSerializer
from players.models import Player
# CRUD 
# Create 
# Retrieve
# Update 
# Delete
# Create your views here.
class PlayerAPIList(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerListSerializer
    
class PlayerAPIDetail(generics.RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerListSerializer