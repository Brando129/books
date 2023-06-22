from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.models_author import Author
from flask_app.models.models_book import Book # Find out why this isnt being accessed


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

# Route for getting one author
@app.route('/author/<int:id>')
def show_author(id):
    data = {
        "id": id
    }
    return render_template('show_authors.html', author=Author.get_by_id(data), unfavorited_books=Book.
    unfavorited_books(data))