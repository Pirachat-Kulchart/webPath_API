import requests


def test_api2_response():
    res = requests.get('http://127.0.0.1:5001/world')
    assert res.status_code == 200
    data = res.json()
    assert 'msg' in data
