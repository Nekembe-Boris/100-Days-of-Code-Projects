from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length

class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Log In')


app = Flask(__name__)
app.secret_key = "JinjaX"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def login():
    form_l = MyForm()
    if form_l.validate_on_submit():
        if form_l.email.data == "admin@email.com" and form_l.password.data == "12345678":
            return render_template("success.html")
        return render_template("denied.html")
    return render_template('login.html', form=form_l)

@app.route("/success")
def success():
    return render_template('success.html')

@app.route("/denied")
def failure():
    return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)
