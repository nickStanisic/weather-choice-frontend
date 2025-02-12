import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True 
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Test if homepage renders correctly on GET request and returns html data"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"<html" in response.data 
