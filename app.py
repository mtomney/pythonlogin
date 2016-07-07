from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def welcome():
	return render_template("welcome.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'user' or request.form['password'] != 'secret':
			error = 'Invalid username or password, please try again.'
		else:
			return redirect(url_for('welcome'))
	return render_template('login.html', error=error)

if __name__ == '__main__':
	app.run(debug=True)