from character_api import app
import pytest

def test_dummy_wrong_path(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/wrong_path')
    assert response.status_code == 404

def test_get_characters(testing_client):
    """
    GIVEN a Flask application 
    WHEN the '/characters' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/characters')
    assert response.status_code == 200
    # Add more assertions to validate the response content, if needed

def test_create_character(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/characters' page is posted to (POST) with a valid body
    THEN check the response is valid with status code 200
    """
    # Exercise 1: Develop this test according to the definition and make it pass in the GitHub workflow
    valid_response = {"name": "Test", "alias": "Test", "level": 1, "health": 100, "strength": 10, "defense": 10, "speed": 10}
    response = testing_client.post('/characters', json=valid_response)
    assert response.status_code == 200