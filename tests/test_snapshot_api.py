from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_root():
    response = client.get('/')
    assert response.status_code == 200


def test_snapshot():
    response = client.get('/snapshot/current')
    assert response.status_code == 200


def test_health():
    response = client.get('/health')
    assert response.status_code == 200
