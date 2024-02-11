import requests
import json
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

# intitialize flask object
app = Flask(__name__)

# intialize sqlite database and integrate it with flask
app.config['SQLACADEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# define Book class attributes and methods
class Book(db.model):
    id = db.Column(db.Integer, primary_key = True)
    book_name = db.Column(db.String(80), unique = True)
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(80))
    
    def __repr__(self) -> str:
        return f"id {self.id}, book_name {self.book_name}, " + \
                f"author {self.author} publisher {self.publisher}"

# select all books and return all of their data in a dictionary format, in short Read
@app.route('/books')
def get_books():
    books = Book.query.all()
    
    output = []
    for book in books:
        book_data = {
            'id': book.id,
            'book_name': book.book_name,
            'author': book.author,
            'publisher': book.publisher
        }
        output.append(book_data)
        
    return {'books': output}

# select one book by it's id and return the book_name, author, and publisher
@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"book_name": book.book_name, "author": book.author, "publisher": book.publisher}

# Create a book JSON object utilizing POST web requests, in short Create
@app.route('/books', methods=['POST'])
def create_book() -> str:
    book = Book()
    book.id = request.json['id']
    book.book_name = request.json['book_name']
    book.author = request.json['author']
    book.publisher = request.json['publisher']
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

# Add a book using POST, i.e. Update
@app.route('/books', methods = ['POST'])
def add_book():
    book = Book(book_name = request.json['book_name'],
                author = request.json['author'],
                publisher = request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

# Delete a book using DELETE and it's id, i.e. Delete
@app.route('/books/<id>', methods = ['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "Not Found"}
    db.session.delete(book)