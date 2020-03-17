from flask import Flask, request
from application import app
from flask import render_template, url_for, redirect, request
import requests
import random


@app.route('/insultword', methods=['GET'])
def insultword():
	list = ['Crazy jumping parrot','Gobermouch','Silly Monkey','Blabbermouth','Snot Nosed Donkey','Bug Eating Neanderthal','Brainless Fossil','Corona infected lunatic zombie']
	
	return list[random.randrange(7)]
