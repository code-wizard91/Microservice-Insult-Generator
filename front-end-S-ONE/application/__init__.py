from flask import Flask, request
#from flask_sqlalchemy import SQLAlchemy
import requests
import os

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))
#app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
#db = SQLAlchemy(app)

from application import routes
