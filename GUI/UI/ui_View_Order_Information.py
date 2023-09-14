# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'View_Order_Information.ui'
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
    QLabel, QLineEdit, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_view_order_information(object):
    def setupUi(self, view_order_information):
        if not view_order_information.objectName():
            view_order_information.setObjectName(u"view_order_information")
        view_order_information.resize(424, 403)
        self.gridLayout = QGridLayout(view_order_information)
        self.gridLayout.setObjectName(u"gridLayout")
        self.orderinformationbox = QGroupBox(view_order_information)
        self.orderinformationbox.setObjectName(u"orderinformationbox")
        font = QFont()
        font.setFamilies([u"Cambria"])
        font.setPointSize(12)
        self.orderinformationbox.setFont(font)
        self.orderinformationbox.setAlignment(Qt.AlignCenter)
        self.customer_name_box = QLineEdit(self.orderinformationbox)
        self.customer_name_box.setObjectName(u"customer_name_box")
        self.customer_name_box.setGeometry(QRect(160, 90, 151, 21))
        self.order_id_box = QLineEdit(self.orderinformationbox)
        self.order_id_box.setObjectName(u"order_id_box")
        self.order_id_box.setGeometry(QRect(160, 50, 71, 21))
        self.customer_address_box = QLineEdit(self.orderinformationbox)
        self.customer_address_box.setObjectName(u"customer_address_box")
        self.customer_address_box.setGeometry(QRect(160, 130, 151, 21))
        self.total_price_box = QLineEdit(self.orderinformationbox)
        self.total_price_box.setObjectName(u"total_price_box")
        self.total_price_box.setGeometry(QRect(160, 170, 111, 21))
        self.order_id_label = QLabel(self.orderinformationbox)
        self.order_id_label.setObjectName(u"order_id_label")
        self.order_id_label.setGeometry(QRect(50, 50, 61, 20))
        self.customer_name_lable = QLabel(self.orderinformationbox)
        self.customer_name_lable.setObjectName(u"customer_name_lable")
        self.customer_name_lable.setGeometry(QRect(10, 90, 131, 21))
        self.customer_addres_lable = QLabel(self.orderinformationbox)
        self.customer_addres_lable.setObjectName(u"customer_addres_lable")
        self.customer_addres_lable.setGeometry(QRect(10, 130, 141, 20))
        self.label = QLabel(self.orderinformationbox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 170, 91, 20))
        self.order_infomation_table = QTableWidget(self.orderinformationbox)
        if (self.order_infomation_table.columnCount() < 3):
            self.order_infomation_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.order_infomation_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.order_infomation_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.order_infomation_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.order_infomation_table.setObjectName(u"order_infomation_table")
        self.order_infomation_table.setGeometry(QRect(0, 200, 401, 192))

        self.gridLayout.addWidget(self.orderinformationbox, 0, 1, 1, 1)


        self.retranslateUi(view_order_information)

        QMetaObject.connectSlotsByName(view_order_information)
    # setupUi

    def retranslateUi(self, view_order_information):
        view_order_information.setWindowTitle(QCoreApplication.translate("view_order_information", u"Grocery Store", None))
        self.orderinformationbox.setTitle(QCoreApplication.translate("view_order_information", u"Order Information", None))
        self.order_id_label.setText(QCoreApplication.translate("view_order_information", u"Order ID", None))
        self.customer_name_lable.setText(QCoreApplication.translate("view_order_information", u"Customer Name", None))
        self.customer_addres_lable.setText(QCoreApplication.translate("view_order_information", u"Customer Address", None))
        self.label.setText(QCoreApplication.translate("view_order_information", u"Total Price", None))
        ___qtablewidgetitem = self.order_infomation_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("view_order_information", u"Name", None));
        ___qtablewidgetitem1 = self.order_infomation_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("view_order_information", u"Price", None));
        ___qtablewidgetitem2 = self.order_infomation_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("view_order_information", u"Quantity", None));
    # retranslateUi

