from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy 
import string
import random
import textwrap

app = Flask(__name__)
app.secret_key = 'hello' # define the secret key to encrypt and decrypt the session data, it should be complicated
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_BINDS'] = {
	'bugs': 'sqlite:///bugs.sqlite3'
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)

class Users(db.Model):
	_id = db.Column('id', db.Integer, primary_key = True)
	name = db.Column('name', db.String(100))
	#userid = db.Column('userid', db.String(100))

	def __init__(self, name):
		self.name = name
		#self.userid = userid

class Bugs(db.Model):
	__bind_key__='bugs'
	_id = db.Column('id', db.Integer, primary_key = True)
	title = db.Column('title', db.String(100))
	opened = db.Column('opened', db.String(100))
	status = db.Column('status', db.Integer)
	details = db.Column('details', db.Text(5000))
	user = db.Column('user', db.String(100))

	def __init__(self, title, opened, status, details, user):
		self.title = title
		self.opened = opened
		self.status = status
		self.details = details
		self.user = user

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/reporter', methods = ['GET', 'POST'])
def bugReporter():
	if request.method == 'POST':

		title = request.form['bugTitle'] or None
		details = request.form['bugDetails'] or None
		user = request.form['name'] or None

		if title == None:
			flash('Bug Must Be Given A Title!', 'info')
			return render_template('reporter.html')

		if details == None:
			flash('A Bug Description Must Also Be Provided!', 'info')
			return render_template('reporter.html')

		session["bugTitle"] = title
		session['bugDetails'] = details

		bugquery = Bugs.query.filter_by(title=title).first()
		query = Users.query.filter_by(name=user).first()

		if bugquery:
			flash('Bug Title Already Exists!', 'warning')
			return render_template('reporter.html', values = user)

		else:
			if query or user == None:
				status = 1 # 1 == Open
				opened = datetime.now()
				bug = Bugs(title, opened, status, details, user)
				db.session.add(bug)
				db.session.commit()

				flash('New Bug {} Added to Database'.format(title))
				return redirect(url_for('openBugs'))

			else:
				flash('User does not exist!')
				return render_template('reporter.html')

	return render_template('reporter.html')

@app.route('/updatebug', methods = ['GET', 'POST'])
def updateBug():
	if request.method == 'POST':

		title = request.form['bugTitle'] or None
		status = request.form['status'] or None
		user = request.form['name']

		if title == None:
			flash('You Must Input A Bug Title To Update!', 'info')
			return render_template('updatebug.html')
		
		session['bugTitle'] = title

		bugquery = Bugs.query.filter_by(title=title).first()

		if user:
			query = Users.query.filter_by(name=user).first()

			if not query:
				flash('User {} Does Not Exist, Create User First!'.format(user), 'info')
				return render_template('users.html', user=user)

		if bugquery:
			if status:					
				if status == 'Open':
					bugquery.status = 1

				elif status == 'Close':
					bugquery.status = 0
					db.session.commit()
					flash('{} Has Been Closed'.format(title))
					return render_template('viewbugsclosed.html', values = Bugs.query.all())

				else:
					flash("Incorrect Syntax, type 'Open' or 'Close' to change the bug status")
					return render_template('updatebug.html', title=title)

			elif not status:
				if bugquery.status == 0:
					flash("{} is closed, you must reopen the bug report to edit!".format(title))
					return render_template('updatebug.html', title=title)

			if user:
				query
				bugquery.user = user

			db.session.commit()
			flash('{} Has Been Updated'.format(title))
			return redirect(url_for('openBugs'))


		else:
			flash('Bug Does Not Yet Exist!', 'warning')
			return render_template('reporter.html', title = title)

	return render_template('updatebug.html')

@app.route('/viewbugs', methods = ['GET', 'POST'])
def openBugs():
	if request.method == 'POST':
		title = request.form['bugTitle'] or None

		if title == None:
			flash('You Must Input A Bug Title!', 'info')
			return render_template('viewbugs.html', values = Bugs.query.filter_by(status=1).all())

		bugquery = Bugs.query.filter_by(title=title).first()

		if bugquery:
			return render_template('viewbugs.html', description = bugquery, values = Bugs.query.filter_by(status=1).all())
		else:
			flash('Bug Does Not Yet Exist!', 'warning')
			return render_template('reporter.html', title = title)
	else:
		return render_template('viewbugs.html',  values = Bugs.query.filter_by(status=1).all())

#@app.route('/viewbugsdetails', methods = ['GET'])
#def openBugsDetails():
#	return render_template('viewbugsdetails.html',  values = Bugs.query.filter_by(status=1).all())

@app.route('/viewbugsclosed', methods = ['GET'])
def closedBugs():
	return render_template('viewbugsclosed.html',  values = Bugs.query.filter_by(status=0).all())

@app.route('/users', methods = ['GET', 'POST'])
def userBase():
	if request.method == 'POST':
		
		user = request.form['name'] or None
		session["user"] = user

		query = Users.query.filter_by(name=user).first()

		if query:
			flash('User Already Exists!', 'warning')
			return render_template('users.html')

		if user:
			#randomid = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))
			usr = Users(user)
			db.session.add(usr)
			db.session.commit()
			flash('User Added to Database')
			return render_template('viewusers.html', values = Users.query.all())
		
		elif not user:
			flash('You Must Include A Username')
			return render_template('users.html')

	else:
		return render_template('users.html')

@app.route('/updateuser', methods = ['GET', 'POST'])
def updateUser():
	if request.method == 'POST':
		user = request.form['name'] or None
		newuser = request.form['newname'] or None

		if user == None:
			flash('A Username Must Be Provided', 'info')
			return render_template('updateuser.html')

		if newuser == None:
			flash('A New Username Must Be Provided', 'info')
			return render_template('updateuser.html')			

		query = Users.query.filter_by(name=user).first()
		newquery = Users.query.filter_by(name=newuser).first()

		if query:
			if newquery:
				flash('Username {} already in use!'.format(newuser), 'info')
				return	render_template('updateuser.html')
			else:
				query.name = newuser
				bugquery = Bugs.query.filter_by(user=user).all()
				for item in bugquery:
					item.user = newuser
				db.session.commit()
				flash('User Details Updated!', 'info')
				return	render_template('viewusers.html', values = Users.query.all())
		
		else:
			flash('User {} not found in database'.format(user), 'info')
			return render_template('updateuser.html')

	else:
		return render_template('updateuser.html')


@app.route('/viewusers', methods = ['GET', 'POST'])
def viewUsers():
		return render_template('viewusers.html', values = Users.query.all())

if __name__ == "__main__":
	db.create_all()
	app.run(debug = True, port = 5500)