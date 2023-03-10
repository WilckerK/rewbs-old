from __main__ import app, home
from flask import render_template

@home.route('/', methods=['GET', 'POST'])
def index():
	return render_template('home/index.html')


