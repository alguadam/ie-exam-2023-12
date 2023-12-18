import pytest
from character_api.models import Character
from character_api import db, app



@pytest.fixture
def testing_client(scope='module'):
    with app.app_context():
        db.create_all()
        character = Character('rixman', 'Riyad')
        db.session.add(character)
        db.session.commit()

    with app.test_client() as testing_client:
        yield testing_client

    with app.app_context():
        db.drop_all()