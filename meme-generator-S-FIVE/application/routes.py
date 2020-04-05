from flask import Flask, request
from application import app
from flask import render_template, url_for, redirect, request
import requests
import random


@app.route('/meme', methods=['GET'])
def meme():
    url = "https://joke3.p.rapidapi.com/v1/joke"
    headers = {
        'x-rapidapi-host': "joke3.p.rapidapi.com",
        'x-rapidapi-key': "e6adf9892amsh8b30e72a8871cf6p14c10djsna97888a775b9"
    }

    response = requests.request("GET", url, headers=headers)

    return response
