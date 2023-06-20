# SQL Connection
from flask_app.config.mysqlconnection import connectToMySQL

# database name
db = "books_schema"

# Author class
class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # gets all the data in authors from the database
    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors;"
        authors_list = []
        results = connectToMySQL(db).query_db(query)

        # "d" is a representation of author data
        for d in results:
            authors_list.append(cls(d))
        return authors_list