# from flask import abort, redirect, render_template, request, session, url_for, flash
from app import app
from app.models import *

@app.route('/')
def index():
    return "<body>Hello, World!</body>"