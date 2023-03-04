from __main__ import app, mongo
from flask import Flask, render_template, redirect, request

@app.route('/rank/')
def rank():
    return render_template('rank.html', users=mongo.db.users)
