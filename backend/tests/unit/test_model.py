from character_api.models import Character
import pytest

def test_create_character():
    """
    GIVEN a Character model
    WHEN a new Character is created
    THEN check the alias, name, level, health, strength, defense and speed are defined correctly
    """
    character = Character(alias="Batman", name="Bruce Wayne")
    assert character.alias == "Batman"
    assert character.name == "Bruce Wayne"
    assert character.level == 1
    assert character.health == 100
    assert character.strength == 5
    assert character.defense == 5
    assert character.speed == 5

    