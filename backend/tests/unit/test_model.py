from character_api.models import Character
import pytest

def test_create_character():
    """
    GIVEN a Character model
    WHEN a new Character is created
    THEN check the alias, name, level, health, strength, defense and speed are defined correctly
    """
    character = Character(alias='test', name='test', level=1, health=100, strength=10, defense=10, speed=10)
    assert character.alias == 'test'
    assert character.name == 'test'
    assert character.level == 1
    assert character.health == 100
    assert character.strength == 10
    assert character.defense == 10
    assert character.speed == 10    