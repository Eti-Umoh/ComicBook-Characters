from django.shortcuts import render
from rest_framework import viewsets
from .models import Characters, PowerStats, Appearance, Work, Connections, Biography 
from .serializers import CharactersSerializer, PowerStatsSerializer, BiographySerializer, AppearanceSerializer, WorkSerializer, ConnectionsSerializer
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


# def get_character_data(character_id=None):
#     try:
#         character = Characters.objects.all()
#         if character_id:
#             character = Characters.objects.filter(character_id=character_id)
#             powerstats = PowerStats.objects.filter(character__id=character_id)
#             biography = Biography.objects.filter(character__id=character_id)
#             appearance = Appearance.objects.filter(character__id=character_id)
#             work = Work.objects.filter(character__id=character_id)
#             connections = Connections.objects.filter(character__id=character_id)
#         return character
#     except Exception as err:
#         return None, "failed"
    

# class AllCharacterDataView(viewsets.ModelViewSet):
#     serializer_class = CharactersCreateSerializer
#     def get_queryset(self):
#         character_id = self.request.query_params.get('id')
#         queryset = get_character_data(character_id)
#         return queryset

class AllCharacterDataView(FlatMultipleModelAPIViewSet):
    # serializer_class = CharactersCreateSerializer
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

        
    # def get_queryset(self):
    #     character_id = self.request.query_params.get('id')
    #     queryset= get_character_data(character_id)
    #     return queryset