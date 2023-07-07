from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.models_author import Author
from flask_app.models.models_book import Book

# Get Routes
# Route for redirecting to "Index Page"
@app.route('/')
def index():
    return redirect('/authors')

# Route for rendering create/show all authors page.
@app.route('/authors')
def authors():
    authors = Author.get_all_authors()
    return render_template("authors.html", all_authors=authors)

# Route for rendering a authors page.
@app.route('/authors/<int:id>')
def show_author(id):
    data = {
        "id": id
    }
    return render_template('show_authors.html', author=Author.get_by_id(data), unfavorited_books=Book.unfavorited_books(data))


# Post Routes
# Route for creating/saving a new author
@app.route('/create/author', methods=['POST'])
def create_author():
    data = {
        "name": request.form['name']
    }
    Author.save_author(data)
    return redirect('/authors')

# Route for joining a book to a author that favorited it
@app.route('/join/book', methods=['POST'])
def join_book():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/authors/{request.form['author_id']}")