from character_api.models import Character
import pytest

def test_create_character():
    """
    GIVEN a Character model
    WHEN a new Character is created
    THEN check the alias, name, level, health, strength, defense and speed are defined correctly
    """
    # Exercise 1: Develop this test according to the definition and make it pass in the GitHub workflow
    account = Character('mmrabtei', 'marouane', '1', '100','5','5','5')
    assert account.alias == 'mmrabtei'
    assert account.name == 'marouane'
    assert account.level != None
    assert account.health == '100'
    assert account.strength == '5'
    assert account.defense == '5'
    assert account.speed == '5'