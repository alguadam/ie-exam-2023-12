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
    assert response.json == {'characters': [{'alias': 'test', 'name': 'test', 'level': 1, 'health': 100, 'strength': 10, 'defense': 10, 'speed': 10}]}

def test_create_character(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/characters' page is posted to (POST) with a valid body
    THEN check the response is valid with status code 200
    """
    response = testing_client.post('/characters', json={'alias':'test', 'name': 'test'})
    assert response.status_code == 200

    

""" # test_routes.py
def test_get_characters(testing_client):
    response = testing_client.get('/characters')
    assert response.status_code == 200

def test_create_character(testing_client):
    response = testing_client.post('/characters', json={'alias': 'test', 'name': 'test'})
    assert response.status_code == 200 """

