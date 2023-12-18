from character_api.models import Character
import pytest

def test_create_character():
    """
    GIVEN a Character model
    WHEN a new Character is created
    THEN check the alias, name, level, health, strength, defense and speed are defined correctly
    """
    # Create a new Character
    character = Character(alias="Test", name="Test", level=10, health=100, strength=50, defense=30, speed=80)

    # Check if the attributes are defined correctly
    assert character.alias == "Test"
    assert character.name == "Test"
    assert character.level == 10
    assert character.health == 100
    assert character.strength == 50
    assert character.defense == 30
    assert character.speed == 80
    