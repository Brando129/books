from flask_app.config.mysqlconnection import connectToMySQL

db = "books_schema"

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
    results = connectToMySQL(db).query_db(query)
    authors = []

    # "d" is a representation of data
    for d in results:
        authors.append(cls(d))
    return authors