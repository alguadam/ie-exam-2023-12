from character_api.models import Character
import pytest

def test_create_character():
    """
    GIVEN a Character model
    WHEN a new Character is created
    THEN check the alias, name, level, health, strength, defense and speed are defined correctly
    """

    # Create a new character instance
    character = Character(alias="maudhelen", name="MaudHelen")

    # Assert that all attributes are set correctly as per model's __init__ and defaults
    assert character.alias == "maudhelen"
    assert character.name == "MaudHelen"
    assert character.level == 1
    assert character.health == 100.0
    assert character.strength == 5.0
    assert character.defense == 5.0
    assert character.speed == 5.0