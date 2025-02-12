import pytest
from app import app
import requests_mock

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Test if homepage renders correctly on GET request and returns html data"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"<html" in response.data 

def test_backend_response(client):
    """Test POST request to backend with mock object"""
    with requests_mock.Mocker() as m:
        mock_response = {"status": "success", "analysis": "Test result"}
        m.post("http://localhost:5001/analyze", json=mock_response)

        response = client.post("/", data={
            "high": "100",
            "low": "50",
            "start_datetime": "2024-02-12T00:00:00Z",
            "end_datetime": "2024-02-13T00:00:00Z"
        })

        assert response.status_code == 200
        assert b"Test result" in response.data

def test_analyze_weather_backend_error(client):
    """Test for when back end is down"""
    with requests_mock.Mocker() as m:
        m.post("http://localhost:5001/analyze", status_code=500, json={"error": "Internal Server Error"})

        response = client.post("/", data={
            "high": "100",
            "low": "50",
            "start_datetime": "2024-02-12T00:00:00Z",
            "end_datetime": "2024-02-13T00:00:00Z"
        })

        assert response.status_code == 200  #make sure just error message comes up and page doesn't crash
