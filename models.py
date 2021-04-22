# Flask database models file

# imports
from database import db
import datetime
import sqlite3
from sqlite3 import Error

class Event(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    #listed = db.Column(("listed"), db.Boolean)
    title = db.Column("title",db.String(200))
    text = db.Column("text", db.String(100))
    date = db.Column("date", db.String(50))
    #rating = db.Column("rating", db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


    def __init__(self, title, text, date, user_id):
        #add rating after "text" above if need be. Add listed after self
        #self.listed = listed
        self.title = title
        self.text = text
        self.date = date
        #self.rating = rating
        self.user_id = user_id

class User(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    first_name = db.Column("first_name", db.String(100))
    last_name = db.Column("last_name", db.String(100))
    email = db.Column("email", db.String(100))
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    events = db.relationship("Event", backref="user", lazy=True)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.registered_on = datetime.date.today()

# Model for RSVP
class Rsvp(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey("event.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)



    def __init__(self, user_id, event_id):
        self.event_id = event_id
        self.user_id = user_id

