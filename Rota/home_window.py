from __main__ import app, mongo
from flask import Flask, render_template, redirect, request

@app.route('/')
def index():
    user = mongo.db.users.find_one_or_404({ "discordId": '1234567890' })
    return render_template('index.html', name=user['name'])