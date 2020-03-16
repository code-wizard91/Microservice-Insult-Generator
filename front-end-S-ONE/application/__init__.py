from flask import Flask, request
import requests
import os

app = Flask(__name__)

from application import routes
