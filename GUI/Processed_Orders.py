import sys
from PySide6 import QtWidgets as qtw
import requests

from UI.ui_Processed_orders_window import Ui_processed_order_form

class ProcessedOrders(qtw.QWidget,Ui_processed_order_form):
    """
    A widget to display processed orders and their details.

    Inherits from:
        qtw.QWidget: a Qt widget for building user interfaces.
        Ui_processed_order_form: a class generated from a Qt Designer UI file.

    Attributes:
        orders_table (QTableWidget): a table to display processed orders.
        products_table (QTableWidget): a table to display products in an order.
        total_price_box (QLineEdit): a box to display the total price of an order.

    Methods:
        load_orders(): sends a GET request to retrieve processed orders from the server.
        open_order_information(): sends a GET request to retrieve details of a selected order from the server.
        clear_products(): clears the products table and the total price box.
    """
    
    def __init__(self):
        """
        Initializes the ProcessedOrders widget.
        """
        super().__init__()
        self.setupUi(self)
        # Setting the column widths for the orders table
        self.orders_table.setColumnWidth(0,75)
        self.orders_table.setColumnWidth(1,130)
        self.orders_table.setColumnWidth(2,135)
        self.orders_table.setColumnWidth(3,235)
        self.orders_table.setColumnWidth(4,235)
        self.orders_table.setColumnWidth(5,100)
        # Load processed orders from the server and display them in the orders table
        self.load_orders()
        # Connecting the select button to the open_order_information method
        self.select_button.clicked.connect(self.open_order_information)
        # Connecting the clear button to the clear_products method
        self.clear_button.clicked.connect(self.clear_products)
    
    def load_orders(self):
        """
        Sends a GET request to the server to retrieve processed orders and displays them in the orders table.
        """
        response = requests.get("http://localhost:5000/api/order/processed")
        if response.status_code == 200:
            orders_list = response.json()
            row = 0 
            self.orders_table.setRowCount(len(orders_list))
            # print(orders_list)
            # Looping through the orders list and add each order to the orders table
            for order in orders_list:
                customer_name = qtw.QTableWidgetItem(order["customer_name"])
                customer_address = qtw.QTableWidgetItem(order["customer_address"])
                processed = qtw.QTableWidgetItem(order["processed"])
                created = qtw.QTableWidgetItem(order["created"])
                completed = qtw.QTableWidgetItem(str(order['completed']))
                order_id = qtw.QTableWidgetItem(str(order["order_id"]))
                # Setting the table items in the corresponding row and column
                self.orders_table.setItem(row, 0, order_id)
                self.orders_table.setItem(row, 1, customer_name)
                self.orders_table.setItem(row, 2, customer_address)
                self.orders_table.setItem(row, 3, processed)
                self.orders_table.setItem(row, 4, created)
                self.orders_table.setItem(row, 5, completed)
                row = row + 1
        else:
            print("Failed to retrieve products")

    def open_order_information(self):
        """
        Sends a GET request to the server to retrieve details of a selected order and displays them in the products table
        and the total price box.
        """        
        # Getting the ID of the selected order
        selected_row = self.orders_table.currentRow()
        order_id = self.orders_table.item(selected_row, 0).text()
        # print(order_id)
        # Sending a get request to the API.
        response = requests.get(f"http://localhost:5000/api/order/{order_id}")
        if response.status_code == 200:
            order_list = response.json()
            # print(order_list)
            row = 0 
            # Updating the products table and total price box
            self.products_table.setRowCount(len(order_list["products"]))
            self.total_price_box.setText(str(order_list["price"]))
            for product in order_list["products"]:
                name_item = qtw.QTableWidgetItem(product["name"])
                price_item = qtw.QTableWidgetItem(str(product["price"]))
                quantity_item = qtw.QTableWidgetItem(str(product["quantity"]))
                # Setting the table items in the corresponding row and column
                self.products_table.setItem(row, 0, name_item)
                self.products_table.setItem(row, 1, price_item)
                self.products_table.setItem(row, 2, quantity_item)
                row = row + 1                 
            print('Request was successful')
        else:
            print('Request failed with status code:', response.status_code)

    def clear_products(self):
        """
         Method to clear all input fields in the form.
        """    
        # Clearing the products table and total price box    
        self.products_table.setRowCount(0)
        self.total_price_box.clear()

if __name__ == "__main__":
   # Creating the application instance
   app = qtw.QApplication(sys.argv)
   # Creating and show the processed orders widget
   window = ProcessedOrders()
   window.show()
    # Starting the application event loop
   sys.exit(app.exec())