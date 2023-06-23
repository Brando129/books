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
@app.route('/books/<int:id>')
def show_book(id):
    data = {
        "id": id
    }
    return render_template('show_books.html', book=Book.get_book_by_id(data), unfavorited_authors=Author.
    unfavorited_authors(data))

# Route for ...
@app.route('/join/author', methods=['POST'])
def join_author():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect (f"/book/{request.form['book_id']}")