import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page_status(client):
    response = client.get('/')
    assert response.status_code == 200

def test_home_page_content_title(client):
    response = client.get('/')
    content = response.data.decode('utf-8')
    assert "Bienvenido a mi Proyecto" in content

def test_home_page_content_name(client):
    response = client.get('/')
    content = response.data.decode('utf-8')
    assert "Prueba de Daniela Alexandra Cárdenas Maldonado" in content