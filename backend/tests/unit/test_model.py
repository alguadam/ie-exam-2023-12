from character_api.models import Character
import pytest

def test_create_character():
    """
    GIVEN a Character model
    WHEN a new Character is created
    THEN check the alias, name, level, health, strength, defense and speed are defined correctly
    """
    # Exercise 1: Develop this test according to the definition and make it pass in the GitHub workflow
    character = Character('ketis','keti', 21, 5.1, 4.2, 4.6, 8.9)
    assert character.alias == 'ketis'
    assert character.name == 'keti'
    assert character.level == 21
    assert character.health == 5.1
    assert character.strength == 4.2
    assert character.defense == 4.6
    assert character.speed == 8.9