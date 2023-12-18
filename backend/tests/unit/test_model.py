from character_api.models import Character
import pytest

def test_create_character():
    """
    GIVEN a Character model
    WHEN a new Character is created
    THEN check the alias, name, level, health, strength, defense and speed are defined correctly
    """
    # Exercise 1: Develop this test according to the definition and make it pass in the GitHub workflow
    
    character = Character('johnusername', 'John Doe')
    assert character.alias == 'johnusername'
    assert character.name == 'John Doe'
    assert character.level == 1
    assert character.health == 100.0
    assert character.strength == 5.0
    assert character.defense == 5.0
    assert character.speed == 5.0

    # okay so here just added a character with an alias and name, since those can't be null. 
    # and then we check if they match what we entered with assert and also check the level, health
    # strength, defense, speed, these are all default values, hence I didn't enter them while creating 
    # as they automatically create, and we check if they create to their default so its a good unit test
    # as our user stories may have an acceptance criteria of defualt values set to these. 