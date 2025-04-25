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

def data_pattern(data, nation):
    """
    :param data - The query recieved from database,
    :param code - Determines if tp use state or region

    Give the structure of json returned
    """

    d_json = {
        'uid' : data.id,
        'name' : data.name,
        'nation' : nation.__name__.upper(),
        'location' : data.location,
        'contact' : {
            'phone' : data.phone,
            'email' : data.email
        },
        'website' : data.website
    }

    return d_json

def resquest_code(err:int):
    """
    Returns error code
    """
    url_end = 'https://status.js.org/codes.json'

    data= requests.get(url=url_end, timeout=10).json()

    err_details = {

        f"Error {err}" : data[str(err)]['description']
    }
    return err_details

@app.route('/')
def home():
    return render_template('register.html')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     mail = request.form.get('email')

#     if request.method == 'POST':
#         if mail:
#             a_key = ''.join(random.choices(string.ascii_letters, k=15))

#             new = User(
#                 email = mail,
#                 api_key = a_key
#             )
#             db.session.add(new)
#             db.session.commit()
#             return render_template('register.html', key=a_key)
    
#     return render_template('register.html')


@app.route('/random')
def random_orp():
    """
    GET random orphanage data
    """
    country = random.choice(TABLE_OBJ)
    result = db.session.execute(db.select(country)).scalars().all()
    return jsonify([data_pattern(random.choice(result), country)])


@app.route('/all')
def all_orph():
    """
    Request orphanage data in stated nation
    """
    nation = request.args.get('nation')
    if nation not in TABLE_NAMES:
        return jsonify(
            no_info = {
            "error" : f"Sorry no Orpahange record from {nation}"
            }
        )

    for obj in TABLE_OBJ:
        if obj.__name__.lower() == nation.lower():
            result = db.session.execute(db.select(obj)).scalars().all()

    return jsonify([data_pattern(orph, obj) for orph in result])
