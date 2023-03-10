<<<<<<< HEAD
from __main__ import app, db
=======
from __main__ import api, db
>>>>>>> ecc92ae5d56a62f0d0887d6a0e4d72296570773d
from flask import render_template

@app.route('/rank')
def rank():
<<<<<<< HEAD
	return render_template('rank.html', users=db.users)
=======
    return render_template('rank.html', users=db.users)
>>>>>>> ecc92ae5d56a62f0d0887d6a0e4d72296570773d
