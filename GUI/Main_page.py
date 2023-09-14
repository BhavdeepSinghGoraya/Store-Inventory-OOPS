import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from UI.ui_GroceryStoreMainPage import Ui_main_widget_form
from Products import ProductForm
from Orders import OrdersForm

class MainPage(qtw.QWidget, Ui_main_widget_form):
   """
   The main page widget for the grocery store application.
   """
   def __init__(self):
      """
      Initializes the main page widget.
      """      
      super().__init__()
      self.setupUi(self)
      # Connecting the product and orders buttons to their respective slots
      self.products_button.clicked.connect(self.open_product)
      self.orders_button.clicked.connect(self.open_orders)
      
   @qtc.Slot()
   def open_product(self):
      """
      Opens the product form when the product button is clicked.
      """     
      # Creating an instance of the ProductForm and display it       
      self.form = ProductForm()
      self.form.show()
      
   @qtc.Slot()     
   def open_orders(self):
      """
      Opens the orders form when the orders button is clicked.
      """
      # Creating an instance of the OrdersForm and display it
      self.form = OrdersForm()
      self.form.show()

if __name__ == "__main__":
   # Creating the application instance
   app = qtw.QApplication(sys.argv)
   # Creating and show the main page widget
   window = MainPage()
   window.show()
   # Starting the application event loop
   sys.exit(app.exec())