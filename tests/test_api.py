from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get('/health')
    assert r.status_code == 200
    assert r.json().get('status') == 'ok'

def test_score():
    payload = {"features":[0.1, -0.2, 0.3, -0.4, 0.5, -0.6]}
    r = client.post('/score', json=payload)
    assert r.status_code == 200
    body = r.json()
    assert 'score' in body and 0.0 <= body['score'] <= 1.0
