import sys
from PySide6 import QtWidgets as qtw
import requests

# Importing the UI file generated from Qt Designer
from UI.ui_Pending_orders_window import Ui_pending_order_form

class PendingOrders(qtw.QWidget,Ui_pending_order_form):
    """
    Class for the Pending Orders window.

    Inherits from QWidget and Ui_pending_order_form.
    """    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Setting column widths for the pending orders table
        self.pending_orders_table.setColumnWidth(0,75)
        self.pending_orders_table.setColumnWidth(1,130)
        self.pending_orders_table.setColumnWidth(2,130)
        self.pending_orders_table.setColumnWidth(3,235)
        self.pending_orders_table.setColumnWidth(4,100)
        # Load pending orders and connect button signals
        self.load_orders()
        # Connecting GUI buttons to the respective methods
        self.select_button.clicked.connect(self.open_order_information)
        self.clear_button.clicked.connect(self.clear_products)
    
    def load_orders(self):
        """
        Retrieve and display pending orders from the server.
        """        
        response = requests.get("http://localhost:5000/api/order/pending")
        if response.status_code == 200:
            orders_list = response.json()
            row = 0 
            self.pending_orders_table.setRowCount(len(orders_list))
            # print(orders_list)
            for order in orders_list:
                # Creating table items for each order attribute
                customer_name = qtw.QTableWidgetItem(order["customer_name"])
                customer_address = qtw.QTableWidgetItem(order["customer_address"])
                created = qtw.QTableWidgetItem(order["created"])
                completed = qtw.QTableWidgetItem(str(order['completed']))
                order_id = qtw.QTableWidgetItem(str(order["order_id"]))
                # Setting the table items in the corresponding row and column
                self.pending_orders_table.setItem(row, 0, order_id)
                self.pending_orders_table.setItem(row, 1, customer_name)
                self.pending_orders_table.setItem(row, 2, customer_address)
                self.pending_orders_table.setItem(row, 3, created)
                self.pending_orders_table.setItem(row, 4, completed)
                row = row + 1
        else:
            print("Failed to retrieve products")

    def open_order_information(self):
        """
        Retrieve and display information for the selected order.
        """
        # Getting the ID of the selected order
        selected_row = self.pending_orders_table.currentRow()
        order_id = self.pending_orders_table.item(selected_row, 0).text()
        # print(order_id)
        response = requests.get(f"http://localhost:5000/api/order/{order_id}")
        if response.status_code == 200:
            order_list = response.json()
            # print(order_list)
            row = 0 
            # Displaying the order's products in the products table
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
        Clear the products table and total price box.
        """        
        self.products_table.setRowCount(0)
        self.total_price_box.clear()

if __name__ == "__main__":
   # Creating the application instance   
   app = qtw.QApplication(sys.argv)
   # Creating and show the pending orders widget
   window = PendingOrders()
   window.show()
   # Starting the application event loop   
   sys.exit(app.exec())