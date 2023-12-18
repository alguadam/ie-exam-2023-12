from character_api.models import Character
import pytest

def test_create_character():
    """
    GIVEN a Character model
    WHEN a new Character is created
    THEN check the alias, name, level, health, strength, defense and speed are defined correctly
    """
    # Exercise 1: Develop this test according to the definition and make it pass in the GitHub workflow
    
    character = Character('johnuser', 'John Doe', 1,  'Spain', '€')
    assert character.name == 'John Doe'
    assert character.country == 'Spain'
    assert character.currency == '€'
    assert character.account_number != None
    assert character.balance == 0.0
    assert character.status == 'Active'

