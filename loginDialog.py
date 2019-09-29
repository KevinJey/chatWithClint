# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoLogin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt, qDebug
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QPushButton


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(422, 315)
        self.label_3 = QtWidgets.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 110, 51, 20))
        self.label_3.setObjectName("label_3")
        self.userIcon = QtWidgets.QLabel(dialog)
        self.userIcon.setGeometry(QtCore.QRect(30, 100, 30, 30))
        self.userIcon.setText("")
        self.userIcon.setObjectName("userIcon")
        self.layoutWidget = QtWidgets.QWidget(dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 140, 338, 155))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(336, 24, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(336, 36, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.SignUpButton = QtWidgets.QPushButton(self.layoutWidget)
        self.SignUpButton.setObjectName("SignUpButton")
        self.horizontalLayout_3.addWidget(self.SignUpButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        img = QImage("usericon.jpg")
        size = QSize(30,30)
        pixImg = QPixmap.fromImage(img.scaled(size,Qt.IgnoreAspectRatio))
        self.userIcon.setPixmap(pixImg)

        self.button = QPushButton()
        self.horizontalLayout.addWidget(self.button)


        self.button.released.connect(self.releaseFunc)
        self.button.clicked.connect(self.clickedFunc)

        self.retranslateUi(dialog)
        self.SignUpButton.clicked.connect(dialog.close)
        QtCore.QMetaObject.connectSlotsByName(dialog)
    def clickedFunc(self):
        qDebug("clicked")
    def releaseFunc(self):
        qDebug("release")
    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "登陆界面"))
        self.label_3.setText(_translate("dialog", "登陆界面"))
        self.label.setText(_translate("dialog", "Account"))
        self.label_2.setText(_translate("dialog", "PassWord"))
        self.pushButton.setText(_translate("dialog", "Login"))
        self.SignUpButton.setText(_translate("dialog", "Sign Up"))
