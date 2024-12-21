"""
This module contains test cases for the Flask application in app.py.
"""
import pytest
from flask.testing import FlaskClient
from app import app
from typing import Generator


@pytest.fixture
def client()->  Generator[FlaskClient, None, None]:  # pylint: disable=redefined-outer-name
    '''
    This function will yield client
    '''
    app.testing = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    # Testing the homepage
    '''
    This function will test rendering of home page
    '''
    response = client.get('/')
    assert response.status_code == 200
    assert b'<title>Calculator</title>' in response.data
    assert b'<form' in response.data  # Check for the presence of a form
    assert b'name="operation"' in response.data  # Check for the operation input


def test_addition(client):
    '''
    This function will test addition
    '''
    response = client.post('/math', data={
        'operation': 'add',
        'num1': '10',
        'num2': '20'
    })
    assert response.status_code == 200
    assert b'the sum of 10 and 20 is 30' in response.data

def test_subtraction(client):
    # Testing the subtraction operation
    '''
    This function will test substration
    '''
    response = client.post('/math', data={
        'operation': 'subtract',
        'num1': '20',
        'num2': '10'
    })
    assert response.status_code == 200
    assert b'the difference of 20 and 10 is 10' in response.data

def test_multiplication(client):
    # Testing the multiplication operation
    '''
    This function will test Multiplication
    '''
    response = client.post('/math', data={
        'operation': 'multiply',
        'num1': '10',
        'num2': '20'
    })
    assert response.status_code == 200
    assert b'the product of 10 and 20 is 200' in response.data

def test_division(client):
    # Testing the division operation
    '''
    This function will test Division
    '''
    response = client.post('/math', data={
        'operation': 'divide',
        'num1': '20',
        'num2': '10'
    })
    assert response.status_code == 200
    assert b'the result when 20 isdividedby 10 is 2.0' in response.data




