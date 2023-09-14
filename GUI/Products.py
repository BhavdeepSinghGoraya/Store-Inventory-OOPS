import sys
from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
import requests

# Importing UI form and another window class
from UI.ui_products_window import Ui_productForm
from View_Product import ViewProducts

class ProductForm(qtw.QWidget, Ui_productForm):
    """
    Class representing the GUI form for managing products.
    """
    def __init__(self):
        """
        Constructor method for the ProductForm class.
        """        
        super().__init__()
        # Setting up the UI from the imported UI form
        self.setupUi(self)
        # Setting focus on the product name entry field
        self.name_entry.setFocus()
        # Connecting GUI buttons to the respective methods
        self.add_product_button.clicked.connect(self.add_product)
        self.delete_product_button.clicked.connect(self.delete_product)
        self.update_product_button.clicked.connect(self.update_product)
        self.view_all_products_button.clicked.connect(self.view_all_products)
        self.clear_button.clicked.connect(self.clear_inputs)

    def add_product(self):
        """
        Method to add a new product to the product list.
        """        
        url = "http://localhost:5000/api/product"
        # Getting text from respective entries.
        name = self.name_entry.text()
        price = self.price_entry.text()
        quantity = self.quantit_entry.text()
        data = { "name":name , "price": float(price), "quantity": int(quantity)}
        # Sending a POST request to the API to add a new product
        response = requests.post(url, json=data)
        if response.status_code == 200:
             print('Request was successful, The Product is added!')
        else:
             print('Request failed with status code:', response.status_code)

    def delete_product(self):
        """
        Method to delete a product from the product list.
        """
        # Getting text from name entry.
        name = self.name_entry.text()
        url = f"http://localhost:5000/api/product/{name}"
        # Sending a DELETE request to the API to delete the specified product
        response = requests.delete(url)
        if response.status_code == 200:
             print('Request was successful, The Product was Deleted!')
        else:
             print('Request failed with status code:', response.status_code)

    def update_product(self):
        """
        Method to update a product in the product list.
        """
        # Getting text from respective entries.
        name = self.name_entry.text()
        price = self.price_entry.text()
        quantity = self.quantit_entry.text()
        data = { "name":name , "price": float(price), "quantity": int(quantity)}
        url = f"http://localhost:5000/api/product/{name}"
        # Sending a PUT request to the API to update the specified product
        response = requests.put(url, json=data)
        if response.status_code == 200:
             print('Request was successful, The Product was Updated!')
        else:
             print('Request failed with status code:', response.status_code)

    @qtc.Slot()
    def view_all_products(self):
        """
        Method to open a new window displaying all the products.
        """
        # Creating a new window and displaying all products using the 'ViewProducts' class
        self.form = ViewProducts()
        self.form.show()

    def clear_inputs(self):
         """
         Method to clear all input fields in the form.
         """
         # Clearing all input fields in the form
         self.name_entry.clear()
         self.price_entry.clear()
         self.quantit_entry.clear()

if __name__ == "__main__":
   # Starting the application and displaying the product management form
   app = qtw.QApplication(sys.argv)

   window = ProductForm()
   window.show()
   sys.exit(app.exec())