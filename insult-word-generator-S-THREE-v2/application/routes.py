from flask import Flask, request
from application import app
from flask import render_template, url_for, redirect, request
import requests
import random


@app.route('/insultword', methods=['GET'])
def insultword():
	list = ['beautiful person, I also want to make you my partner in crime together forever','wonderful pretty human','mesmerising star and you have a lovely jacket','intoxicating pleasure','special unique specimen of human excellence','starry eyed huggy bear','smart intelligent fantastic person','mind bending sexy super star','rockstar']
	
	return list[random.randrange(len(list))]
