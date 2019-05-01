"""Main tests module."""
import main


def test_home():
    """Test Home page"""
    main.APP.testing = True
    client = main.APP.test_client()

    req = client.get("/")
    assert req.status_code == 200
