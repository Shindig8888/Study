from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from random import randint


'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
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
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "map_url": self.map_url,
            "img_url": self.img_url,
            "location": self.location,
            "seats": self.seats,
            "has_toilet": self.has_toilet,
            "has_wifi": self.has_wifi,
            "has_sockets": self.has_sockets,
            "can_take_calls": self.can_take_calls,
            "coffee_price": self.coffee_price
        }


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route('/random')
def random():
    random_cafe_list = db.session.query(Cafe).all()
    random_number = randint(0, len(random_cafe_list)-1)
    random_cafe = random_cafe_list[random_number]
    return jsonify(cafe=random_cafe.to_dict())

@app.route('/all')
def read_all():
    cafes = db.session.query(Cafe).all()
    return jsonify([cafe.to_dict() for cafe in cafes])


@app.route('/search')
def search():
    location = request.args.get('location')
    cafe_search_list = db.session.query(Cafe).filter_by(location=location).all()
    try:
        return jsonify([cafe.to_dict() for cafe in cafe_search_list])
    except:
        return jsonify({"error": "Sorry, we don't have a cafe at that location."})

# HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add():

    new_cafe = Cafe()
    try:
        name = request.form.get('name')
        map_url = request.form.get('map_url')
        img_url = request.form.get('img_url')
        location = request.form.get('location')
        seats = request.form.get('seats')
        has_toilet = request.form.get('has_toilet', '').lower() == 'true'  # Boolean 필드 처리
        has_wifi = request.form.get('has_wifi', '').lower() == 'true'      # Boolean 필드 처리
        has_sockets = request.form.get('has_sockets', '').lower() == 'true' # Boolean 필드 처리
        can_take_calls = request.form.get('can_take_calls', '').lower() == 'true'  # Boolean 필드 처리
        coffee_price = int(request.form.get('coffee_price')) if request.form.get('coffee_price') else None

        new_cafe = Cafe(
            name=name,
            map_url=map_url,
            img_url=img_url,
            location=location,
            seats=seats,
            has_toilet=has_toilet,
            has_wifi=has_wifi,
            has_sockets=has_sockets,
            can_take_calls=can_take_calls,
            coffee_price=coffee_price
        )

        db.session.add(new_cafe)
        db.session.commit()
        db.session.close()

        return jsonify({'message': 'Cafe added successfully'})
    except Exception as e:
        return jsonify({"error": str(e)})
    
        
    
# HTTP PUT/PATCH - Update Record
@app.route('/update_price/<cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    try:
        cafe = db.session.query(Cafe).filter_by(id=cafe_id).first()
        cafe.coffee_price =request.args.get('new_price')
        db.session.commit()
        return jsonify({'message': 'Cafe added modified'})
    except Exception as e:
        return jsonify({"error": str(e)})


# HTTP DELETE - Delete Record
@app.route('/delete_cafe/<cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    try:
        cafe = db.session.query(Cafe).filter_by(id=cafe_id).first()
        db.session.delete(cafe)
        db.session.commit()
        return jsonify({'message': 'Cafe deleted successfully'})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
