from flask import Flask, request
from application import app
from flask import render_template, url_for, redirect, request
import requests
import random


@app.route('/insultsentance', methods=['GET'])
def insultsentance():

	list = ['You are a','Hey you absolute','You ugly long nosed','Your cat is a','How can you 		be such a monkey brained','You had to be such a mental','Why are you always a crazy','Why 		you insolent']
	
	return list[random.randrange(7)]
