from django.db import models
from django.contrib.postgres.fields import ArrayField

def default_list(self):
    return list()

# Create your models here.
class Characters(models.Model):
    ch_id = models.TextField(null=True)
    name = models.TextField(null=True)
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
    full_name = models.TextField(null=True)
    alter_ego = models.TextField(null=True)
    aliases = ArrayField(models.TextField(null=True), null=True, default=default_list)
    place_of_birth = models.TextField(null=True)
    first_appearance = models.TextField(null=True)
    publisher = models.TextField(null=True)
    alignment = models.TextField(null=True)

class Appearance(models.Model):
    character = models.ForeignKey(Characters,on_delete=models.SET_NULL,null=True)
    gender = models.TextField(null=True)
    race = models.TextField(null=True)
    height = ArrayField(models.TextField(null=True), null=True, default=default_list)
    weight = ArrayField(models.TextField(null=True), null=True, default=default_list)
    eye_color = models.TextField(null=True)
    hair_color = models.TextField(null=True)

class Work(models.Model):
    character = models.ForeignKey(Characters,on_delete=models.SET_NULL,null=True)
    occupation = models.TextField(null=True)
    base = models.TextField(null=True)

class Connections(models.Model):
    character = models.ForeignKey(Characters,on_delete=models.SET_NULL,null=True)
    group_affiliation = models.TextField(null=True)
    relative = models.TextField(null=True)

