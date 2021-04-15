import os 
from flask import Flask, render_template

app = Flask(__name__)

from flask import render_template, request, redirect, url_for, session
from database import db
from models import Note as Note, User as User, Comment as Comment
from forms import RegisterForm, LoginForm, RegisterForm, LoginForm, CommentForm
import bcrypt
