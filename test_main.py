from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_post_predict_endpoint_unprocessable_entity():
    response = client.post("/api/predict/", {"file": None})
    assert response.status_code == 422

def test_post_predict_endpoint_with_string():
    response = client.post("/api/predict/", {"file": "test.jpg"})
    assert response.status_code == 422
