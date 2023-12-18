from character_api.models import Character
import pytest

def test_create_character():
    """
    GIVEN a Character model
    WHEN a new Character is created
    THEN check the alias, name, level, health, strength, defense and speed are defined correctly
    """
    # Exercise 1: Develop this test according to the definition and make it pass in the GitHub workflow
    new_character = Character(alias='Do7', name='Zaid', level=0, health=100, strength=10, defense=10, speed=10)
    assert new_character.alias == 'Do7'
    assert new_character.name == 'Zaid'
    assert new_character.level == 0
    assert new_character.health == 100
    assert new_character.strength == 10
    assert new_character.defense == 10
    assert new_character.speed == 10