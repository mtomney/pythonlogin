# Imported tools and frameworks
from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps
app = Flask(__name__)

#Secret key generation and wraps function to force proper authentication prior to accessing welcome page
app.secret_key = "dont hack me"

def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You must login to gain access.')
			return redirect(url_for('login'))
	return wrap

#Decorators are being utilized to connect functions to urls
@app.route('/')
@login_required
def welcome():
	return render_template("welcome.html")

#Handling login and logout functions to allow user access to the main welcome page
@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'user' or request.form['password'] != 'secret':
			error = 'Invalid username or password, please try again.'
		else:
			session['logged_in'] = True
			flash('You have been logged in')
			return redirect(url_for('welcome'))
	return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	flash('You have been logged out')
	return redirect(url_for('login'))

#Debug mode on while in creation for ease of testing and edits
if __name__ == '__main__':
	app.run(debug=True)