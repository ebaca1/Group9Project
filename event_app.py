import os                 # os is used to get environment variables IP & PORT
   # Flask is the web app that we will customize
from flask import Flask, render_template

app = Flask(__name__)     # create an app

# @app.route is a decorator. It gives the function "index" special powers.
# In this case it makes it so anyone going to "your-url/" makes this function
# get called. What it returns is what is shown as the web page
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from database import db
from models import Note as Note
from models import User as User
from forms import RegisterForm
from flask import session
import bcrypt
from forms import LoginForm
from models import Comment as Comment
from forms import RegisterForm
from forms import LoginForm
from forms import CommentForm


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_note_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SECRET_KEY'] = 'SE3155'
#  Bind SQLAlchemy db object to this Flask app
db.init_app(app)
# Setup models
with app.app_context():
    db.create_all()   # run under the app context

# LOGIN PAGE #  
@app.route('/')
@app.route('/login')
def login():

    return render_template("login.html")
  
# REGISTRATION PAGE #
@app.route('/register')
def register():
    form = RegisterForm()

    if request.method == 'POST' and form.validate_on_submit():
        # salt and hash password
        h_password = bcrypt.hashpw(
            request.form['password'].encode('utf-8'), bcrypt.gensalt())
        # get entered user data
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        # create user model
        new_user = User(first_name, last_name, request.form['email'], h_password)
        # add user to database and commit
        db.session.add(new_user)
        db.session.commit()
        # save the user's name to the session
        session['user'] = first_name
        session['user_id'] = new_user.id  # access id value from user model of this newly added user
        # show user dashboard view
        return redirect(url_for('index'))

    # something went wrong - display register view
    return render_template('register.html', form=form)

# EVENTS (HOME) PAGE #
@app.route('/index')
def index():
    # retrieve user from database
    # check if a user is saved in session
    if session.get('user'):
        events = db.session.query(Event).filter_by(user_id=session['user_id']).all()
        return render_template("index.html", index=events, user=session['user'])
    else:
        return redirect(url_for('login'))

# CREATE PAGE #
@app.route('/new', methods=['GET', 'POST'])
def new():
    if session.get('user'):
        if request.method == 'POST':
            title = request.form['title']
            text = request.form['noteText']
            date = request.form['date']
            new_record = Event(title, text, date, session['user_id'])
            db.session.add(new_record)
            db.session.commit()

            return redirect(url_for('index'))
        else:
            return render_template('new.html', user=session['user'])
    else:
        return redirect(url_for('login'))

# INDIVIDUAL EVENT (EDIT) PAGE #
@app.route('/edit/<event_id>', methods = ['GET', 'POST'])
def edit(event_id):
    if session.get('user'):
        if request.method == 'POST':
            title = request.form['title']
            date = request.form['date']
            desc = request.form['desc']
            event = db.session.query(Event).filter_by(id=event_id).one()
            event.title = title
            event.date = date
            event.desc = desc
            db.session.add(event)
            db.session.commit()

            return redirect(url_for('index'))
        else:
            my_event = db.session.query(Event).filter_by(id=event_id).one()

            return render_template("new.html", index=my_event, user=session['user'])
    else:
        # user is not in session redirect to login
        return redirect(url_for('login'))

# INDIVIDUAL EVENT PAGE #
@app.route('/index/eventID')
def event(event_id):
#check if a user is saved in session
    if session.get('user'):
        #retrieve event from database
        a_event = db.session.query(Event).filter_by(id=event_id).one()

        return render_template("event.html", event = a_event, user = session['user'])
    else:
        return render_template("login.html")

# ACCOUNT INFO PAGE #
@app.route('/edit/list/<event_id>', methods = ['POST'])
def list(event_id):
    listed = request.form['listed']
    event = db.session.query(Event).filter_by(id=event_id).one()
    event.listed = True
    return render_template("index.html")

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

# RSVP to an event
@app.route('/events/rsvp/<event_id>', methods=['POST'])
def rsvp (event_id):
    if session.get('user'):
        # Retrieve event from database
        my_event = db.session.query(Event).filter_by(id=event_id).one()

	    # Add the event to RSVP'd events
        db.session.add(my_event)
        db.session.commit()

        # Go to events page after event has been RSVP'd
        return redirect(url_for('get_events'))
    else:
        # User is not in session, redirect to login
        return redirect(url_for('login'))



app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True) 
