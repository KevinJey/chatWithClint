from socket import *
import sys

HOST = '127.0.0.1'
PORT = 1998
BUFFSIZE = 1024
ADD = (HOST,PORT)

tcpClintSock = socket(AF_INET,SOCK_STREAM)
tcpClintSock.connect(ADD)

while True:
    data = input('>')
    tcpClintSock.send(data.encode())
    if not data:
        break;
print(data.decode('utf-8'))
tcpClintSock.close()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
