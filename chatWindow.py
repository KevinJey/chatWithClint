from PyQt5 import QtWidgets,QtCore,QtGui
import loginDialog
import chatPanel

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginDialog = QtWidgets.QDialog()
    ui = loginDialog.Ui_dialog()
    ui.setupUi(LoginDialog)
    LoginDialog.exec()

    chatMainWindow = QtWidgets.QMainWindow()
    chatUi = chatPanel.Ui_MainWindow()
    chatUi.setupUi(chatMainWindow)
    chatMainWindow.show()
    sys.exit(app.exec())
