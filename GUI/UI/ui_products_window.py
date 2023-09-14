# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'products_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_productForm(object):
    def setupUi(self, productForm):
        if not productForm.objectName():
            productForm.setObjectName(u"productForm")
        productForm.resize(549, 313)
        self.gridLayout = QGridLayout(productForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(productForm)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setFamilies([u"Cambria"])
        font.setPointSize(16)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.price_entry = QLineEdit(self.groupBox)
        self.price_entry.setObjectName(u"price_entry")
        font1 = QFont()
        font1.setFamilies([u"Cambria"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.price_entry.setFont(font1)

        self.gridLayout_2.addWidget(self.price_entry, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.update_product_button = QPushButton(self.groupBox)
        self.update_product_button.setObjectName(u"update_product_button")
        font2 = QFont()
        font2.setFamilies([u"Cambria"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.update_product_button.setFont(font2)

        self.gridLayout_2.addWidget(self.update_product_button, 1, 3, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.quantit_entry = QLineEdit(self.groupBox)
        self.quantit_entry.setObjectName(u"quantit_entry")
        self.quantit_entry.setFont(font1)

        self.gridLayout_2.addWidget(self.quantit_entry, 2, 1, 1, 1)

        self.name_entry = QLineEdit(self.groupBox)
        self.name_entry.setObjectName(u"name_entry")
        self.name_entry.setFont(font1)

        self.gridLayout_2.addWidget(self.name_entry, 0, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.add_product_button = QPushButton(self.groupBox)
        self.add_product_button.setObjectName(u"add_product_button")
        self.add_product_button.setFont(font2)

        self.gridLayout_2.addWidget(self.add_product_button, 0, 3, 1, 1)

        self.view_all_products_button = QPushButton(self.groupBox)
        self.view_all_products_button.setObjectName(u"view_all_products_button")
        self.view_all_products_button.setFont(font2)

        self.gridLayout_2.addWidget(self.view_all_products_button, 3, 3, 1, 1)

        self.delete_product_button = QPushButton(self.groupBox)
        self.delete_product_button.setObjectName(u"delete_product_button")
        self.delete_product_button.setFont(font2)

        self.gridLayout_2.addWidget(self.delete_product_button, 2, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.clear_button = QPushButton(self.groupBox)
        self.clear_button.setObjectName(u"clear_button")
        font3 = QFont()
        font3.setFamilies([u"Cambria"])
        font3.setPointSize(16)
        font3.setBold(False)
        self.clear_button.setFont(font3)

        self.gridLayout_2.addWidget(self.clear_button, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(productForm)

        QMetaObject.connectSlotsByName(productForm)
    # setupUi

    def retranslateUi(self, productForm):
        productForm.setWindowTitle(QCoreApplication.translate("productForm", u"Grocery Store", None))
        self.groupBox.setTitle(QCoreApplication.translate("productForm", u"Products", None))
        self.label_2.setText(QCoreApplication.translate("productForm", u"Price", None))
        self.update_product_button.setText(QCoreApplication.translate("productForm", u"Update Product", None))
        self.label_3.setText(QCoreApplication.translate("productForm", u"Quantity", None))
        self.label.setText(QCoreApplication.translate("productForm", u"Name", None))
        self.add_product_button.setText(QCoreApplication.translate("productForm", u"Add Product", None))
        self.view_all_products_button.setText(QCoreApplication.translate("productForm", u"View All Products", None))
        self.delete_product_button.setText(QCoreApplication.translate("productForm", u"Delete Product", None))
        self.clear_button.setText(QCoreApplication.translate("productForm", u"Clear", None))
    # retranslateUi

