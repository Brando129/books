# SQL Connection
from flask_app.config.mysqlconnection import connectToMySQL
# models_author Connection
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

    # method for getting all the books in the database
    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        books_list = []
        results = connectToMySQL(db).query_db(query)

        # "details" is a representation of book data
        for details in results:
            books_list.append(cls(details))
        return books_list

    # method that saves the new book to the database
    @classmethod
    def save_book(cls, data):
        query = """INSERT INTO books (title, num_of_pages)
                VALUES (%(title)s, %(num_of_pages)s);"""
        return connectToMySQL(db).query_db(query, data)