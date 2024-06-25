from flask import Flask, render_template, request, redirect, url_for
from pprint import pprint
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite+pysqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class BookShelf(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


@app.route('/')
def home():
    books = BookShelf.query.all()
    all_books = []
    for book in books:
        book_data = {
            "id": book.id,
            "title" : book.title,
            "author" : book.author,
            "rating" : str(book.rating),
        }
        all_books.append(book_data)
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        try:
            book_name = request.form['book'].title()
            author = request.form['author'].title()
            rating = request.form['rating']
            new_book = BookShelf(title=book_name, author=author, rating=rating)
            db.session.add(new_book)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return f'Error occurred: {str(e)}'
        return redirect(url_for('home'))

    return render_template('add.html')

@app.route("/edit_rating/<book_id>", methods=['GET', 'POST'])
def edit_rating(book_id):
    book_finder = BookShelf.query.filter_by(id=book_id).first()
    if request.method == 'POST':
        new_rating = float(request.form['rating'])
        book_finder.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))
    else:
        if book_finder:
            return render_template("edit-rating.html", book_info=book_finder)
        else:
            return 'User not found'

@app.route("/delete/<book_id>")  
def delete_book(book_id):
    book_finder = BookShelf.query.filter_by(id=book_id).first()
    if book_finder:
        db.session.delete(book_finder)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return 'User not found.'  





if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # 데이터베이스 파일 및 테이블 생성
    app.run(debug=True)

