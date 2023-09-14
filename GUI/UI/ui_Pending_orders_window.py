# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Pending_orders_window.ui'
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

class Ui_pending_order_form(object):
    def setupUi(self, pending_order_form):
        if not pending_order_form.objectName():
            pending_order_form.setObjectName(u"pending_order_form")
        pending_order_form.resize(1041, 530)
        self.gridLayout = QGridLayout(pending_order_form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pending_order_box = QGroupBox(pending_order_form)
        self.pending_order_box.setObjectName(u"pending_order_box")
        font = QFont()
        font.setFamilies([u"Cambria"])
        font.setPointSize(12)
        font.setBold(False)
        self.pending_order_box.setFont(font)
        self.pending_order_box.setAlignment(Qt.AlignCenter)
        self.pending_orders_table = QTableWidget(self.pending_order_box)
        if (self.pending_orders_table.columnCount() < 5):
            self.pending_orders_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.pending_orders_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.pending_orders_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.pending_orders_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.pending_orders_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.pending_orders_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.pending_orders_table.setObjectName(u"pending_orders_table")
        self.pending_orders_table.setGeometry(QRect(10, 29, 691, 431))
        self.pending_orders_table.setFont(font)
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
        __qtablewidgetitem5 = QTableWidgetItem()
        self.products_table.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.products_table.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.products_table.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        self.products_table.setObjectName(u"products_table")
        self.products_table.setGeometry(QRect(710, 30, 301, 431))
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

        self.gridLayout.addWidget(self.pending_order_box, 0, 0, 1, 1)


        self.retranslateUi(pending_order_form)

        QMetaObject.connectSlotsByName(pending_order_form)
    # setupUi

    def retranslateUi(self, pending_order_form):
        pending_order_form.setWindowTitle(QCoreApplication.translate("pending_order_form", u"Grocery Store", None))
        self.pending_order_box.setTitle(QCoreApplication.translate("pending_order_form", u"Pending Order List", None))
        ___qtablewidgetitem = self.pending_orders_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("pending_order_form", u"Order Id", None));
        ___qtablewidgetitem1 = self.pending_orders_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("pending_order_form", u"Customer Name", None));
        ___qtablewidgetitem2 = self.pending_orders_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("pending_order_form", u"Customer Address", None));
        ___qtablewidgetitem3 = self.pending_orders_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("pending_order_form", u"Time Created", None));
        ___qtablewidgetitem4 = self.pending_orders_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("pending_order_form", u"Completed", None));
        self.select_button.setText(QCoreApplication.translate("pending_order_form", u"Select", None))
        ___qtablewidgetitem5 = self.products_table.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("pending_order_form", u"Name", None));
        ___qtablewidgetitem6 = self.products_table.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("pending_order_form", u"Price", None));
        ___qtablewidgetitem7 = self.products_table.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("pending_order_form", u"Quantity ", None));
        self.clear_button.setText(QCoreApplication.translate("pending_order_form", u"Clear", None))
        self.total_price_label.setText(QCoreApplication.translate("pending_order_form", u"Total Price", None))
    # retranslateUi

