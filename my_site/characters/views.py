from django.shortcuts import render
from rest_framework import viewsets
from .models import Characters, PowerStats, Appearance, Work, Connections, Biography 
from .serializers import CharactersSerializer, PowerStatsSerializer, BiographySerializer, AppearanceSerializer, WorkSerializer, ConnectionsSerializer, PowerStatsMatchUpSerializer
from .utils import get_all_characters
from django.db.models import Q
from drf_multiple_model.viewsets import FlatMultipleModelAPIViewSet

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
    
def calculate_matchup(character1_id,character2_id):
    character1 = PowerStats.objects.filter(character__id=character1_id)
    character2 = PowerStats.objects.filter(character__id=character2_id)
    return character1, character2
class CalculateMatchUpView(viewsets.ModelViewSet):
    serializer_class = PowerStatsMatchUpSerializer
    def get_queryset(self):
        character1_id = self.request.query_params.get('idone')
        character2_id = self.request.query_params.get('idtwo')
        queryset = calculate_matchup(character1_id,character2_id)
        return queryset
        



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