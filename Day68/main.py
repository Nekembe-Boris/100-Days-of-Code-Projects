from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os
from pathlib import Path

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

main_py_dir = Path(os.path.dirname(os.path.abspath(__file__)))
db_path = main_py_dir / 'instance' / 'users.db'

login_manager = LoginManager()
login_manager.init_app(app)

# Create a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['UPLOAD_FOLDER'] = f'{main_py_dir}/static/files'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == "POST":
        mail = request.form.get("email")
        passw = request.form.get("password")
        nom = request.form.get("name").title()

        if all([mail, passw, nom]):

            e_check = db.session.execute(db.select(User).where(User.email == mail)).scalar()
            if e_check:
                flash('You already signed up with that email. Please login instead')
                return redirect(url_for('login'))
            
            hashed_pass = generate_password_hash(passw, method='pbkdf2:sha256', salt_length=8)
            new_user = User(
                email= mail,
                password = hashed_pass,
                name = nom
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('secrets', person=nom, logged_in=current_user.is_authenticated))

    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():

    if request.method == "POST":
        mail = request.form.get("email")
        passw = request.form.get("password")

        user = db.session.execute(db.select(User).where(User.email == mail)).scalar()
        if user:
            if check_password_hash(user.password, passw):
                login_user(user)
                return redirect(url_for('secrets', person=user.name, logged_in=current_user.is_authenticated))
            
            flash('Incorrect Password. Try again')
            return render_template("login.html")

        flash('Email does not exist. Please try again')
        return render_template("login.html")
   
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", person=current_user.name, logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home', logged_in=current_user.is_authenticated))


@app.route('/download/<file>')
@login_required
def download(file):
    return send_from_directory(
        app.config['UPLOAD_FOLDER'], file, as_attachment=False
    )


if __name__ == "__main__":
    app.run(debug=True)
