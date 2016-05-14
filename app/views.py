from flask import abort, redirect, render_template, request, session, url_for, flash
from app import app
from app.models import *
from app.tasks import add

@app.route('/')
def index():
    return render_template('index.html')