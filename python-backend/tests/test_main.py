import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    """
    Tests that the health check endpoint returns a 200 status and the correct JSON body.
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "Claude Agent SDK Backend is running"}
