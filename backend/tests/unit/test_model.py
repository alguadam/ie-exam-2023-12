from character_api.models import Character
import pytest

def test_create_character():
    """
    GIVEN a Character model
    WHEN a new Character is created
    THEN check the alias, name, level, health, strength, defense and speed are defined correctly
    """
    character = Character('rixman', 'Riyad')
    assert character.alias == 'rixman'
    assert character.name == 'Riyad'
    assert character.level != 10
    assert character.health == 80.0
    assert character.strength == 5.0
    assert character.defense == 3.0
    assert character.speed == 4.0