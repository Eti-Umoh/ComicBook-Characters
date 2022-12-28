from rest_framework import serializers
from .models import Characters, PowerStats, Biography, Appearance, Work, Connections

class CharactersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Characters
        fields = ('id','name','image')

class PowerStatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PowerStats
        fields = ('intelligence','strength','speed','durability','power','combat')
    
class BiographySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Biography
        fields = ('full_name','alter_ego','aliases','place_of_birth','first_appearance','publisher','alignment')

class AppearanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appearance
        fields = ('gender','race','height','weight','eye_color','hair_color')

class WorkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Work
        fields = ('occupation','base')

class ConnectionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Connections
        fields = ('group_affiliation','relative')

class PowerStatsMatchUpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PowerStats
        fields = ('intelligence','strength','speed','durability','power','combat')











# class CharactersCreateSerializer(serializers.HyperlinkedModelSerializer):
#     class PowerStatsTempSerializer(serializers.HyperlinkedModelSerializer):
#         class Meta:
#             model = PowerStats
#             exclude = ['character']
#     powerstats = PowerStatsTempSerializer()

#     class BiographyTempSerializer(serializers.HyperlinkedModelSerializer):
#         class Meta:
#             model = Biography
#             exclude = ['character']
#     biography = BiographyTempSerializer()

#     class AppearanceTempSerializer(serializers.HyperlinkedModelSerializer):
#         class Meta:
#             model = Appearance
#             exclude = ['character']
#     appearance = AppearanceTempSerializer()

#     class WorkTempSerializer(serializers.HyperlinkedModelSerializer):
#         class Meta:
#             model = Work
#             exclude = ['character']
#     work = WorkTempSerializer()

#     class ConnectionsTempSerializer(serializers.HyperlinkedModelSerializer):
#         class Meta:
#             model = Connections
#             exclude = ['character']
#     connections = ConnectionsTempSerializer()

#     class Meta:
#         model = Characters
#         fields = '__all__'
    
#     def create(self, validated_data):
#         powerstats_data = validated_data.pop('powerstats')
#         characters_instance = Characters.objects.create(**validated_data)
#         PowerStats.objects.create(character=characters_instance,**powerstats_data)
#         biography_data = validated_data.pop('biography')
#         characters_instance = Characters.objects.create(**validated_data)
#         Biography.objects.create(character=characters_instance,**biography_data)
#         appearance_data =  validated_data.pop('appearance')
#         characters_instance = Characters.objects.create(**validated_data)
#         Appearance.objects.create(character=characters_instance,**appearance_data)
#         work_data =  validated_data.pop('work')
#         characters_instance = Characters.objects.create(**validated_data)
#         Work.objects.create(character=characters_instance,**work_data)
#         connections_data = validated_data.pop('connections')
#         characters_instance = Characters.objects.create(**validated_data)
#         Connections.objects.create(character=characters_instance,**connections_data)
#         return characters_instance