from flask import render_template, redirect, request
from flask_app import app

# Route for Index
@app.route('/')
def index():
    return redirect('/authors')

# Route for displaying authors page
# @app.route('/authors')
# def authors():
