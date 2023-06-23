# SQL Connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import models_author


# Database name
db = 'books_schema'

# Book Class
class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # list of the authors who have favorited this book
        self.authors_who_favorited = []


    # classmethod for getting all the books in the database
    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        books_list = []
        results = connectToMySQL(db).query_db(query)

        # "details" is a representation of book data
        for details in results:
            books_list.append(cls(details))
        return books_list

    # classmethod that saves the new book to the database
    @classmethod
    def save_book(cls, data):
        query = """INSERT INTO books (title, num_of_pages)
                VALUES (%(title)s, %(num_of_pages)s);"""
        return connectToMySQL(db).query_db(query, data)

    # classmethod that gets a book with all the favorited authors
    @classmethod
    def get_book_by_id(cls, data):
        query = """SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id
                LEFT JOIN authors ON authors.id = favorites.author_id WHERE books.id = %(id)s;"""
        results = connectToMySQL(db).query_db(query, data)
        # Makes book into its own instance of the class
        book = cls(results[0])
        # Goes through all the results and gets the data
        for row in results:
            if row['authors.id'] == None:
                break
            data = {
                "id": row['authors.id'],
                "name": row['name'],
                "created_at": row['authors.created_at'],
                "updated_at": row['authors.updated_at']
            }
            book.authors_who_favorited.append(models_author.Author(data))
        return book

    # classmethod for getting books that are not favorited by an author
    @classmethod
    def unfavorited_books(cls, data):
        query = """SELECT * FROM books WHERE books.id NOT IN (SELECT book_id FROM favorites WHERE
                author_id = %(id)s);"""
        results = connectToMySQL(db).query_db(query, data)
        books = []
        for row in results:
            books.append(cls(row))
        print(books)
        return books