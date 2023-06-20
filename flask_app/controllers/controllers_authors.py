from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.models_author import Author

# Route for Index
@app.route('/')
def index():
    return redirect('/authors')

# Route for displaying authors page
@app.route('/authors')
def authors():
    authors = Author.get_all_authors()
    return render_template("authors.html", all_authors=authors)

# Route for creating/saving a new author
@app.route('/create/author', methods=['POST'])
def create_author():
    data = {
        "name": request.form['name']
    }
    Author.save_author(data)
    return redirect('/authors')
