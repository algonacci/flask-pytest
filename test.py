from app import app
import json
import uuid


def test_index_route():
    response = app.test_client().get('/')
    res = json.loads(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert type(res) is dict
    assert res["message"] == "Success!"
    assert res["status_code"] == 200


def test_not_found_route():
    response = app.test_client().get(str(uuid.uuid4()))
    assert response.status_code == 404
    res = json.loads(response.data.decode('utf-8'))
    assert type(res) is dict
    assert res["message"] == "URL not found"
    assert res["status_code"] == 404
