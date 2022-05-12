from flask import render_template, redirect, request
from flask_app import app 
from flask_app.models.author import Author

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def author():
    authors = Author.get_all()
    return render_template("authors.html", all_authors = authors)

@app.route('/create/author',methods=['POST'])
def add_author():
    Author.save(request.form)
    return redirect('/authors')