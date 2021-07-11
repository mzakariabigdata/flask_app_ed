import os, json
import tempfile
import requests
import pytest

from app import create_app
from dba.models import db


# from dba.db import init_db


@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app(config_env="testing")

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

    os.close(db_fd)
    os.unlink(db_path)

def test_root_front(client):
    """Start with a blank database."""

    rv = client.get('/')
    assert b'Hello, Zakaria MORCHID!' in rv.data

def test_empty_db(client):
    """Start with a blank database."""

    rv = client.get('/api/v1/books/')

    assert 404 == rv.status_code

def test_post_book(client):
    # with client.test_client() as c:
    book = {'title': 'unittest', 'author': 'test hello word'}
    url = 'http://127.0.0.1:5000/api/v1/books/'
    headers = {'Content-Type': 'application/json', 'accept': 'application/json'}
    response = requests.post(url, json=book, headers=headers)
    # rv = client.post(url, data=json.dumps(book), headers=headers)
    # resp = client.get("/api/v1/books/unittest")
    # json_data = resp.data
    # assert 201 == rv.status_code
    assert 201 == response.status_code
    # assert book == resp.json()

def test_post_book_response(client):
    url = 'http://127.0.0.1:5000/api/v1/books/unittest'
    book = {'title': 'unittest', 'author': 'test hello word'}
    # rv = client.post(url, data=json.dumps(book), headers=headers)
    # resp = client.get("/api/v1/books/unittest")
    resp = requests.get(url)

    # json_data = resp.data
    # assert 201 == rv.status_code
    # assert 201 == response.status_code
    assert 200 == resp.status_code
