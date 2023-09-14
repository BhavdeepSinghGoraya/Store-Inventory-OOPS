# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GroceryStoreMainPage.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_main_widget_form(object):
    def setupUi(self, main_widget_form):
        if not main_widget_form.objectName():
            main_widget_form.setObjectName(u"main_widget_form")
        main_widget_form.resize(494, 244)
        font = QFont()
        font.setPointSize(12)
        main_widget_form.setFont(font)
        self.gridLayout = QGridLayout(main_widget_form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(main_widget_form)
        self.groupBox.setObjectName(u"groupBox")
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic UI Semibold"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.groupBox.setFont(font1)
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.products_button = QPushButton(self.groupBox)
        self.products_button.setObjectName(u"products_button")
        self.products_button.setMaximumSize(QSize(95, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Cambria"])
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setItalic(False)
        self.products_button.setFont(font2)

        self.gridLayout_2.addWidget(self.products_button, 0, 1, 2, 1)

        self.orders_button = QPushButton(self.groupBox)
        self.orders_button.setObjectName(u"orders_button")
        self.orders_button.setFont(font2)

        self.gridLayout_2.addWidget(self.orders_button, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(main_widget_form)

        QMetaObject.connectSlotsByName(main_widget_form)
    # setupUi

    def retranslateUi(self, main_widget_form):
        main_widget_form.setWindowTitle(QCoreApplication.translate("main_widget_form", u"Grocery Store", None))
        self.groupBox.setTitle(QCoreApplication.translate("main_widget_form", u"Welcome to the Grocery Store!", None))
        self.products_button.setText(QCoreApplication.translate("main_widget_form", u"Products", None))
        self.orders_button.setText(QCoreApplication.translate("main_widget_form", u"Orders", None))
    # retranslateUi

