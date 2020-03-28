from flask import Flask, request
from flask import render_template, url_for, redirect, request
from application import app
import requests
import random


@app.route('/specialinsult', methods=['GET'])
def specialinsult():
	brainteaser=["A boy is walking down the road with a doctor. While the boy is the doctor’s son, the doctor isn’t the boy’s father. Then who is the doctor?","What can you hold without ever touching, or using your hands?","When you have me, you immediately feel like sharing me. But, if you do share me, you don’t have me.","What has a mouth but cannot eat, what moves but has no legs and what has a bank but cannot put money in it?","Arnold Schwarzenegger has a long one. Michael J. Fox has a short one. Madonna doesn’t use hers. Bill Clinton always uses his. The Pope never uses his. What is it?","First I threw away the outside and cooked the inside, then I ate the outside and threw away the inside, what did I eat?"]
	response1 = requests.get('http://insultservicetwo:5001/insultsentance')
	response2 = requests.get('http://insultservicethree:5002/insultword')
	response3 = response1.text+" "+response2.text
	if len(response3) >= 40:
		return "You are today's prize WINNER! as a reward you get a mind fuzzing brain teaser: " + brainteaser[random.randrange(len(brainteaser))]

	return response3


