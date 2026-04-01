from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Database (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///campus_exchange.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# -------------------- MODELS --------------------

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    category = db.Column(db.String(100))
    price = db.Column(db.Integer)
    condition = db.Column(db.String(50))
    seller = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    postedDate = db.Column(db.String(50))
    description = db.Column(db.Text)
    image = db.Column(db.String(255))

# Create DB
with app.app_context():
    db.create_all()

# -------------------- ROUTES --------------------

@app.route('/')
def home():
    return {"message": "Backend running 🚀"}

# ✅ Signup
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json

    if User.query.filter_by(email=data['email']).first():
        return {"error": "User already exists"}

    user = User(email=data['email'], password=data['password'])
    db.session.add(user)
    db.session.commit()

    return {"message": "Signup successful"}

# ✅ Login
@app.route('/login', methods=['POST'])
def login():
    data = request.json

    user = User.query.filter_by(
        email=data['email'],
        password=data['password']
    ).first()

    if not user:
        return {"error": "Invalid credentials"}

    return {"message": "Login successful"}

# ✅ Add Item
@app.route('/add_item', methods=['POST'])
def add_item():
    data = request.json

    item = Item(
        name=data.get('name'),
        category=data.get('category'),
        price=data.get('price'),
        condition=data.get('condition'),
        seller=data.get('seller'),
        phone=data.get('phone'),
        postedDate=str(datetime.now().date()),
        description=data.get('description'),
        image=data.get('image')
    )

    db.session.add(item)
    db.session.commit()

    return {"message": "Item added successfully"}

# ✅ Get all items
@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()

    result = []
    for item in items:
        result.append({
            "id": item.id,
            "name": item.name,
            "category": item.category,
            "price": item.price,
            "condition": item.condition,
            "seller": item.seller,
            "phone": item.phone,
            "postedDate": item.postedDate,
            "description": item.description,
            "image": item.image
        })

    return jsonify(result)

# ✅ Get single item
@app.route('/item/<int:id>', methods=['GET'])
def get_item(id):
    item = Item.query.get(id)

    if not item:
        return {"error": "Item not found"}

    return {
        "id": item.id,
        "name": item.name,
        "category": item.category,
        "price": item.price,
        "condition": item.condition,
        "seller": item.seller,
        "phone": item.phone,
        "postedDate": item.postedDate,
        "description": item.description,
        "image": item.image
    }

# ✅ Delete item
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.get(id)

    if not item:
        return {"error": "Item not found"}

    db.session.delete(item)
    db.session.commit()

    return {"message": "Item deleted"}

# -------------------- RUN --------------------

if __name__ == '__main__':
    app.run(debug=True)