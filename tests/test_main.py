import requests

api_url="http://localhost:8000"

def test_healthcheck():
    response=requests.get(f'{api_url}/__health')
    assert response.status_code==200

class TestProduct:

    def test_get_empty_phone(self):
        responce = requests.get(f'{api_url}/v1/phones')
        assert responce.status_code == 200
        assert len(responce.json()) == 0

    def test_create_phone(self):
        body = {"model": "modelTest", "developer": "devTest"}
        responce = requests.post(f'{api_url}/v1/phones', json=body)
        assert responce.status_code == 200
        assert responce.json().get("model") == "modelTest"
        assert responce.json().get("developer") == "devTest"
        assert responce.json().get("id") == 0

    def test_get_phone_by_id(self):
        responce = requests.get(f'{api_url}/v1/phones/0')
        assert responce.status_code == 200
        assert responce.json().get("model") == "modelTest"
        assert responce.json().get("developer") == "devTest"
        assert responce.json().get("id") == 0

    def test_get_not_empty_phones(self):
        responce = requests.get(f'{api_url}/v1/phones')
        assert responce.status_code == 200
        assert len(responce.json()) == 1