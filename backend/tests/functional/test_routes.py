from character_api import app
import pytest

def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404


def test_get_characters(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/characters' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/characters')
    assert response.status_code == 200
    data = response.get_json()
    assert 'characters' in data
    assert isinstance(data['characters'], list)

def test_create_character(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/characters' page is posted to (POST) with a valid body
    THEN check the response is valid with status code 200
    """
    body = {
        'alias': 'test_alias',
        'name': 'test_name'
    }
    response = testing_client.post('/characters', json=body)
    assert response.status_code == 200
    data = response.get_json()
    assert 'alias' in data and data['alias'] == body['alias']
    assert 'name' in data and data['name'] == body['name']

