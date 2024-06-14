# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'list_of_tasks_uiOKwsfO.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(472, 300)
        Form.setStyleSheet(u"QLabel {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color:rgb(90, 185, 90)\n"
"}\n"
"\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(171, 255, 46);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border-radius: 5px;\n"
"	border: 1 solid rgba(0, 0, 0, 0.1)\n"
"}\n"
"\n"
"QListWidget {\n"
"	background-color:rgb(138, 255, 197);\n"
"}\n"
"\n"
"#widget_2 {\n"
"	background-color: rgb(45, 81, 60);\n"
"}\n"
"\n"
"#widget {\n"
"	background-color: rgb(85, 207, 19)\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setPixmap(QPixmap(u":/images/check_box_checked.png"))
        self.label.setScaledContents(True)
        self.label.setIndent(6)

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.task_lineEdit = QLineEdit(self.widget)
        self.task_lineEdit.setObjectName(u"task_lineEdit")
        self.task_lineEdit.setMinimumSize(QSize(388, 30))
        self.task_lineEdit.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_2.addWidget(self.task_lineEdit)

        self.btn_add_task = QPushButton(self.widget)
        self.btn_add_task.setObjectName(u"btn_add_task")
        self.btn_add_task.setMaximumSize(QSize(30, 16777215))
        icon = QIcon()
        icon.addFile(u":/images/add_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_task.setIcon(icon)
        self.btn_add_task.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.btn_add_task)


        self.verticalLayout.addWidget(self.widget)

        self.tasks_listWidget = QListWidget(Form)
        self.tasks_listWidget.setObjectName(u"tasks_listWidget")
        self.tasks_listWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout.addWidget(self.tasks_listWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"TODO", None))
        self.btn_add_task.setText("")
    # retranslateUi

