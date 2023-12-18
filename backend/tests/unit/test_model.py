from character_api.models import Character
import pytest

def test_create_character():
    """
    GIVEN a Character model
    WHEN a new Character is created
    THEN check the alias, name, level, health, strength, defense and speed are defined correctly
    """
    character = Character('reoken', '11-aleja')
    assert character.alias == 'reoken'
    assert character.name == '11-aleja'
    assert character.level == 11
    assert character.health == 100.0
    assert character.strength == 7.0
    assert character.defense == 4.0
    assert character.speed == 8.0