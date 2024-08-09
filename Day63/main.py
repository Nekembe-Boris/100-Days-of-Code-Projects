import os
from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


app = Flask(__name__)

main_py_dir = Path(os.path.dirname(os.path.abspath(__file__)))
db_path = main_py_dir / 'project.db'

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
db.init_app(app)

class D_Model(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[str] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    result = db.session.execute(db.select(D_Model).order_by(D_Model.title))
    all_books = result.scalars()
    return render_template('index.html', books=all_books)


@app.route('/add', methods=['GET', 'POST'])
def add():

    if request.method == 'POST':
        with app.app_context():
            new_book = D_Model(
                title = request.form['title'],
                author = request.form['author'],
                rating = float(request.form['rating'])
            )
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

 
@app.route('/edit/<uid>', methods=['GET', 'POST'])
def change(uid):
    with app.app_context():
        r_book = db.session.execute(db.select(D_Model).where(D_Model.id==uid)).scalar()
        if request.method == 'POST':
            r_book.rating = request.form['rating']
            db.session.commit()
            return redirect(url_for('home'))

    return render_template('rating.html', book=r_book)

@app.route('/delete/<int:uid>', methods=['GET', 'POST'])
def delete(uid):
    with app.app_context():
        row = db.session.execute(db.select(D_Model).where(D_Model.id==uid)).scalar()
        db.session.delete(row)
        db.session.commit()
        return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)

