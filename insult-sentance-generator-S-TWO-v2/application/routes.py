from flask import Flask, request
from application import app
from flask import render_template, url_for, redirect, request
import requests
import random


@app.route('/insultsentance', methods=['GET'])
def insultsentance():

	list = ['You are a really','Hey you are a','You are such a','You are surprisingly a','I do not understand how you can be such a','In life rarely we come across such a','Why are you always such a','You certainly are a','Nice to see a']
	
	return list[random.randrange(len(list))]
