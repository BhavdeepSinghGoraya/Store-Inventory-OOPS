# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Orders_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_OrdersForm(object):
    def setupUi(self, OrdersForm):
        if not OrdersForm.objectName():
            OrdersForm.setObjectName(u"OrdersForm")
        OrdersForm.resize(659, 511)
        self.gridLayout = QGridLayout(OrdersForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ProductsList = QGroupBox(OrdersForm)
        self.ProductsList.setObjectName(u"ProductsList")
        font = QFont()
        font.setFamilies([u"Cambria"])
        font.setPointSize(12)
        font.setBold(False)
        self.ProductsList.setFont(font)
        self.ProductsList.setAlignment(Qt.AlignCenter)
        self.products_table = QTableWidget(self.ProductsList)
        if (self.products_table.columnCount() < 3):
            self.products_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.products_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.products_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.products_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.products_table.setObjectName(u"products_table")
        self.products_table.setGeometry(QRect(10, 30, 301, 411))
        font1 = QFont()
        font1.setFamilies([u"Cambria"])
        font1.setPointSize(11)
        font1.setBold(False)
        self.products_table.setFont(font1)
        self.OutofstockGropuBox = QGroupBox(self.ProductsList)
        self.OutofstockGropuBox.setObjectName(u"OutofstockGropuBox")
        self.OutofstockGropuBox.setGeometry(QRect(0, 449, 281, 41))
        self.view_out_of_stock_button = QPushButton(self.ProductsList)
        self.view_out_of_stock_button.setObjectName(u"view_out_of_stock_button")
        self.view_out_of_stock_button.setGeometry(QRect(10, 460, 141, 24))
        font2 = QFont()
        font2.setFamilies([u"Cambria"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.view_out_of_stock_button.setFont(font2)
        self.select_button = QPushButton(self.ProductsList)
        self.select_button.setObjectName(u"select_button")
        self.select_button.setGeometry(QRect(190, 460, 75, 24))
        self.select_button.setFont(font2)

        self.gridLayout.addWidget(self.ProductsList, 0, 0, 1, 1)

        self.OrderGroupBox = QGroupBox(OrdersForm)
        self.OrderGroupBox.setObjectName(u"OrderGroupBox")
        self.OrderGroupBox.setFont(font)
        self.OrderGroupBox.setAlignment(Qt.AlignCenter)
        self.order_table = QTableWidget(self.OrderGroupBox)
        if (self.order_table.columnCount() < 3):
            self.order_table.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.order_table.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.order_table.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.order_table.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.order_table.setObjectName(u"order_table")
        self.order_table.setGeometry(QRect(10, 370, 301, 121))
        self.order_table.setFont(font1)
        self.label = QLabel(self.OrderGroupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 40, 71, 16))
        self.label.setFont(font)
        self.order_id_box = QLineEdit(self.OrderGroupBox)
        self.order_id_box.setObjectName(u"order_id_box")
        self.order_id_box.setGeometry(QRect(90, 40, 51, 21))
        self.order_id_box.setFont(font1)
        self.view_order_button = QPushButton(self.OrderGroupBox)
        self.view_order_button.setObjectName(u"view_order_button")
        self.view_order_button.setGeometry(QRect(190, 30, 111, 31))
        self.view_order_button.setFont(font2)
        self.create_order_button = QPushButton(self.OrderGroupBox)
        self.create_order_button.setObjectName(u"create_order_button")
        self.create_order_button.setGeometry(QRect(190, 80, 111, 31))
        self.create_order_button.setFont(font2)
        self.delete_order_button = QPushButton(self.OrderGroupBox)
        self.delete_order_button.setObjectName(u"delete_order_button")
        self.delete_order_button.setGeometry(QRect(190, 130, 111, 31))
        self.delete_order_button.setFont(font2)
        self.process_order_button = QPushButton(self.OrderGroupBox)
        self.process_order_button.setObjectName(u"process_order_button")
        self.process_order_button.setGeometry(QRect(10, 80, 131, 31))
        self.process_order_button.setFont(font2)
        self.view_processed_orders = QPushButton(self.OrderGroupBox)
        self.view_processed_orders.setObjectName(u"view_processed_orders")
        self.view_processed_orders.setGeometry(QRect(10, 130, 171, 31))
        font3 = QFont()
        font3.setFamilies([u"Cambria"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.view_processed_orders.setFont(font3)
        self.view_pending_orders = QPushButton(self.OrderGroupBox)
        self.view_pending_orders.setObjectName(u"view_pending_orders")
        self.view_pending_orders.setGeometry(QRect(10, 180, 171, 31))
        self.view_pending_orders.setFont(font3)
        self.find_order_button = QPushButton(self.OrderGroupBox)
        self.find_order_button.setObjectName(u"find_order_button")
        self.find_order_button.setGeometry(QRect(190, 180, 111, 31))
        self.find_order_button.setFont(font2)
        self.name_label = QLabel(self.OrderGroupBox)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(10, 280, 49, 16))
        self.customer_name_box = QLineEdit(self.OrderGroupBox)
        self.customer_name_box.setObjectName(u"customer_name_box")
        self.customer_name_box.setGeometry(QRect(70, 280, 151, 21))
        self.label_2 = QLabel(self.OrderGroupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 310, 61, 16))
        self.customer_address_box = QLineEdit(self.OrderGroupBox)
        self.customer_address_box.setObjectName(u"customer_address_box")
        self.customer_address_box.setGeometry(QRect(70, 310, 151, 21))
        self.price_label = QLabel(self.OrderGroupBox)
        self.price_label.setObjectName(u"price_label")
        self.price_label.setGeometry(QRect(10, 340, 49, 16))
        self.order_price_box = QLineEdit(self.OrderGroupBox)
        self.order_price_box.setObjectName(u"order_price_box")
        self.order_price_box.setGeometry(QRect(70, 340, 151, 21))
        self.update_order_button = QPushButton(self.OrderGroupBox)
        self.update_order_button.setObjectName(u"update_order_button")
        self.update_order_button.setGeometry(QRect(190, 230, 111, 31))
        self.update_order_button.setFont(font2)
        self.clear_button = QPushButton(self.OrderGroupBox)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setGeometry(QRect(20, 230, 75, 31))
        self.clear_button.setFont(font2)

        self.gridLayout.addWidget(self.OrderGroupBox, 0, 1, 1, 1)


        self.retranslateUi(OrdersForm)

        QMetaObject.connectSlotsByName(OrdersForm)
    # setupUi

    def retranslateUi(self, OrdersForm):
        OrdersForm.setWindowTitle(QCoreApplication.translate("OrdersForm", u"Grocery Store", None))
        self.ProductsList.setTitle(QCoreApplication.translate("OrdersForm", u"Products List ", None))
        ___qtablewidgetitem = self.products_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("OrdersForm", u"Name", None));
        ___qtablewidgetitem1 = self.products_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("OrdersForm", u"Price", None));
        ___qtablewidgetitem2 = self.products_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("OrdersForm", u"Quantity", None));
        self.OutofstockGropuBox.setTitle("")
        self.view_out_of_stock_button.setText(QCoreApplication.translate("OrdersForm", u"View Out of Stock", None))
        self.select_button.setText(QCoreApplication.translate("OrdersForm", u"Select", None))
        self.OrderGroupBox.setTitle(QCoreApplication.translate("OrdersForm", u"Orders", None))
        ___qtablewidgetitem3 = self.order_table.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("OrdersForm", u"Name", None));
        ___qtablewidgetitem4 = self.order_table.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("OrdersForm", u"Price", None));
        ___qtablewidgetitem5 = self.order_table.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("OrdersForm", u"Quantity", None));
        self.label.setText(QCoreApplication.translate("OrdersForm", u"Order ID", None))
        self.view_order_button.setText(QCoreApplication.translate("OrdersForm", u"View Order", None))
        self.create_order_button.setText(QCoreApplication.translate("OrdersForm", u"Create Order", None))
        self.delete_order_button.setText(QCoreApplication.translate("OrdersForm", u"Delete Order", None))
        self.process_order_button.setText(QCoreApplication.translate("OrdersForm", u"Process Order", None))
        self.view_processed_orders.setText(QCoreApplication.translate("OrdersForm", u"View Processed Orders", None))
        self.view_pending_orders.setText(QCoreApplication.translate("OrdersForm", u"View Pending Orders", None))
        self.find_order_button.setText(QCoreApplication.translate("OrdersForm", u"Find Order", None))
        self.name_label.setText(QCoreApplication.translate("OrdersForm", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("OrdersForm", u"Address", None))
        self.price_label.setText(QCoreApplication.translate("OrdersForm", u"Price", None))
        self.update_order_button.setText(QCoreApplication.translate("OrdersForm", u"Update Order", None))
        self.clear_button.setText(QCoreApplication.translate("OrdersForm", u"Clear", None))
    # retranslateUi

