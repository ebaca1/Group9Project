# IMPORTS #
import os 
from flask import Flask, render_template

app = Flask(__name__)

from flask import render_template, request, redirect, url_for, session
from database import db
from models import Event as Event, User as User, Rsvp as Rsvp
from forms import RegisterForm, LoginForm
import bcrypt

# SETUP #
#Pulled this directly from flask_app tutorial. Edit/delete what needs to be fixed
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SECRET_KEY'] = 'SE3155'

db.init_app(app)

with app.app_context():
    db.create_all()

# LOGIN PAGE #  
@app.route('/')
@app.route('/login')
def login():

    return render_template("login.html")
  
# REGISTRATION PAGE #
@app.route('/register')
def register():
#insert code
    return render_template("register.html")

# EVENTS (HOME) PAGE #
@app.route('/index')
def index():
#insert code
    return render_template("index.html")

# CREATE PAGE #
@app.route('/new')
def new():
#insert code
    return render_template("new.html")

# INDIVIDUAL EVENT (EDIT) PAGE #
@app.route('/edit/eventID')
def edit():
#insert code
    return render_template("edit.html")

# INDIVIDUAL EVENT PAGE #
@app.route('/index/eventID')
def event():
#insert code
    return render_template("event.html")

# ACCOUNT INFO PAGE #
@app.route('/profile/userID')
def profile():
#insert code
    return render_template("profile.html")

# Delete event
@app.route('/events/delete/<event_id>', methods=['POST'])
def delete_event(event_id):
    if session.get('user'):
        # Retrieve event from database
        my_event = db.session.query(Event).filter_by(id=event_id).one()

	# Delete the event
        db.session.delete(my_event)
        db.session.commit()

    # Go to events page after event is deleted
	return redirect(url_for('get_events'))
    else:
        # User is not in session, redirect to login
        return redirect(url_for('login'))

app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True) 
