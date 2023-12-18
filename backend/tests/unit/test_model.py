from character_api.models import Character
import pytest
from character_api import db, app

def test_create_character():
    """
    GIVEN a Character model
    WHEN a new Character is created
    THEN check the new character's fields are defined correctly
    """
    alias = 'test_alias'
    name = 'test_name'
    character = Character(alias, name)

    assert character.alias == alias
    assert character.name == name
    assert character.level == 1
    assert character.health == 100.0
    assert character.strength == 5.0
    assert character.defense == 5.0
    assert character.speed == 5.0

@pytest.fixture
def testing_client(scope='module'):
    with app.app_context():
        db.create_all()
        character = Character('alguadam2', 'Alvaro Guadamillas')
        db.session.add(character)
        db.session.commit()

    with app.test_client() as testing_client:
        yield testing_client

    with app.app_context():
        db.drop_all()