from character_api.models import Character
import pytest

def test_create_character():
    """
    GIVEN a Character model
    WHEN a new Character is created
    THEN check the alias, name, level, health, strength, defense and speed are defined correctly
    """
    # Exercise 1: Develop this test according to the definition and make it pass in the GitHub workflow
    char = Character('kakel', 'khaled')
    assert char.alias == 'kakel'
    assert char.name == 'khaled'
    assert char.level == 1
    assert char.health == 100.0
    assert char.strength == 5.0
    assert char.defense == 5.0
    assert char.speed == 5.0
    