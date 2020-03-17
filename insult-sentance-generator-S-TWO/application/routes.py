from flask import Flask, request
from application import app
from flask import render_template, url_for, redirect, request
import requests
import random


@app.route('/insultsentance', methods=['POST'])
def insultsentance():
	return "This will be a sentance"
