from flask import render_template, session, request, url_for
from shop import app, db


@app.route("/")
def home():
    return "<h1>Welcome to flask page<h1/>"
