from flask import Flask, request
from flask import render_template, url_for, redirect, request
from application import app
import requests
import random


@app.route('/specialinsult', methods=['GET'])
def specialinsult():
	response1 = requests.get('http://insultservicetwo:5001/insultsentance')
	response2 = requests.get('http://insultservicethree:5002/insultword')
	response3 = response1.text+" "+response2.text
	return response3


