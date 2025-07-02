from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_search_music():
    response = client.get("/music/search?query=test")
    assert response.status_code == 200
    assert "results" in response.json()
