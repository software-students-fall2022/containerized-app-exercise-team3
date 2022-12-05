import sys
sys.path.append('../web-app')
print(sys.path)

from app import app
from flask import Flask, render_template
import pytest
import pytest_flask
import pymongo

def test_base_template():
    # Test index route
    client = app.test_client()
    url = '/'
    response = client.get(url)
    assert response.status_code == 200

def test_job_notexist_template():
    # Test a job that does not exist
    client = app.test_client()
    url = '/job/00000000'
    response = client.get(url)
    assert response.status_code == 404
1
def test_job_template():
    # Test a job
    client = app.test_client()
    url = '/job/63850f2eb4f144d4df2fc305'
    response = client.get(url)
    assert response.status_code == 200

def test_error_template():
    # Test a route that does not exist
    client = app.test_client()
    url = '/errornotexist'
    response = client.get(url)
    assert response.status_code == 404
