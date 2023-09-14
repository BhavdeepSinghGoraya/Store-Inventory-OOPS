# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'find_orders_window.ui'
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

class Ui_find_order_form(object):
    def setupUi(self, find_order_form):
        if not find_order_form.objectName():
            find_order_form.setObjectName(u"find_order_form")
        find_order_form.resize(1108, 530)
        self.gridLayout = QGridLayout(find_order_form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pending_order_box = QGroupBox(find_order_form)
        self.pending_order_box.setObjectName(u"pending_order_box")
        font = QFont()
        font.setFamilies([u"Cambria"])
        font.setPointSize(12)
        font.setBold(False)
        self.pending_order_box.setFont(font)
        self.pending_order_box.setAlignment(Qt.AlignCenter)
        self.orders_table = QTableWidget(self.pending_order_box)
        if (self.orders_table.columnCount() < 6):
            self.orders_table.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.orders_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.orders_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.orders_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.orders_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.orders_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.orders_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.orders_table.setObjectName(u"orders_table")
        self.orders_table.setGeometry(QRect(10, 29, 771, 431))
        self.orders_table.setFont(font)
        self.select_button = QPushButton(self.pending_order_box)
        self.select_button.setObjectName(u"select_button")
        self.select_button.setGeometry(QRect(520, 470, 75, 31))
        font1 = QFont()
        font1.setFamilies([u"Cambria"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.select_button.setFont(font1)
        self.products_table = QTableWidget(self.pending_order_box)
        if (self.products_table.columnCount() < 3):
            self.products_table.setColumnCount(3)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.products_table.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.products_table.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.products_table.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        self.products_table.setObjectName(u"products_table")
        self.products_table.setGeometry(QRect(790, 20, 301, 431))
        self.clear_button = QPushButton(self.pending_order_box)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setGeometry(QRect(630, 470, 75, 31))
        self.clear_button.setFont(font1)
        self.total_price_label = QLabel(self.pending_order_box)
        self.total_price_label.setObjectName(u"total_price_label")
        self.total_price_label.setGeometry(QRect(800, 470, 81, 16))
        self.total_price_box = QLineEdit(self.pending_order_box)
        self.total_price_box.setObjectName(u"total_price_box")
        self.total_price_box.setGeometry(QRect(890, 470, 113, 21))
        self.label = QLabel(self.pending_order_box)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 470, 121, 31))
        self.customer_name_box = QLineEdit(self.pending_order_box)
        self.customer_name_box.setObjectName(u"customer_name_box")
        self.customer_name_box.setGeometry(QRect(230, 470, 113, 31))
        self.search_button = QPushButton(self.pending_order_box)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setGeometry(QRect(360, 470, 75, 31))
        self.search_button.setFont(font1)

        self.gridLayout.addWidget(self.pending_order_box, 0, 0, 1, 1)


        self.retranslateUi(find_order_form)

        QMetaObject.connectSlotsByName(find_order_form)
    # setupUi

    def retranslateUi(self, find_order_form):
        find_order_form.setWindowTitle(QCoreApplication.translate("find_order_form", u"Grocery Store", None))
        self.pending_order_box.setTitle(QCoreApplication.translate("find_order_form", u" Order List", None))
        ___qtablewidgetitem = self.orders_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("find_order_form", u"Order Id", None));
        ___qtablewidgetitem1 = self.orders_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("find_order_form", u"Customer Name", None));
        ___qtablewidgetitem2 = self.orders_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("find_order_form", u"Customer Address", None));
        ___qtablewidgetitem3 = self.orders_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("find_order_form", u"Processed", None));
        ___qtablewidgetitem4 = self.orders_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("find_order_form", u"Time Created", None));
        ___qtablewidgetitem5 = self.orders_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("find_order_form", u"Completed", None));
        self.select_button.setText(QCoreApplication.translate("find_order_form", u"Select", None))
        ___qtablewidgetitem6 = self.products_table.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("find_order_form", u"Name", None));
        ___qtablewidgetitem7 = self.products_table.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("find_order_form", u"Price", None));
        ___qtablewidgetitem8 = self.products_table.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("find_order_form", u"Quantity ", None));
        self.clear_button.setText(QCoreApplication.translate("find_order_form", u"Clear", None))
        self.total_price_label.setText(QCoreApplication.translate("find_order_form", u"Total Price", None))
        self.label.setText(QCoreApplication.translate("find_order_form", u"Search By Name", None))
        self.search_button.setText(QCoreApplication.translate("find_order_form", u"Search", None))
    # retranslateUi

