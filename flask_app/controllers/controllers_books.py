from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.models_book import Book
from flask_app.models.models_author import Author

# Route getting all the books
@app.route('/books')
def books():
    books = Book.get_all_books()
    return render_template('books.html', all_books=books)

# Route for displaying the books page
@app.route('/create/book', methods=['POST'])
def create_book():
    data = {
        "title": request.form['title'],
        "num_of_pages": request.form['num_of_pages']
    }
    book_id = Book.save_book(data)
    return redirect('/books')

# Route for ...
@app.route('/book/<int:id>')
def show_book(id):
    data = {
        "id": id
    }
    return render_template('show_book.html', book=Book.get_book_by_id(data), unfavorited_authors=Authors.
                          unfavorited_authors(data))