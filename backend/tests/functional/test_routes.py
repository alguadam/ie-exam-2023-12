from character_api import app
import pytest

# ok now we just created functional tests and we have three of them
# the first one is just sending it purposefully to the wrong path and checking if we don't get a valid path, give 404 so that's that
# then for get characters we simple send a get request at /characters which gets all the characters, and if works 200 status code so pass.
# then for create character we have a post request where again we only put the values that we need to, and then if it works 200 so pass.


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
    response = testing_client.get('/characters')
    assert response.status_code == 200


def test_create_character(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/characters' page is posted to (POST) with a valid body
    THEN check the response is valid with status code 200
    """
    # Exercise 1: Develop this test according to the definition and make it pass in the GitHub workflow
    response = testing_client.post('/characters', json={'alias': 'johnusername', 'name': 'John Doe'})
    assert response.status_code == 200

