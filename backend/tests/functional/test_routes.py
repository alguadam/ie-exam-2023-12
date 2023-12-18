from character_api import app
import pytest

@pytest.fixture
def testing_client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_dummy_wrong_path(testing_client):
    response = testing_client.get('/wrong_path')
    assert response.status_code == 404  


def test_get_characters(testing_client):
    response = testing_client.get('/characters')
    assert response.status_code == 200


def test_create_character(testing_client):
    valid_payload = {
        "alias": "Hero",
        "name": "John Doe",
        # Add other required fields for character creation
    }
    response = testing_client.post('/characters', json=valid_payload)
    assert response.status_code == 200



