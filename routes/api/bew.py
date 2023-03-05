from __main__ import api, db
from flask import render_template

@api.route('/bew/<string:id>')
def bews(id):
    print(id)
    user = db.users.find_one_or_404({ "discordId": id })

    return render_template('bews.html', bews=user['bews'])
