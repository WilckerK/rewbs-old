from flask import redirect, url_for
from flask_login import login_required, logout_user
from __main__ import app

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))
