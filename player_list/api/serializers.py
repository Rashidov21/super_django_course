from rest_framework import serializers
from players.models import Player


class PlayerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ("id","name","image","country","club","position","height","weight","transfer_summa")