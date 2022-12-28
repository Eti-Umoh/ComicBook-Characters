from characters.models import Characters
from characters.utils import get_super_hero_by_id, create_biography_record

characters = Characters.objects.exclude(id=1)
for character in characters:
    ch_id = character.ch_id
    hero_response = get_super_hero_by_id(ch_id)
    full_name = hero_response['biography']['full-name']
    alter_egos = hero_response['biography']['alter-egos']
    aliases = hero_response['biography']['aliases']
    place_of_birth = hero_response['biography']['place-of-birth']
    first_appearance = hero_response['biography']['first-appearance']
    publisher = hero_response['biography']['publisher']
    alignment = hero_response['biography']['alignment']
    print(full_name)
    bio = create_biography_record(character, full_name, alter_egos, aliases, place_of_birth, first_appearance, publisher, alignment)
    print(bio)
    
# character = Characters.objects.get(id=1)
# ch_id = character.ch_id
# hero_response = get_super_hero_by_id(ch_id)
# full_name = hero_response['biography']['full-name']
# alter_egos = hero_response['biography']['alter-egos']
# aliases = hero_response['biography']['aliases']
# place_of_birth = hero_response['biography']['place-of-birth']
# first_appearance = hero_response['biography']['first-appearance']
# publisher = hero_response['biography']['publisher']
# alignment = hero_response['biography']['alignment']
# bio = create_biography_record(character, full_name, alter_egos, aliases, place_of_birth, first_appearance, publisher, alignment)