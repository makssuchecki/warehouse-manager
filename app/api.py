from flask import Flask, request, jsonify
from src.storage import Storage
from src.product import Product
from src.user import User
from src.products_repository import MongoProductsRepository

app = Flask(__name__)
storage = Storage()

@app.post("/products")
def add_product():
    data = request.json
    try:
        product = Product(data["name"], data["quantity"])
        storage.add_product(product)
        return {"status": "created"}, 201
    except ValueError as e:
        return {"error": str(e)}, 400

@app.get("/products")
def get_products():
    return jsonify([
        {"name": p.name, "quantity": p.quantity} for p in storage.get_all_products()
    ])

@app.get("/products/<name>")
def get_product(name):
    product = storage.get_product_by_name(name)
    if not product:
        return {"error": "not found"}, 404
    return {"name": product.name, "quantity": product.quantity}

@app.delete("/products/<name>")
def delete_product(name):
    role = request.headers.get("Role", "user")
    user = User("test", role)

    deleted = storage.delete_product(name, user)
    if not deleted:
        return {"error": "forbidden or not found"}, 403
    return {"status": "deleted"}

@app.post("/warehouse/in")
def receive_stock():
    data = request.json
    product = storage.get_product_by_name(data["name"])
    if not product or not product.receive_stock(data["amount"]):
        return {"error": "operation failed"}, 400
    return {"status": "received"}

@app.post("/warehouse/out")
def release_stock():
    data = request.json
    product = storage.get_product_by_name(data["name"])
    if not product or not product.release_stock(data["amount"]):
        return {"error": "operation failed"}, 400
    return {"status": "released"}

@app.post("/products/save")
def save_products():
    try: 
        repo = MongoProductsRepository()
        repo.save_all(storage.get_all_products())

        return jsonify({"message": "Products saved to a database"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.post("/products/load")
def load_products():
    try: 
        repo = MongoProductsRepository()
        storage.clear()
        products = repo.load_all()
        for product in products:
            storage.add_product(product)
        return jsonify({"message": "Products loaded from a database"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500