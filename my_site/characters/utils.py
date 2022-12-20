from .models import Characters,Connections,PowerStats,Work,Appearance,Biography
import requests
from django.conf import settings


def create_character(ch_id,name,image):
    try:
        character = Characters.objects.create(
            ch_id=ch_id,
            name=name,
            image=image
        )

        return character
    except Exception as err:
        return None

def create_powerstats_record(character,intelligence,strength,speed,durability,power,combat):
    try:
        power_stats = PowerStats.objects.create(
            character=character,
            intelligence=intelligence,
            strength=strength,
            speed=speed,
            durability=durability,
            power=power,
            combat=combat
        )

        return power_stats
    except Exception as err:
        return None

def create_biography_record(character,full_name,alter_egos,aliases,place_of_birth,first_appearance,publisher,alignment):
    try:
        biography = Biography.objects.create(
            character=character,
            full_name=full_name,
            alter_egos=alter_egos,
            aliases=aliases,
            place_of_birth=place_of_birth,
            first_appearance=first_appearance,
            publisher=publisher,
            alignment=alignment
        )

        return biography
    except Exception as err:
        return None

def create_appearance_record(character,gender,race,height,weight,eye_color,hair_color):
    try:
        appearance = Appearance.objects.create(
            character=character,
            gender=gender,
            race=race,
            height=height,
            weight=weight,
            eye_color=eye_color,
            hair_color=hair_color
        )

        return appearance
    except Exception as err:
        return None

def create_work_record(character,occupation,base):
    try:
        work = Work.objects.create(
            character=character,
            occupation=occupation,
            base=base
        )

        return work
    except Exception as err:
        return None

def create_connections_record(character,group_affiliation,relative):
    try:
        connections = Connections.objects.create(
            character=character,
            group_affiliation=group_affiliation,
            relative=relative
        )

        return connections
    except Exception as err:
        return None

def get_super_hero_by_id(hero_id):
    try:
        req = requests.get(
            f"https://superheroapi.com/api.php/{settings.SP_ACCESS_TOKEN}/{hero_id}",
        )

        if req.status_code != 200:
            return req.json()

        response = req.json()
        return response
    except Exception as err:
        return None