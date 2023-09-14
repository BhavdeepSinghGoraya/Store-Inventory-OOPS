import sys
from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
import requests

from UI.ui_Orders_window import Ui_OrdersForm
from Pending_orders import PendingOrders
from Processed_Orders import ProcessedOrders
from Find_order import FindOrder

class OrdersForm(qtw.QWidget,Ui_OrdersForm):
    """
    A class to represent the OrdersForm GUI.

    Inherits from:
        qtw.QWidget
        Ui_OrdersForm

    Methods:
        __init__(self): Constructor of the class
        loadproducts(self): loads all the products for the products table
        clear_contents(self) clears all the contents in the the different entries
        add_selected_product(self) this method adds products selected in the products table to the orders table
        create_order(self) this method creates an order 
        view_order(self) this method is used to view a order with order ID
        update_order(self) this method is used to update an existing order
        delete_order(self) this method is used to delete an order
        process_order(self) this mthod is used to process the order; it changes completed to True
        find_out_of_stock(self) this method updates the products table with alll the products with quantity zero
        open_pending_orders(self) this method opens a window whisch shows all the pending orders
        open_processed_orders(self) this method opens a window that shows all the processed orders 
        open_find_orders(self) this method opens a widow to find the products by searching the customer name.
    """    
    def __init__(self):
        """
        Initialize the OrdersForm widget and connect its buttons to the corresponding functions.
        """        
        super().__init__()
        self.setupUi(self)
        # Setting columns width for tables
        self.products_table.setColumnWidth(0,100)
        self.products_table.setColumnWidth(1,65)
        self.products_table.setColumnWidth(2,75)
        self.order_table.setColumnWidth(0,120)
        self.order_table.setColumnWidth(1,75)
        self.order_table.setColumnWidth(2,85)
        # Load products on startup
        self.loadproducts()
        # Connecting all the buttons to their respective methods
        self.select_button.clicked.connect(self.add_selected_product)
        self.create_order_button.clicked.connect(self.create_order)
        self.view_order_button.clicked.connect(self.view_order)
        self.update_order_button.clicked.connect(self.update_order)
        self.delete_order_button.clicked.connect(self.delete_order)
        self.clear_button.clicked.connect(self.clear_contents)
        self.process_order_button.clicked.connect(self.process_order)
        self.view_pending_orders.clicked.connect(self.open_pending_orders)
        self.view_processed_orders.clicked.connect(self.open_processed_orders)
        self.find_order_button.clicked.connect(self.open_find_orders)
        self.view_out_of_stock_button.clicked.connect(self.find_out_of_stock)

    def loadproducts(self):
        """
        Load the products from the API and display them in the products_table.
        """        
        response = requests.get("http://localhost:5000/api/product")
        if response.status_code == 200:
            products_list = response.json()
            row = 0 
            self.products_table.setRowCount(len(products_list))
            # Iterating over products list retrived from get request.
            for product in products_list:
                # Create table items for each order attribute
                name_item = qtw.QTableWidgetItem(product["name"])
                price_item = qtw.QTableWidgetItem(str(product["price"]))
                quantity_item = qtw.QTableWidgetItem(str(product["quantity"]))
                # Setting the table items in the corresponding row and column
                self.products_table.setItem(row, 0, name_item)
                self.products_table.setItem(row, 1, price_item)
                self.products_table.setItem(row, 2, quantity_item)
                row = row + 1
        else:
            print("Failed to retrieve products")

    def clear_contents(self):
        """
        Clear the contents of the order_table, customer_name_box, customer_address_box,
        order_id_box, order_price_box and products_table. Reload the products.
        """    
        # clearing the contents of the entries and table.    
        self.order_table.setRowCount(0)
        self.customer_address_box.clear()
        self.customer_name_box.clear()
        self.order_id_box.clear()
        self.order_price_box.clear()
        self.products_table.setRowCount(0)
        # Loading the products in the products table after clearing the table
        self.loadproducts()


    def add_selected_product(self):
        """
        Add the selected product from the products_table to the order_table.
        """    
        # Selecting the current row of the products table.    
        selected_row = self.products_table.currentRow()
        if selected_row >= 0:
            name_item = self.products_table.item(selected_row, 0)
            price_item = self.products_table.item(selected_row, 1)
            row = self.order_table.rowCount()
            self.order_table.insertRow(row)
            # Setting the table items with the selected row items in the corresponding row and column
            self.order_table.setItem(row, 0, qtw.QTableWidgetItem(name_item.text()))
            self.order_table.setItem(row, 1, qtw.QTableWidgetItem(price_item.text()))
            # self.view_order_button.clicked.connect(self.view_order)


    def create_order(self):
        """
        Create a new order on the server based on the current contents of the form.
        """ 
        # Sending a GET request to the server to retrieve a list of available products.       
        response = requests.get("http://localhost:5000/api/product")
        if response.status_code == 200:
            products = response.json()
            products_dict = {product["name"]: {"price": product["price"], "quantity": product["quantity"]} for product in products}
            customer_name = self.customer_name_box.text()
            customer_address= self.customer_address_box.text()
            ordered_products_list = []
            for row in range(self.order_table.rowCount()):
                # GEtting the contents name and quantity in the order table.
                name = self.order_table.item(row, 0).text()
                quantity = int(self.order_table.item(row, 2).text())
                # If the product is in the available products and the requested quantity is less than or equal to the
                # available quantity, add the product to the ordered products list.
                if name in products_dict and quantity <= products_dict[name]["quantity"]:
                    ordered_product = {"name": name, "price": products_dict[name]["price"], "quantity": quantity}
                    ordered_products_list.append(ordered_product)
                elif name in products_dict and quantity > products_dict[name]["quantity"]:
                    print("Invalid Quantity!")
                    return 
                else:
                    print("Invalid Product!")
            # print(ordered_products_list)
            data = { "customer_name": customer_name , "customer_address": customer_address, "products": ordered_products_list }
            url = "http://localhost:5000/api/order"
            # sending a post request to update the database
            order_response= requests.post(url, json=data)
            if order_response.status_code == 200:
                # self.products_table.setRowCount(0)
                # self.loadproducts()
                print('Request was successful, New Order is created!')
            else:
                print('Request failed with status code:', response.status_code)
        else:
            print("Request Failed!")

    def view_order(self):
        """
        Retrieve and display the details of an order from the server based on the input order ID.
        """
        # Extracting the order ID from the input form.        
        order_id = self.order_id_box.text()
        data = { "process": True}
        url = f"http://localhost:5000/api/order/{order_id}"
        response= requests.get(url,json=data)
        if response.status_code == 200:
            # If the request is successful, extract the order details from the response JSON and display them in the input form.
            order_detail = response.json()
            self.customer_name_box.setText(order_detail["customer_name"])
            self.customer_address_box.setText(order_detail["customer_address"])
            self.order_price_box.setText(str(order_detail["price"]))
            self.order_table.setRowCount(0)
            row =0
            # print(order_detail["products"])
            self.order_table.setRowCount(len(order_detail["products"]))
            for product in order_detail["products"]:
                # Creating table items for each order attribute
                name_item = qtw.QTableWidgetItem(product["name"])
                price_item = qtw.QTableWidgetItem(str(product["price"]))
                quantity_item = qtw.QTableWidgetItem(str(product["quantity"]))
                # Setting the table items in the corresponding row and column
                self.order_table.setItem(row, 0, name_item)
                self.order_table.setItem(row, 1, price_item)
                self.order_table.setItem(row, 2, quantity_item)
                row = row + 1                 
            print('Request was successful')
        else:
            print('Request failed with status code:', response.status_code)

    def update_order(self):
        """
        Sends a PUT request to update the order with the provided order_id, customer_name, customer_address, and products
        """   
        # Getting order details from the input fields     
        order_id = self.order_id_box.text()
        customer_name = self.customer_name_box.text()
        customer_address = self.customer_address_box.text()
        products = []
        row=0
        # Getting product details from the product table
        for row in range(self.order_table.rowCount()):
            name = self.order_table.item(row, 0).text()
            price = float(self.order_table.item(row, 1).text())
            quantity = int(self.order_table.item(row, 2).text())        
            product = {"name":name, "price":price, "quantity":quantity}
            products.append(product)
        # Creating data payload for PUT request
        data = {"customer_name": customer_name, "customer_address": customer_address, "products":products}
        # print(data)
        url = f"http://localhost:5000/api/order/update/{order_id}"
        response = requests.put(url,json=data)
        if response.status_code == 200:        
             print('Request was successful, the Order is updated!')
        else:
             print('Request failed with status code:', response.status_code)

    def delete_order(self):
        """
        Sends a DELETE request to delete an order with the provided order_id
        """        
        # Getting the order id from the order entry in the GUI
        order_id = self.order_id_box.text()
        url = f"http://localhost:5000/api/order/{order_id}"
        response = requests.delete(url)
        if response.status_code == 200:        
             print('Request was successful, the Order is Deleted!')
        else:
             print('Request failed with status code:', response.status_code)
    
    def process_order(self):
        """
        Sends a PUT request to update an order with the provided order_id to set 'process' field to True
        """  
        # Getting the order id from the order entry in the GUI      
        order_id = self.order_id_box.text()
        data = {"process": True}
        url = f"http://localhost:5000/api/order/{order_id}" 
        response = requests.put(url,json=data)
        if response.status_code == 200:
              # Clearing the products table and reload the data to reflect the changes in the inventory
             self.products_table.setRowCount(0)        
             self.loadproducts()
             print('Request was successful, The Order is Processed!')
        else:
             print('Request failed with status code:', response.status_code)

    def find_out_of_stock(self):
        """
        Sends a GET request to retrieve products that have zero quantity in stock and display them in the products table
        """        
        url = f"http://localhost:5000/api/product/zero_quantity"
        self.products_table.setRowCount(0)
        response = requests.get(url)
        if response.status_code == 200:
            products_list = response.json()
            row = 0 
            self.products_table.setRowCount(len(products_list))
            # print(len(products_list))
            # Populate the products table with retrieved products data
            for product in products_list:
                name_item = qtw.QTableWidgetItem(product["name"])
                price_item = qtw.QTableWidgetItem(str(product["price"]))
                quantity_item = qtw.QTableWidgetItem(str(product["quantity"]))
                self.products_table.setItem(row, 0, name_item)
                self.products_table.setItem(row, 1, price_item)
                self.products_table.setItem(row, 2, quantity_item)
                row = row + 1
        else:
            print("Failed to retrieve products")

    @qtc.Slot()
    def open_pending_orders(self):
        """
        Method to open a new window displaying all the pending orders.
        """
        # Creating a new window and displaying all products using the 'PendingOrders' class
        self.form = PendingOrders()
        self.form.show()

    @qtc.Slot()
    def open_processed_orders(self):
        """
        Method to open a new window displaying all the processed.
        """        
        # Creating a new window and displaying all products using the 'ProcessedOrders' class
        self.form = ProcessedOrders()
        self.form.show()

    @qtc.Slot()
    def open_find_orders(self):
        """
        Method to open a new window displaying find order window.
        """        
        # Creating a new window and displaying all products using the 'FindOrder' class
        self.form = FindOrder()
        self.form.show()

if __name__ == "__main__":
   # Creating the application instance
   app = qtw.QApplication(sys.argv)
    # Creating and show the orders widget
   window = OrdersForm()
   window.show()
   # Starting the application event loop
   sys.exit(app.exec())