from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os
from pathlib import Path

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
main_py_dir = Path(os.path.dirname(os.path.abspath(__file__)))
db_path = main_py_dir / 'movies.db'

HEADERS = {
            "accept": "application/json",
            "Authorization": "SOME_KEY"
        }

class Update(FlaskForm):
    ratx = StringField('Your Rating out of 10 eg 7.5', validators=[DataRequired()])
    rev = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')

class Add(FlaskForm):
    mov_name = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')



##CREATE DB
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


##CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

## After adding the new_movie the code needs to be commented out/deleted.
## So you are not trying to add the same movie twice. The db will reject non-unique movie titles.
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )

# with app.app_context():
#     db.session.add(new_movie)
#     db.session.add(second_movie)
#     db.session.commit()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.ranking))
    all_movies = result.scalars().all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route("/edit/<int:uid>", methods=['GET', 'POST'])
def details(uid):
    form = Update()
    result = db.session.execute(db.select(Movie).where(Movie.id==uid)).scalar()
    if form.validate_on_submit():
        result.rating = request.form['ratx']
        result.review = request.form['rev']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form, title=result.title)

@app.route("/delete/<int:uid>")
def remove(uid):
    with app.app_context():
        result = db.session.execute(db.select(Movie).where(Movie.id==uid)).scalar()
        db.session.delete(result)
        db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=['GET', 'POST'])
def add_movie():
    a_form = Add()
    if request.method == 'POST':
        if a_form.validate_on_submit():
            query = request.form['mov_name']
            url_end = f"https://api.themoviedb.org/3/search/movie?query={query}"
            response = requests.get(url=url_end, headers=HEADERS)
            all_films = response.json()['results']
            return render_template('select.html', films=all_films)
    return render_template('add.html', form=a_form)

@app.route("/new/<uid>")
def insert_db(uid):
    url_end = f'https://api.themoviedb.org/3/movie/{uid}'
    response = requests.get(url=url_end, headers=HEADERS)
    film = response.json()
    new_movie = Movie(
        title = film['title'],
        img_url = f"https://image.tmdb.org/t/p/w500{film['poster_path']}",
        year = film['release_date'][:4],
        description = film['overview']
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('details', uid=new_movie.id))






if __name__ == '__main__':
    app.run(debug=True)