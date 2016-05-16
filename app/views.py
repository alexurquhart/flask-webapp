from flask import abort, redirect, render_template, request, session, url_for, flash
from app import app
from app.models import db, user
from app.tasks import add

@app.route('/')
def index():
    add.delay(2,3)
    return render_template('index.html')