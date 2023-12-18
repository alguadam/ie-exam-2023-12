from character_api.models import Character
import pytest

def test_create_character():
    """
    GIVEN a Character model
    WHEN a new Character is created
    THEN check the alias, name, level, health, strength, defense and speed are defined correctly
    """
    character = Character('kathe', 'papilioau')
    # Assert that the attributes are as expected
    assert character.alias == 'Test Alias'
    assert character.name == 'Test Name'
    assert character.level == 1
    assert character.health == 100
    assert character.strength == 10
    assert character.defense == 10
    assert character.speed == 10