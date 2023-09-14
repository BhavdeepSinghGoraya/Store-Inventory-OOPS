import sys
from PySide6 import QtWidgets as qtw
import requests

from UI.ui_ProductListWindow import Ui_widget

class ViewProducts(qtw.QWidget, Ui_widget):
    """
    The main widget for displaying a list of products retrieved from the server.
    """
    def __init__(self): 
        """
        Initializes the product list widget.
        """        
        super().__init__()
        self.setupUi(self)
        # Setting the column widths for the product table
        self.products_table.setColumnWidth(0,175)
        self.products_table.setColumnWidth(1,150)
        self.products_table.setColumnWidth(2,150)
        # Load the list of products from the server
        self.loadproducts()

    def loadproducts(self):
        """
        Loads the list of products from the server and displays them in the product table.
        """        
        response = requests.get("http://localhost:5000/api/product")
        if response.status_code == 200:
            products_list = response.json()
            # Setting the number of rows in the product table
            self.products_table.setRowCount(len(products_list))
            # Adding each product to the table
            row = 0 
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

if __name__ == "__main__":
   # Creating the application instance
   app = qtw.QApplication(sys.argv)
   # Creating and show the product list widget
   window = ViewProducts()
   window.show()
   # Starting the application event loop
   sys.exit(app.exec())