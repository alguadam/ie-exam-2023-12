from character_api.models import Character
import pytest

def test_create_character():
    """
    GIVEN a Character model
    WHEN a new Character is created
    THEN check the alias, name, level, health, strength, defense and speed are defined correctly
    """
    # Exercise 1: Develop this test according to the definition and make it pass in the GitHub workflow
    new_character = Character(alias='alguadam', name='Alvaro Guadamillas')
    assert new_character.alias == 'Alvaro Guadamillas'
    assert new_character.name == 'Zaid'
    assert new_character.level == 1
    assert new_character.health == 100.0
    assert new_character.strength == 5.0
    assert new_character.defense == 5.0
    assert new_character.speed == 5.0