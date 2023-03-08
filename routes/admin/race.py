from flask import Flask, jsonify, request, render_template, url_for
from flask_pymongo import PyMongo
from __main__ import admin

@admin.route('/race', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        _id = f'{db.bews.count_document({}):03d}'
        name = request.form['name']
        rosto = request.form['rosto'].replace(" ","").split(",")
        imagem = request.form['imagem']
        brasão = request.form["brasão"].replace(" ","").split(",")
        mongo.db.race.insert_one({"_id": _id, "name":name, "rosto":rosto, "imagem":imagem, "brasão":brasão})
        json = {
            "name":name,
            "rosto":rosto,
            "imagem":imagem,
            "brasao":brasão
        }
        return jsonify(json)
      
    return render_template("admin.html")
