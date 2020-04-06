import unittest
import pytest
import requests
from flask import abort, url_for
from flask_testing import TestCase

url = "http://51.132.11.147/"
url2 = "http://51.132.11.147/frontend"
url3 = "http://51.132.11.147/frontend"
url4 = "http://51.132.11.147/frontend"
url5 = "http://51.132.11.147/frontend"
url6 = "http://51.132.11.147/frontend"

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
