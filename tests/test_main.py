from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"data": "sea"}

def test_test2():
    response = client.get("/test/2")
    assert response.status_code == 200
    assert response.json() == {"test": "test2"}

def test_test4():
    response = client.get("/test/4")
    assert response.status_code == 200
    assert response.json() == {'10': '20'}