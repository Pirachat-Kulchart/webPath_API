import requests


def test_api1_response():
    res = requests.get('http://127.0.0.1:5000/hello')
    assert res.status_code == 200
    data = res.json()
    assert 'api1' in data
    assert 'api2' in data
    assert 'msg' in data['api2']
