from app import create_app

flask_app = create_app('tests/functional/config.test.yaml')

def test_brew_history():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/brew_history' page is requested (GET)
    THEN check that the response is valid
    """

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/brew_history')
        assert response.status_code == 200
        assert b"<title>PicoBrew Server</title>" in response.data


def test_ferm_history():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/ferm_history' page is requested (GET)
    THEN check that the response is valid
    """

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/ferm_history')
        assert response.status_code == 200
        assert b"<title>PicoBrew Server</title>" in response.data


def test_still_history():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/still_history' page is requested (GET)
    THEN check that the response is valid
    """

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/still_history')
        assert response.status_code == 200
        assert b"<title>PicoBrew Server</title>" in response.data


def test_ispindel_history():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/iSpindel_history' page is requested (GET)
    THEN check that the response is valid
    """

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/iSpindel_history')
        assert response.status_code == 200
        assert b"<title>PicoBrew Server</title>" in response.data


def test_tilt_history():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/tilt_history' page is requested (GET)
    THEN check that the response is valid
    """

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/tilt_history')
        assert response.status_code == 200
        assert b"<title>PicoBrew Server</title>" in response.data