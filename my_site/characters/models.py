from django.db import models

# Create your models here.
class Characters(models.Model):
    ch_id = models.CharField(null=True)
    name = models.CharField(null=True)
    image = models.ImageField(null=True)

class PowerStats(models.Model):
    character = models.ForeignKey(Characters,on_delete=models.SET_NULL,null=True)
    intelligence = models.IntegerField(null=True)
    strength = models.IntegerField(null=True)
    speed = models.IntegerField(null=True)
    durability = models.IntegerField(null=True)
    power = models.IntegerField(null=True)
    combat = models.IntegerField(null=True)

class Biography(models.Model):
    character = models.ForeignKey(Characters,on_delete=models.SET_NULL,null=True)
    full_name = models.CharField(null=True)
    alter_ego = models.CharField(null=True)
    aliases = models.CharField(null=True)
    place_of_birth = models.CharField(null=True)
    first_appearance = models.CharField(null=True)
    publisher = models.CharField(null=True)
    alignment = models.CharField(null=True)

class Appearance(models.Model):
    character = models.ForeignKey(Characters,on_delete=models.SET_NULL,null=True)
    gender = models.CharField(null=True)
    race = models.CharField(null=True)
    height = models.CharField(null=True)
    weight = models.CharField(null=True)
    eye_color = models.CharField(null=True)
    hair_color = models.CharField(null=True)

class Work(models.Model):
    character = models.ForeignKey(Characters,on_delete=models.SET_NULL,null=True)
    occupation = models.CharField(null=True)
    base = models.CharField(null=True)

class Connections(models.Model):
    character = models.ForeignKey(Characters,on_delete=models.SET_NULL,null=True)
    group_affiliation = models.CharField(null=True)
    relative = models.CharField(null=True)

