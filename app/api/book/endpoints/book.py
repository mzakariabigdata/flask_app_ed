from flask_restplus import Resource, Namespace
from api.restplus import api_v1

ns_books = Namespace('books', description = "Books operations")

@ns_books.route('/')
class BooksList(Resource):
    
    def get(self):
        """
        returns a list of books
        """
        return {'hello': 'world'}
    
    def post(self):
        """
        Add a new book to the list
        """
        return True, 201

    def put(self):
        """
        Update/Replace a selected book
        """
        return True, 405
    
    def patch(self):
        """
        Update/Modify a selected book
        """
        return True, 405

    def delete(self):
        """
        delete a selected book
        """
        return True, 205

@ns_books.route('/<string:title>')
class Book(Resource):
        
    def get(self):
        """
        returns a list of books
        """
        return {'hello': 'world'}
    
    def post(self):
        """
        Add a new book to the list
        """
        return True, 201

    def put(self):
        """
        Update/Replace a selected book
        """
        return True, 405
    
    def patch(self):
        """
        Update/Modify a selected book
        """
        return True, 405

    def delete(self):
        """
        delete a selected book
        """
        return True, 205


# @ns_movies.route('/')
# class HelloWorld(Resource):
    
#     def get(self):
#         return {'hello': 'world'}
    
#     def post(self):
#         return True, 201

#     def put(self):
#         return True, 405
    
#     def patch(self):
#         return True, 405

#     def delete(self):
#         return True, 205

