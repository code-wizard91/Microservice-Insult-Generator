from flask import Flask, request
from application import app
from flask import render_template, url_for, redirect, request,
import requests
import random


@app.route('/meme', methods=['POST'])
def meme():
	return "This will be a meme"
