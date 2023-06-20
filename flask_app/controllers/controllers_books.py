from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.models_author import Author
from flask_app.models.models_book import Book

# Route getting all the books
@app.route('/books')
def books():
    books = Book.get_all_books()
    return render_template('books.html', all_books=books)

# Route for displaying the books page
@app.route('/create/book', mehtods=['POST'])
def create_book():
    data = {
        "title": request.form['title'],
        "num_of_pages": request.form['num_of_pages']
    }
    book_id = Book.save_book(data)
    return redirect('/books')