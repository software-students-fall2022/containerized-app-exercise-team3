from app import configure_routes
from flask import Flask, render_template
import pytest
import pytest_flask
import pymongo
import mongomock

collection = mongomock.MongoClient().db.collection

def test_base_template():
    app = configure_routes(Flask(__name__))
    client = app.test_client()
    url = '/'
    response = client.get(url)
    assert response.status_code == 200

def test_index_template():
    app = configure_routes(Flask(__name__))
    client = app.test_client()
    url = '/index'
    response = client.get(url)
    assert response.status_code == 404

def test_job_template():
    app = configure_routes(Flask(__name__))
    client = app.test_client()
    url = '/job'
    response = client.get(url)
    assert response.status_code == 404

def test_error_template():
    app = configure_routes(Flask(__name__))
    client = app.test_client()
    url = '/error'
    response = client.get(url)
    assert response.status_code == 404

def test_base_template():
    app = configure_routes(Flask(__name__))
    client = app.test_client()
    url = '/base'
    response = client.get(url)
    assert response.status_code == 404


