from rest_framework import serializers
from .models import Characters

class CharactersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Characters
        fields = ('id','name','image')