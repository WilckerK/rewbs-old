<<<<<<< HEAD
from __main__ import app, home
from flask import render_template

@home.route('/', methods=['GET', 'POST'])
def index():
	return render_template('home/index.html')


=======
from __main__ import app
from flask import render_template

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')


>>>>>>> ecc92ae5d56a62f0d0887d6a0e4d72296570773d
