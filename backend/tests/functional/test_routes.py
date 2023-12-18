from character_api import app
import pytest

def test_dummy_wrong_path(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    #Define the endpoint
    endpoint = '/wrong_path'
    #Send a GET request to the endpoint
    response = testing_client.get(endpoint)
    #Assert that the response status code is 404 (Not Found)
    assert response.status_code == 404

def test_get_characters(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/characters' page is requested (GET)
    THEN check the response is valid
    """
    #Define the endpoint
    endpoint = '/characters'
    #Send a GET request to the endpoint
    response = testing_client.get(endpoint)
    #Assert that the response status code is 200 (OK)
    assert response.status_code == 200
    #Assert that the response data is a list (this assumes that the endpoint returns a list of characters)
    assert isinstance(response.get_json(), list)

def test_create_character(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/characters' page is posted to (POST) with a valid body
    THEN check the response is valid with status code 200
    """
    response = testing_client.post('/characters', json={'alias': 'kathe', 'name': 'papilioau'})
    assert response.status_code == 200