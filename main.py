from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy  

app = Flask(__name__)
app.secret_key = 'hello' # define the secret key to encrypt and decrypt the session data, it should be complicated
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_BINDS'] = {
	'bugs': 'sqlite:///bugs.sqlite3'
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)

class Users(db.Model):
	id = db.Column('id', db.Integer, primary_key = True)
	name = db.Column('name', db.String(100))
	email = db.Column('email', db.String(100))


class Bugs(db.Model):
	__bind_key__='bugs'
	id = db.Column('id', db.Integer, primary_key = True)
	title = db.Column('title', db.String(100))
#	description = db.Column('description', db.text)
#	status = db.Column('status', db.Integer)
#	opened = db.Column('opened', db.datetime)
#	bugCode = db.Column('bugCode', db.real)

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/reporter')
def bugReporter():
	return render_template('reporter.html')

@app.route('/viewbugs')
def openBugs():
	return render_template('viewbugs.html')

@app.route('/users')
def userBase():
	return render_template('users.html')

if __name__ == "__main__":
	db.create_all(bind=['bugs'])
	app.run(debug = True, port = 5500)