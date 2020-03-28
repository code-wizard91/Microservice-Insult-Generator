from flask import Flask, request
from application import app
from flask import render_template, url_for, redirect, request
import requests
import random


@app.route('/', methods=['GET'])
def home():
	response = requests.get('http://insultjoinerservicefour:5003/specialinsult')
	insult = response.text
	return render_template('home.html',insult = insult, title = 'Home')
