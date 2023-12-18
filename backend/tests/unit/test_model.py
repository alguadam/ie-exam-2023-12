from character_api.models import Character
import pytest

def test_create_character():
    """
    GIVEN a Character model
    WHEN a new Character is created
    THEN check the alias, name, level, health, strength, defense and speed are defined correctly
    """
    # Exercise 1: Develop this test according to the definition and make it pass in the GitHub workflow
    character = Character(alias='Juni', name='Joseph', level=1, health=1, strength=1, defense=1, speed=1)
    assert character.alias == 'Juni'
    assert character.name == 'Joseph'
    assert character.level == 1
    assert character.health == 1
    assert character.strength == 1
    assert character.defense == 1
    assert character.speed == 1