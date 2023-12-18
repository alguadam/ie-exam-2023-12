from character_api.models import Character
import pytest

def test_create_character():
    """
    GIVEN a Character model
    WHEN a new Character is created
    THEN check the alias, name, level, health, strength, defense and speed are defined correctly
    """
    # Exercise 1: Develop this test according to the definition and make it pass in the GitHub workflow
    char = Character('xx', 'name', '100', '10.0', '10.0', '10.0', '10.0')
    assert char.alias == 'xx'
    assert char.name == 'name'
    assert char.level == '100'
    assert char.health == '10.0'
    assert char.strength == '10.0'
    assert char.defense == '10.0'
    assert char.speed == '10.0'