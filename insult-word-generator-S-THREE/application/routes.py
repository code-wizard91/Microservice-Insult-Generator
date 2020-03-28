from flask import Flask, request
from application import app
from flask import render_template, url_for, redirect, request
import requests
import random


@app.route('/insultword', methods=['GET'])
def insultword():
	list = ['crazy jumping parrot', 'rubbish talking willy fizzle', 'silly Monkey', 'wide eyed corona infested bat', 'Snot Nosed Donkey brain', 'Bug Eating Neanderthal', 'Brainless Fossil', 'Corona infected lunatic zombie', 'insane baby faced snot nosed microphallus', 'empty brained dumbfounded ant eater']
	return list[random.randrange(len(list))]
