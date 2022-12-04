import requests

port = 5000
base = "http://localhost:" + str(port) + "/"

def test_base_template():
    url = base
    response = requests.get(url)
    assert response.status_code == 200

def test_index_template(): # ??? same route as base
    url = base
    response = requests.get(url)
    assert response.status_code == 200

def test_job_template():
    url = base + 'job/'
    response = requests.get(url)
    assert response.status_code == 200

def test_error_template():
    url = base + 'error'
    response = requests.get(url)
    assert response.status_code == 200


