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
    #Define the endpoint the functional test will access
    endpoint = '/characters'

    #Define the character's body
    body = {
        'alias': 'Test Alias',
        'name': 'Test Name',
        'level': 1,
        'health': 100,
        'strength': 10,
        'defense': 10,
        'speed': 10
    }

    #Send a POST request to the endpoint
    response = testing_client.post(endpoint, json=body)

    #Assert that the response status code = 200
    assert response.status_code == 200

    #Assert that the response data is as expected
    response_data = response.get_json()
    assert response_data['alias'] == 'Test Alias'
    assert response_data['name'] == 'Test Name'
    assert response_data['level'] == 1
    assert response_data['health'] == 100
    assert response_data['strength'] == 10
    assert response_data['defense'] == 10
    assert response_data['speed'] == 10