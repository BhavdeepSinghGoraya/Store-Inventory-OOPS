from database import db
from datetime import datetime


class Product(db.Model):
    name = db.Column(db.String, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        product_dict = {
            "name" : self.name, 
            "price" : self.price,
            "quantity" : self.quantity
        }
        return product_dict
       
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    completed = db.Column(db.Boolean, default= False)
    created = db.Column(db.DateTime)
    products = db.relationship('ProductsOrder', back_populates='order')
    processed = db.Column(db.DateTime)
    
    def to_dict(self):
        empty_list = []
        price = 0
        for p in self.products:
            product = db.session.get(Product, p.product_name)
            empty_list.append({"name":p.product_name,"price": product.price, "quantity":p.quantity})
            price += (product.price * p.quantity)
        order_dict={
            "customer_name":self.name,
            "customer_address":self.address,
            "completed": self.completed,
            "products":empty_list,
            "price":round(price,2)
            }
        return order_dict
    
    def to_dict_time(self):
        empty_list = []
        price = 0
        for p in self.products:
            product = db.session.get(Product, p.product_name)
            empty_list.append({"name":p.product_name,"price": product.price, "quantity":p.quantity})
            price += (product.price * p.quantity)
        order_dict={
            "customer_name":self.name,
            "customer_address":self.address,
            "completed": self.completed,
            "products":empty_list,
            "price":round(price,2),
            "completed":self.completed,
            "created": self.created,
            "order_id": self.id,
            "processed":self.processed
            }
        return order_dict

    def process(self):
        for p in self.products:
            product = db.session.get(Product, p.product_name)
            if p.quantity > product.quantity:
                p.quantity = product.quantity
                product.quantity = 0
                self.completed = True
                self.processed = datetime.now()
                # return f" Order contains more than available number of products"
            
            else:
                product.quantity -= p.quantity
                self.completed = True                
                # Set processed value to current date time
                self.processed = datetime.now()

class ProductsOrder(db.Model):
    # Product foreign key is name
    product_name = db.Column(db.ForeignKey("product.name"), primary_key=True)
    # Order foreign key is ID
    order_id = db.Column(db.ForeignKey("order.id"), primary_key=True)
    # This is how many items we want
    quantity = db.Column(db.Integer, nullable=False)
    # price = db.Column(db.Float , nullable= False)
    # Relationships and backreferences for SQL Alchemy
    product = db.relationship('Product')
    order = db.relationship('Order', back_populates='products')

