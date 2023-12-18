from character_api.models import Character
import pytest

def test_create_character():
    """
    GIVEN a Character model
    WHEN a new Character is created
    THEN check the alias, name, level, health, strength, defense, and speed are defined correctly
    """

    character_alias = 'hero123'
    character_name = 'Hero'
    character = Character(character_alias, character_name)

    assert character.alias == character_alias
    assert character.name == character_name
    assert character.level == 1  
    assert character.health == 100.0  
    assert character.strength == 5.0  
    assert character.defense == 5.0  
    assert character.speed == 5.0  


