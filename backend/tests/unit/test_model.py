from character_api.models import Character
import pytest

def test_create_character():

    character = Character(alias="Hero", name="John Doe", level=1, health=100, strength=10, defense=5, speed=3)

    # Assertions to check if each attribute is set correctly
    assert character.alias == "Hero"
    assert character.name == "John Doe"
    assert character.level == 1
    assert character.health == 100
    assert character.strength == 10
    assert character.defense == 5
    assert character.speed == 3
