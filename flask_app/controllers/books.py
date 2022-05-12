from flask import render_template, redirect, request
from flask_app import app 
from flask_app.models.book import Book


@app.route('/books')
def book():
    books = Book.get_all()
    return render_template('books.html', all_books = books)

