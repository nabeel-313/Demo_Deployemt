import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    # Testing the homepage
    response = client.get('/')
    assert response.status_code == 200
    assert b'<title>Calculator</title>' in response.data
    assert b'<form' in response.data  # Check for the presence of a form
    assert b'name="operation"' in response.data  # Check for the operation input


def test_addition(client):
    # Testing the addition operation
    response = client.post('/math', data={
        'operation': 'add',
        'num1': '10',
        'num2': '20'
    })
    assert response.status_code == 200
    assert b'the sum of 10 and 20 is 30' in response.data

def test_subtraction(client):
    # Testing the subtraction operation
    response = client.post('/math', data={
        'operation': 'subtract',
        'num1': '20',
        'num2': '10'
    })
    assert response.status_code == 200
    assert b'the difference of 20 and 10 is 10' in response.data

def test_multiplication(client):
    # Testing the multiplication operation
    response = client.post('/math', data={
        'operation': 'multiply',
        'num1': '10',
        'num2': '20'
    })
    assert response.status_code == 200
    assert b'the product of 10 and 20 is 200' in response.data

def test_division(client):
    # Testing the division operation
    response = client.post('/math', data={
        'operation': 'divide',
        'num1': '20',
        'num2': '10'
    })
    assert response.status_code == 200
    assert b'the quotient when 20 is divided by 10 is 2.0' in response.data

