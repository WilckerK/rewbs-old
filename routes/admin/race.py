from flask import Flask, jsonify, request, render_template, url_for
from flask_pymongo import PyMongo
from __main__ import admin, db

@admin.route('/race', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        _id = f'{db.bews.count_documents({}):03d}'
        name = request.form['name']
        face = request.form['rosto'].replace(" ","").split(",")
        image = request.form['imagem']
        brasão = request.form["brasão"].replace(" ","").split(",")
        json = jsonify({_id, name, face, image,brasão})
        db.race.insert_one(json)
        return json
      
    return render_template("race.html")
