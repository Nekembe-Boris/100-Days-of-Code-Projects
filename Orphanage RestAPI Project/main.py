import os
from pathlib import Path
import random
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
import requests
# from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
main_py_dir = Path(os.path.dirname(os.path.abspath(__file__)))
db_path = main_py_dir / 'instance' / 'records.db'

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class cameroon(db.Model):
    id: Mapped[int]= mapped_column(Integer, primary_key=True, nullable=False)
    name: Mapped[str]= mapped_column(String, nullable=False, unique=True)
    location: Mapped[str]= mapped_column(String, nullable=False, unique=False)
    phone: Mapped[str]= mapped_column(String, nullable=False, unique=False)
    email: Mapped[str]= mapped_column(String, nullable=False, unique=False)
    website: Mapped[str]= mapped_column(String, nullable=False, unique=False)

class Nigeria(db.Model):
    __tablename__ = 'nigeria'
    id: Mapped[int]= mapped_column(Integer, primary_key=True, nullable=False)
    name: Mapped[str]= mapped_column(String, nullable=False, unique=False)
    location: Mapped[str]= mapped_column(String, nullable=False, unique=False)
    phone: Mapped[str]= mapped_column(String, nullable=False, unique=False)
    email: Mapped[str]= mapped_column(String, nullable=False, unique=False)
    website: Mapped[str]= mapped_column(String, nullable=False, unique=False)

# class User(db.Model):
#     id: Mapped[int]= mapped_column(Integer, primary_key=True, nullable=False)
#     email: Mapped[str]= mapped_column(String, nullable=False, unique=True)
#     api_key: Mapped[str]= mapped_column(String, nullable=False, unique=True)


with app.app_context():
    db.create_all()


TABLE_OBJ = [Nigeria, cameroon]
TABLE_NAMES = [table.lower() for table in list(db.metadata.tables.keys())]
COL_NAMES = [col.name.lower() for col in cameroon.__table__.columns]
