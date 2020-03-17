from flask import Flask, request
from application import app
from flask import render_template, url_for, redirect, request
import requests
import random


@app.route('/', methods=['GET'])
def home():
	response = requests.get('https://example.api.com')
	insult = "You are a snot nosed donkey"
	return render_template('home.html',insult = insult, title = 'Home')
