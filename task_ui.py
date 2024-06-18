# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tasks_uiVMUBAR.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resource_rc
from custom_line_edit import CustomLineEdit


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(459, 66)
        Form.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"	border-radius: 5;\n"
"	border: 1px solid rgba(0, 0, 0, 0.1)\n"
"}\n"
"\n"
"QFrame {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	margin: 2 0 0 2\n"
"}\n"
"\n"
"#btn_checkbox {\n"
"border:none;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border-radius: 2px;\n"
"	border: 1px solid black;\n"
"	padding: 5px\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 0, 15, 0)
        self.btn_checkbox = QPushButton(Form)
        self.btn_checkbox.setObjectName(u"btn_checkbox")
        self.btn_checkbox.setMinimumSize(QSize(30, 30))
        self.btn_checkbox.setMaximumSize(QSize(30, 30))
        self.btn_checkbox.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/images/check_box_unchecked.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/check_box_checked.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_checkbox.setIcon(icon)
        self.btn_checkbox.setIconSize(QSize(40, 40))
        self.btn_checkbox.setCheckable(True)
        self.btn_checkbox.setChecked(False)

        self.horizontalLayout_2.addWidget(self.btn_checkbox)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.lineEdit = CustomLineEdit(self)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(300, 30))
        self.lineEdit.setMaximumSize(QSize(16777215, 30))
        self.lineEdit.setStyleSheet(u"")
        self.lineEdit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_edit = QPushButton(Form)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setMinimumSize(QSize(71, 33))
        self.btn_edit.setMaximumSize(QSize(71, 33))
        icon1 = QIcon()
        icon1.addFile(u":/images/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_edit.setIcon(icon1)
        self.btn_edit.setIconSize(QSize(40, 25))
        self.btn_edit.setCheckable(False)
        self.btn_edit.setChecked(False)

        self.verticalLayout.addWidget(self.btn_edit)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(71, 31))
        self.frame.setMaximumSize(QSize(71, 31))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_top = QPushButton(self.frame)
        self.btn_top.setObjectName(u"btn_top")
        self.btn_top.setMinimumSize(QSize(34, 30))
        self.btn_top.setMaximumSize(QSize(34, 30))
        icon2 = QIcon()
        icon2.addFile(u":/images/top_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_top.setIcon(icon2)
        self.btn_top.setIconSize(QSize(22, 22))
        self.btn_top.setCheckable(False)

        self.horizontalLayout.addWidget(self.btn_top)

        self.btn_delete = QPushButton(self.frame)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setMinimumSize(QSize(34, 30))
        self.btn_delete.setMaximumSize(QSize(34, 30))
        icon3 = QIcon()
        icon3.addFile(u":/images/close_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete.setIcon(icon3)
        self.btn_delete.setIconSize(QSize(22, 22))
        self.btn_delete.setCheckable(False)

        self.horizontalLayout.addWidget(self.btn_delete)


        self.verticalLayout.addWidget(self.frame)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)
        self.btn_edit.clicked.connect(self.frame.show)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_checkbox.setText("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("")
        self.btn_edit.setText("")
        self.btn_top.setText("")
        self.btn_delete.setText("")
    # retranslateUi

