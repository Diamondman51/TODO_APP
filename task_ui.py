# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tasks_uitFKMNf.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(450, 62)
        Form.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid black\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#btn_checkbox {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:none\n"
"}\n"
"\n"
"\n"
"\n"
"QLineEdit {\n"
"	border-radius: 2px;\n"
"	border: 1px solid black;\n"
"	padding: 5px\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_checkbox = QPushButton(Form)
        self.btn_checkbox.setObjectName(u"btn_checkbox")
        self.btn_checkbox.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u":/images/check_box_unchecked.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/check_box_checked.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_checkbox.setIcon(icon)
        self.btn_checkbox.setIconSize(QSize(40, 40))
        self.btn_checkbox.setCheckable(True)
        self.btn_checkbox.setChecked(False)

        self.horizontalLayout.addWidget(self.btn_checkbox)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(16777215, 25))
        self.lineEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.btn_top = QPushButton(Form)
        self.btn_top.setObjectName(u"btn_top")
        icon1 = QIcon()
        icon1.addFile(u":/images/top_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_top.setIcon(icon1)
        self.btn_top.setIconSize(QSize(22, 22))

        self.horizontalLayout.addWidget(self.btn_top)

        self.btn_delete = QPushButton(Form)
        self.btn_delete.setObjectName(u"btn_delete")
        icon2 = QIcon()
        icon2.addFile(u":/images/close_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete.setIcon(icon2)
        self.btn_delete.setIconSize(QSize(22, 22))

        self.horizontalLayout.addWidget(self.btn_delete)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_checkbox.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"write task", None))
        self.btn_top.setText("")
        self.btn_delete.setText("")
    # retranslateUi

