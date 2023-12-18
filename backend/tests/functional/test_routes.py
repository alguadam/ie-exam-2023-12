from character_api import app
import pytest

def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    # Exercise 1: Develop this test according to the definition and make it pass in the GitHub workflow
    
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404
  

def test_get_characters(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/characters' page is requested (GET)
    THEN check the response is valid
    """
    # Exercise 1: Develop this test according to the definition and make it pass in the GitHub workflow
    
    # Making GET request to the characters endpoint
    response = testing_client.get('/characters')
    assert response.status_code == 200

def test_create_character(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/characters' page is posted to (POST) with a valid body
    THEN check the response is valid with status code 200
    """
    # Exercise 1: Develop this test according to the definition and make it pass in the GitHub workflow
    
    # Valid character body
    character = {'alias': 'Jane Doe', 'name': 'Jane', 'level': 1, 'health': 100.0}

    # Make a POST request to the '/characters' endpoint with the valid character body
    response = testing_client.post('/characters', json=character)

    # Check that the response status code is 200
    assert response.status_code == 200

    # Check that the response data contains the same character information that was sent in the request
    response_data = response.get_json()
    assert response_data['alias'] == character['alias']
    assert response_data['level'] == character['level']
    assert response_data['health'] == character['health']
  



    

