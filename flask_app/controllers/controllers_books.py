from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.models_author import Author
from flask_app.models.models_book import Book

# Route getting all the books
@app.route('/books')
def books():
    return render_template('books.html', all_books=Book.get_all_books())