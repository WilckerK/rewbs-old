from __main__ import app, mongo
from flask import Flask, render_template, redirect, request

@app.route('/bew/<string:id>')
def bews(id):
    print(id)
    user = mongo.db.users.find_one_or_404({ "discordId": id })

    return render_template('bews.html', bews=user['bews'])
