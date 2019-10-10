# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox

import chatPanel

class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/loginIcon/QQScLauncher.exe(129).ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setWindowOpacity(4.0)
        Dialog.setStyleSheet("")
        Dialog.setModal(False)
        self.login = QtWidgets.QPushButton(Dialog)
        self.login.setGeometry(QtCore.QRect(130, 270, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        self.login.setFont(font)
        self.login.setStyleSheet("selection-color: rgb(108, 142, 255);\n"
"selection-background-color: rgb(52, 96, 255);")
        self.login.setObjectName("login")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 30, 101, 61))
        self.label.setStyleSheet("image: url(:/loginIcon/QQScLauncher.exe(129).png);\n"
"font: 28pt \"Ubuntu\" ;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.headIcon = QtWidgets.QLabel(Dialog)
        self.headIcon.setGeometry(QtCore.QRect(20, 140, 91, 91))
        self.headIcon.setStyleSheet("image: url(:/loginIcon/picHead.jpeg);")
        self.headIcon.setText("")
        self.headIcon.setObjectName("headIcon")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(200, 20, 111, 81))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(40)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.RememberPass = QtWidgets.QCheckBox(Dialog)
        self.RememberPass.setGeometry(QtCore.QRect(130, 210, 127, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.RememberPass.setFont(font)
        self.RememberPass.setObjectName("RememberPass")
        self.AutoLogin = QtWidgets.QCheckBox(Dialog)
        self.AutoLogin.setGeometry(QtCore.QRect(280, 210, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.AutoLogin.setFont(font)
        self.AutoLogin.setObjectName("AutoLogin")
        self.forgetLabel = QtWidgets.QLabel(Dialog)
        self.forgetLabel.setEnabled(True)
        self.forgetLabel.setGeometry(QtCore.QRect(370, 130, 59, 42))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.forgetLabel.setFont(font)
        self.forgetLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.forgetLabel.setMouseTracking(True)
        self.forgetLabel.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.forgetLabel.setAcceptDrops(False)
        self.forgetLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.forgetLabel.setAutoFillBackground(True)
        self.forgetLabel.setStyleSheet("color: rgb(126, 176, 255);")
        self.forgetLabel.setTextFormat(QtCore.Qt.RichText)
        self.forgetLabel.setObjectName("forgetLabel")
        self.signupLabel = QtWidgets.QLabel(Dialog)
        self.signupLabel.setGeometry(QtCore.QRect(370, 170, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.signupLabel.setFont(font)
        self.signupLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signupLabel.setStyleSheet("color: rgb(82, 174, 255);")
        self.signupLabel.setObjectName("signupLabel")
        self.Account = QtWidgets.QLineEdit(Dialog)
        self.Account.setGeometry(QtCore.QRect(130, 140, 231, 31))
        self.Account.setObjectName("Account")
        self.Password = QtWidgets.QLineEdit(Dialog)
        self.Password.setGeometry(QtCore.QRect(130, 170, 231, 31))
        self.Password.setObjectName("Password")
        self.login.raise_()
        self.headIcon.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.RememberPass.raise_()
        self.AutoLogin.raise_()
        self.forgetLabel.raise_()
        self.signupLabel.raise_()
        self.Account.raise_()
        self.Password.raise_()

        self.login.clicked.connect(self.showDialog)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login Dialog"))
        self.login.setText(_translate("Dialog", "Login"))
        self.label_3.setText(_translate("Dialog", "TIM"))
        self.RememberPass.setText(_translate("Dialog", "Remember Pwd"))
        self.AutoLogin.setText(_translate("Dialog", "AutoLogin"))
        self.forgetLabel.setText(_translate("Dialog", "Forget?"))
        self.signupLabel.setText(_translate("Dialog", "Sign Up"))
    def showDialog(self):
        if self.Account.text() == "admin" and self.Password.text() == "123":
            QMessageBox.information(self,"登录成功","恭喜你登陆成功",QMessageBox.Ok,QMessageBox.Ok)
            self.close()
            chatPanel.Ui_MainWindow().exec_()
            # chatMainWindow = QtWidgets.QMainWindow()
            # chatUi = chatPanel.Ui_MainWindow()
            # chatUi.setupUi(chatMainWindow)
            # chatMainWindow.exec_()
import icons_rc
