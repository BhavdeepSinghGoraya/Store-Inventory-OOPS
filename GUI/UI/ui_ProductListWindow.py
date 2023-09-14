# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProductListWindow.ui'
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
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(523, 520)
        self.gridLayout = QGridLayout(widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.products_table = QTableWidget(widget)
        if (self.products_table.columnCount() < 3):
            self.products_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.products_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.products_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.products_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.products_table.setObjectName(u"products_table")

        self.gridLayout.addWidget(self.products_table, 1, 0, 1, 1)

        self.groupBox = QGroupBox(widget)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setFamilies([u"Cambria"])
        font.setPointSize(12)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"Grocery Store", None))
        ___qtablewidgetitem = self.products_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("widget", u"Name", None));
        ___qtablewidgetitem1 = self.products_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("widget", u"Price", None));
        ___qtablewidgetitem2 = self.products_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("widget", u"Quantity", None));
        self.groupBox.setTitle(QCoreApplication.translate("widget", u"Products List", None))
    # retranslateUi

