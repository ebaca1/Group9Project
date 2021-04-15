import os 
from flask import Flask, render_template

app = Flask(__name__)

from flask import render_template, request, redirect, url_for, session
from database import db
from models import Note as Note, User as User, Comment as Comment
from forms import RegisterForm, LoginForm, RegisterForm, LoginForm, CommentForm
import bcrypt

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SECRET_KEY'] = 'SE3155'

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
@app.route('/login')
def login():

    return render_template("login.html")
  
@app.route('/')
@app.route('/login')
def login():
#insert code
    return render_template("login.html")

@app.route('/register')
def register():
#insert code
    return render_template("register.html")

@app.route('/index')
def index():
#insert code
    return render_template("index.html")

@app.route('/new')
def new():
#insert code
    return render_template("new.html")

@app.route('/edit/eventID')
def edit():
#insert code
    return render_template("edit.html")

@app.route('/index/eventID')
def event():
#insert code
    return render_template("event.html")

@app.route('/profile/userID')
def profile():
#insert code
    return render_template("profile.html")
