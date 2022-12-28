from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Characters, PowerStats, Appearance, Work, Connections, Biography 
from .serializers import CharactersSerializer, PowerStatsSerializer, BiographySerializer, AppearanceSerializer, WorkSerializer, ConnectionsSerializer, PowerStatsMatchUpSerializer
from .utils import get_all_characters
from django.db.models import Q
from drf_multiple_model.viewsets import FlatMultipleModelAPIViewSet
from itertools import chain
from django.http import JsonResponse

# Create your views here.


class CharactersView(viewsets.ModelViewSet):
    serializer_class = CharactersSerializer
    def get_queryset(self):
        search = self.request.query_params.get('q')
        queryset = get_all_characters(search)
        return queryset

class AllCharacterDataView(FlatMultipleModelAPIViewSet):
    def get_querylist(self):
        character_id = self.request.query_params.get('id')
        querylist = [
            {'queryset': Characters.objects.filter(id=character_id), 'serializer_class': CharactersSerializer},
            {'queryset': PowerStats.objects.filter(character__id=character_id), 'serializer_class': PowerStatsSerializer},
            {'queryset': Biography.objects.filter(character__id=character_id), 'serializer_class': BiographySerializer},
            {'queryset': Appearance.objects.filter(character__id=character_id), 'serializer_class': AppearanceSerializer},
            {'queryset': Work.objects.filter(character__id=character_id), 'serializer_class': WorkSerializer},
            {'queryset': Connections.objects.filter(character__id=character_id), 'serializer_class': ConnectionsSerializer}
        ]
        return querylist


@api_view(['GET','POST'])
def calculate_match_up(request):
    character1_id = request.query_params.get('id_one')
    character2_id = request.query_params.get('id_two')
    print(character2_id)

    try:
        character1 = PowerStats.objects.get(character__id=character1_id)
    except:
        character_1 = Characters.objects.get(id=character1_id)
        return Response({"message": f"Powerstats does not exist for {character_1.name}"}, status=status.HTTP_404_NOT_FOUND)
    character1_stats = PowerStatsMatchUpSerializer(character1)
    try:
        character2 = PowerStats.objects.get(character__id=character2_id)
    except:
        character_2 = Characters.objects.get(id=character2_id)
        return Response({"message": f"Powerstats does not exist for {character_2.name}"}, status=status.HTTP_404_NOT_FOUND)
    character2_stats = PowerStatsMatchUpSerializer(character2)
    character1_character_data = CharactersSerializer(character1.character)
    character2_character_data = CharactersSerializer(character2.character)


    character1_stats_total = ((character1.intelligence)+(character1.strength)+(character1.speed)+(character1.durability)+(character1.power)+(character1.combat))
    character2_stats_total = ((character2.intelligence)+(character2.strength)+(character2.speed)+(character2.durability)+(character2.power)+(character2.combat))
    stats_total = character1_stats_total+character2_stats_total
    character1_win_percent = round(character1_stats_total*100/stats_total)
    character2_win_percent = round(100-character1_win_percent)

    data_dict = {
        "character1": {
            "data": character1_character_data.data,
            "info": character1_stats.data,
            "percent": character1_win_percent
        },
        "character2": {
            "data": character2_character_data.data,
            "info": character2_stats.data,
            "percent": character2_win_percent
        }
    }

    return Response(data_dict)


        

