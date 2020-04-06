import unittest
import pytest
import requests
from flask import abort, url_for
from flask_testing import TestCase

url = "http://51.132.11.147/"
url2 = "http://52.151.100.171:5000/insultsentance"
url3 = "http://52.151.100.171:5000/insultword"
url4 = "http://52.151.101.47:5000/insultjoiner"
url5 = "http://52.151.101.47:5000/frontend"
url6 = "http://52.151.101.47:5000/meme"

def test_urlhome():
    response = requests.get(url)
    assert response.status_code ==200


def test_invalidurl():
    response = requests.get(url2)
    assert response.status_code ==404

def test_getresponse():
    response = requests.get(url)
    assert isinstance(response.text,str)

def test_getrespo():
    response = requests.get(url3)
    assert response.status_code ==404

def test_getresp():
    response = requests.get(url4) 
    assert response.status_code ==404

def test_getres():
    response = requests.get(url5)
    assert response.status_code ==404
