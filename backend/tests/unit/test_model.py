from character_api.models import Character
import pytest

def test_create_character():
    """
    GIVEN a Character model
    WHEN a new Character is created
    THEN check the alias, name, level, health, strength, defense and speed are defined correctly
    """
    # Exercise 1: Develop this test according to the definition and make it pass in the GitHub workflow
    
    character = Character('johndoe_alias', 'John Doe')
    assert character.alias == 'johndoe_alias'
    assert character.name == 'John Doe'
    assert character.level == 5
    assert character.health == 100.0
    assert character.strength == 10.0
    assert character.defense == 10.0
    assert character.speed == 10.0
