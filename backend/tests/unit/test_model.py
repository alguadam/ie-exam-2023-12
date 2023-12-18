from character_api.models import Character
import pytest

def test_create_character():
    """
    GIVEN a Character model
    WHEN a new Character is created
    THEN check the alias, name, level, health, strength, defense and speed are defined correctly
    """
    # Create a character with test data
    character = Character( 
        alias= 'Ana 123', 
        name= 'Test Ana',
        level= 1,
        health= 100,
        strength= 10,
        defense= 10,
        speed= 5
    )
    
    # Assert that each attribute is set correctly
    assert character.alias == 'Ana123'
    assert character.name == 'Test Ana'
    assert character.level == 1
    assert character.health == 100
    assert character.strength == 10
    assert character.defense == 10
    assert character.speed == 5

