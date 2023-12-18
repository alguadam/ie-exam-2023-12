from character_api.models import Character
import pytest

def test_create_character():
    """
    GIVEN a Character model
    WHEN a new Character is created
    THEN check the alias, name, level, health, strength, defense and speed are defined correctly
    """
    # Exercise 1: Develop this test according to the definition and make it pass in the GitHub workflow
    
    character = Character('johnusername', 'John Doe')
    assert character.alias == 'johnusername'
    assert character.name == 'John Doe'
    assert character.level == 1
    assert character.health == 100.0
    assert character.strength == 5.0
    assert character.defense == 5.0
    assert character.speed == 5.0

