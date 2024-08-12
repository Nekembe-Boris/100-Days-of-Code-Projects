from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random
import os
from pathlib import Path



app = Flask(__name__)
main_py_dir = Path(os.path.dirname(os.path.abspath(__file__)))
db_path = main_py_dir / 'instance' / 'cafes.db'

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()

def pattern(data):
    cafe={
        "id": data.id,
        "name": data.name,
        "map_url": data.map_url,
        "img_url": data.img_url,
        "location": data.location,
        "seats": data.seats,
        "has_toilet": data.has_toilet,
        "has_wifi": data.has_wifi,
        "has_sockets": data.has_sockets,
        "can_take_calls": data.can_take_calls,
        "coffee_price": data.coffee_price
    }

    return cafe



@app.route("/")
def home():
    return render_template("index.html")

@app.route('/random')
def random_orp():
    with app.app_context():
        result = db.session.execute(db.select(Cafe))
        random_cafe = random.choice(result.scalars().all())
    return jsonify(pattern(random_cafe))

@app.route("/all")
def all_cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    cafes = result.scalars().all()
    return jsonify([pattern(cafe) for cafe in cafes])

@app.route("/search")
def location():
    loc = request.args.get('loc').title()
    result = db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalars().all()
    if result:
        return jsonify([pattern(cafe) for  cafe in result])
    
    return jsonify(
        {
            'Error' : f"No records of any cafe @{loc}"
        }
    )


@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.get_or_404(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        ## Just add the code after the jsonify method. 200 = Ok
        return jsonify(response={"success": "Successfully updated the price."}), 200
    
    return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe = db.get_or_404(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

    return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403



if __name__ == '__main__':
    app.run(debug=True)
