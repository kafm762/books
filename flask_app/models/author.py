from flask_app.config.mysqlconnection import connectToMySQL


class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors"
        authors = []
        results = connectToMySQL('books_schema').query_db(query)
        for row in results:
            authors.append( cls(row) )
        return authors

    @classmethod
    def save(cls, data):
        query= "INSERT INTO authors (name) VALUES (%(name)s);"
        result = connectToMySQL('books_schema').query_db(query,data)
        return result