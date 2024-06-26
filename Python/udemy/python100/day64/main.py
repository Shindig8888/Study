from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()
tmdb_key = os.getenv('TMDB_KEY')
tmdb_token = os.getenv('TMDB_TOKEN')
def find_movie(url, query):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {tmdb_token}"
    }
    parameter = {
        'api_key': tmdb_key,
        'query': str(query),
    }
    response = requests.get(url, headers=headers, params=parameter)
    return response.json()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
Bootstrap5(app)

# CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite+pysqlite:///database-movie.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class MovieDatabase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=True)
    year = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(250), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=True)

# CREATE TABLE

# with app.app_context():
#     # Create the database and tables
#     db.create_all()

#     # Create a new movie entry
#     new_movie = MovieDatabase(
#         title="Phone Booth",
#         year=2002,
#         description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#         rating=7.3,
#         ranking=10,
#         review="My favourite character was the caller.",
#         img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#     )

#     # Add the new movie to the session and commit it to the database
#     db.session.add(new_movie)
#     db.session.commit()



@app.route("/")
def home():
    movies = MovieDatabase.query.order_by(MovieDatabase.rating.desc()).all()
    rank = 1
    for movie in movies:
        movie.ranking = rank
        rank += 1
    db.session.commit()
    
    return render_template("index.html", movies=movies)

@app.route("/edit/<movie_id>", methods=['GET', 'POST'])
def edit(movie_id):
    if request.method == 'POST':
        try:
            target_movie = MovieDatabase.query.filter_by(id=movie_id).first()
            new_rating = request.form['rating']
            new_review = request.form['review']
            target_movie.rating = new_rating
            target_movie.review = new_review
            db.session.commit()
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()
            return f'Error occurred: {str(e)}'
    movie = MovieDatabase.query.get(movie_id)
    return render_template('edit.html', movie=movie)

@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    try:
        target_movie = MovieDatabase.query.filter_by(id=movie_id).first()
        db.session.delete(target_movie)
        db.session.commit()
        return redirect(url_for('home'))
    except Exception as e:
        db.session.rollback()
        return f'Error occurred: {str(e)}'
    
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        url = f"https://api.themoviedb.org/3/search/movie"
        movie_title = request.form['movie-title']

        
        search_data = find_movie(url, movie_title)['results']

        for movie in search_data:
            movie['poster_path'] = "https://image.tmdb.org/t/p/w600_and_h900_bestv2"+str(movie['poster_path'])
            
        # return search_data
        return render_template('select.html', data=search_data)

    return render_template('add.html')

@app.route('/save')
def save():
    tmdb_movie_id = int(request.args.get('movie_id'))
    url = fr"https://api.themoviedb.org/3/movie/{tmdb_movie_id}"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {tmdb_token}"
    }
    parameter = {
        'api_key': tmdb_key,
    }
    data = requests.get(url, headers=headers, params=parameter).json()

    new_movie = MovieDatabase(
        title = data['title'],
        year = data['release_date'].split("-")[0],
        img_url="https://image.tmdb.org/t/p/w600_and_h900_bestv2"+str(data['poster_path']),
        description=data['overview']
    )
    db.session.add(new_movie)
    db.session.commit()

    target_movie = MovieDatabase.query.filter_by(img_url="https://image.tmdb.org/t/p/w600_and_h900_bestv2"+str(data['poster_path'])).first()
    movie_id = str(target_movie.id)

    return redirect(url_for('edit', movie_id=movie_id))
    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
