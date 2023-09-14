from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from flask import Flask, jsonify, render_template, request

from database import db
from models import Order, Product, ProductsOrder

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"
app.instance_path = Path(".").resolve()
db.init_app(app)


@app.route("/")
def home():
    data = Product.query.all()
    return render_template("index.html", products=data)

@app.route("/api/product", methods=["GET"])
def api_get_products():
    products = db.session.query(Product).all()
    products_list = []
    for product in products:
        product_dict = {"name": product.name, "price": product.price, "quantity": product.quantity}
        products_list.append(product_dict)
    return jsonify(products_list)

@app.route("/api/product/<string:name>", methods=["GET"])
def api_get_product(name):
    product = db.session.get(Product, name.lower())
    product_json = product.to_dict()
    return jsonify(product_json)

@app.route("/api/product/zero_quantity", methods=["GET"])
def find_out_of_stock():
    zero_quantity_products = Product.query.filter_by(quantity=0).all()
    product_list = []
    for products in zero_quantity_products:
        product = products.to_dict()
        product_list.append(product)
    return jsonify(product_list)


@app.route("/api/product", methods=["POST"])
def api_create_product():
    data = request.json
    # Check all data is provided
    for key in ("name", "price", "quantity"):
        if key not in data:
            return f"The JSON provided is invalid (missing: {key})", 400

    try:
        price = float(data["price"])
        quantity = int(data["quantity"])
        # Make sure they are positive
        if price < 0 or quantity < 0:
            raise ValueError
    except ValueError:
        return (
            "Invalid values: price must be a positive float and quantity a positive integer",
            400,
        )

    product = Product(
        name=data["name"],
        price=price,
        quantity=quantity,
    )
    db.session.add(product)
    db.session.commit()
    return "Item added to the database"

@app.route("/api/product/<string:name>", methods=["DELETE"])
def api_delete_product(name):
    product = db.session.get(Product, name.lower())
    if not product:
        return "not found", 404
    db.session.delete(product)
    db.session.commit()
    return "Item Deleted"

@app.route("/api/product/<string:name>", methods=["PUT"])
def api_put_product(name):
    data = request.json
    for key in ("price", "quantity"):
        if key not in data:
            return f"The JSON provided is invalid (missing: {key})", 400
    product = db.session.get(Product, name.lower())  
    try:
        price = float(data["price"])
        quantity = int(data["quantity"])
        # Make sure they are positive
        if type(price) is not float or type(quantity) is not int:
            raise ValueError
        if price < 0 or quantity < 0:
            raise ValueError
        product.price = price 
        product.quantity = quantity

    except ValueError:
        return (
            "Invalid values: price must be a positive float and quantity a positive integer",
            400,
        )
    db.session.commit()
    return "Item was updated in the database"

@app.route("/api/order/<int:order_id>", methods=["GET"])
def api_get_order(order_id):
    product_order= db.session.get(Order, order_id)
    product_order_json = product_order.to_dict()
    return jsonify(product_order_json)

@app.route("/api/order", methods=["POST"])
def api_create_order():
    data = request.json
    for key in ("customer_name", "customer_address","products"):
        if key not in data:
            return f"The JSON provided is invalid (missing: {key})", 400
    products = data["products"]
    for product in data["products"]:
       if not Product.query.filter(Product.name == product["name"].lower()).count():
           return f"The product doesn't exist", 400
       if product["quantity"] < 0 or type(product["quantity"]) is not int:
            return f"Invalid quantity", 400
    order = Order(name=data["customer_name"], address=data["customer_address"],created=datetime.now())
    db.session.add(order)
    db.session.commit()
    for product in products:
        quantity = int(product["quantity"])
        prod_obj = Product.query.get(product["name"].lower())
        association = ProductsOrder(product=prod_obj, order=order, quantity=quantity)
        db.session.add(association)
    db.session.commit()
    return jsonify(order.to_dict())


@app.route("/api/order/update/<int:order_id>", methods=["PUT"])
def update_order(order_id):
    order = Order.query.get(int(order_id))
    if not order:
        return f"Order with ID {order_id} not found", 404
    data = request.json
    if not data:
        return "No data provided", 400
    for product in order.products:
        db.session.delete(product)
    if "customer_address" in data:
        order.address = data["customer_address"]
    if "products" in data:
        for product in data["products"]:
            name = str(product["name"])
            price = float(product["price"])
            quantity = int(product["quantity"])
            association=ProductsOrder(product=db.session.get(Product,name),order=order,quantity=quantity)
            print(name,price,quantity)
            db.session.add(association)
    db.session.commit()
    return "Item was updated in the database"


@app.route("/api/order/<int:order_id>", methods=["DELETE"])
def api_delete_order(order_id):
    order = db.session.get(Order, order_id)
    if not order:
        return "not found", 404
    for product in order.products:
        db.session.delete(product)
    db.session.delete(order)
    db.session.commit()
    return "Item Deleted"


@app.route("/api/order/<int:order_id>", methods=["PUT"])
def api_process_order(order_id):
    data = request.json
    if "process" in data and data["process"] == True:
        order = db.session.get(Order,order_id)
        if order.completed != True:
            order.process()
            db.session.commit()
    processed_order=order.to_dict()
    return jsonify(processed_order)

@app.route("/api/order/pending", methods=["GET"])
def pending_orders():
    # Getting orders that have not been completed yet
    pending_orders = Order.query.filter_by(completed=False).order_by(Order.created)
    orders_list =[]
    for order in pending_orders:
        new_order = order.to_dict_time()
        orders_list.append(new_order)
    return jsonify(orders_list)

@app.route("/api/order/processed", methods=["GET"])
def processed_orders():
    # Getting orders that have completed
    processed_orders = Order.query.filter_by(completed=True).order_by(Order.processed).order_by(Order.created)
    orders_list =[]
    for order in processed_orders:
        new_order = order.to_dict_time()
        orders_list.append(new_order)
    return jsonify(orders_list)


@app.route("/api/order/<string:name>", methods=["GET"])
def find_order(name):
    named_orders = Order.query.filter(Order.name.like(f"%{name}%")).all()
    print(named_orders)
    order_list = []
    for order in named_orders:
        order_dict = order.to_dict_time()
        order_list.append(order_dict)
    print(order_list)
    return jsonify(order_list)

if __name__ == "__main__":
    app.run(debug=True)
