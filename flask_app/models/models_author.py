# SQL Connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models  import models_book


# database name
db = "books_schema"

# Author class
class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_books = []

    # classmethod that gets all the data in authors from the database
    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors;"
        authors = []
        results = connectToMySQL(db).query_db(query)
        # "info" is a representation of author data
        for info in results:
            authors.append(cls(info))
        return authors

    # classmethod that saves the new author to the database
    @classmethod
    def save_author(cls, data):
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        result = connectToMySQL(db).query_db(query, data)
        # whenever we save; pymysql returns the id of the row of data
        return result

    # classmethod that gets the authors id that doesn't match a favorite book
    @classmethod
    def unfavorited_authors(cls, data):
        query = """SELECT * FROM authors WHERE authors.id NOT IN
                ( SELECT author_id FROM favorites WHERE book_id = %(id)s);"""
        authors = []
        results = connectToMySQL(db).query_db(query, data)
        for row in results:
            authors.append(cls(row))
        return authors

    # classmethod that adds favorite book to an author
    @classmethod
    def add_favorite(cls, data):
        query = """INSERT INTO favorites (author_id, book_id)
                VALUES (%(author_id)s, %(book_id)s);"""
        return connectToMySQL(db).query_db(query, data)

    # classmethod to get all the favorited
    @classmethod
    def get_by_id(cls, data):
        query = """SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id
                LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id = %(id)s;"""
        results = connectToMySQL(db).query_db(query, data)
        # Creates instance of author object from row one
        author = cls(results[0])
        # Goes through all the results and gets the data
        for row in results:
            # If there are no favorites
            if row['books.id'] == None:
                break
            # Common column names come back with the specific tables attached
            data = {
                "id": row['books.id'],
                "title": row['title'],
                "num_of_pages": row['num_of_pages'],
                "created_at": row['books.created_at'],
                "updated_at": row['books.updated_at']
            }
            author.favorite_books.append(models_book.Book(data))
        print(author.favorite_books)
        return author

