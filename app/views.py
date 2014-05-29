# -*- coding: utf-8 -*-

from app import app, models
from flask import render_template
from models import Post 

@app.route('/')
def index():
	some_post = Post ("Not much to say", "Terri", "Today was an uneventful day")
	some_other_post = Post ("Today was a good day", "Terri", "I dont know but today seems kinda odd. No barking from the dog.  No smog.  Had to stop at a red light.  Looking in my mirror and not a jacker in sight.")
	return render_template("index.html", posts = [some_post, some_other_post])
