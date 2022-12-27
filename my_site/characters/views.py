from django.shortcuts import render
from rest_framework import viewsets, status
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
    
# def calculate_matchup(character1_id,character2_id):
#     character1 = PowerStats.objects.filter(character__id=character1_id)
#     character2 = PowerStats.objects.filter(character__id=character2_id)
#     return character1, character2
class CalculateMatchUpView(viewsets.ModelViewSet):
    serializer_class = PowerStatsMatchUpSerializer
    def get_queryset(self):
        character1_id = self.request.query_params.get('idone')
        character2_id = self.request.query_params.get('idtwo')
        character1 = PowerStats.objects.get(character__id=character1_id)
        character2 = PowerStats.objects.get(character__id=character2_id)
        character1_stats_total = ((character1.intelligence)+(character1.strength)+(character1.speed)+(character1.durability)+(character1.power)+(character1.combat))
        character2_stats_total = ((character2.intelligence)+(character2.strength)+(character2.speed)+(character2.durability)+(character2.power)+(character2.combat))
        stats_total = character1_stats_total+character2_stats_total
        character1_win_percent = character1_stats_total*100/stats_total
        character2_win_percent = 100-character1_win_percent
        content = JsonResponse({character1.character.name:character1_win_percent}, safe=False, status=status.HTTP_200_OK )
        print(content)
        return character1,character2,content


        



# class AllCharacterDataView(viewsets.ModelViewSet):
#     serializer_class = CharactersCreateSerializer
#     def get_queryset(self):
#         character_id = self.request.query_params.get('id')
#         queryset = get_character_data(character_id)
#         return queryset
        
    # def get_queryset(self):
    #     character_id = self.request.query_params.get('id')
    #     queryset= get_character_data(character_id)
    #     return queryset