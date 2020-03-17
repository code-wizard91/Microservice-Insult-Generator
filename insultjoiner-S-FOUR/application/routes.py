from flask import Flask, request
from flask import render_template, url_for, redirect, request
from application import app
import requests
import random


@app.route('/specialinsult', methods=['GET'])
def specialinsult():
	api = 'http://localhost:5001'
	response = requests.get(api + '/insultsentance')
	return response.text
