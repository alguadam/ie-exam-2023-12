from character_api.models import Character
import pytest


def test_create_character():
    """
    GIVEN a Character model
    WHEN a new Character is created
    THEN check the new character's fields are defined correctly
    """
    alias = 'smorenolasa'
    name = 'sofia moreno'
    character = Character(alias, name)

    assert character.alias == alias
    assert character.name == name
    assert character.level == 1
    assert character.health == 100.0
    assert character.strength == 5.0
    assert character.defense == 5.0
    assert character.speed == 5.0