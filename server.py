#注册用户名 使用邮箱注册

from socket import *
from time import ctime


if __name__ == '__main__':
    HOST=''
    PORT=1998
    BUFSIZE=1024
    ADDR=(HOST,PORT)

    tcpServerSock=socket(AF_INET,SOCK_STREAM)
    tcpServerSock.bind(ADDR)
    tcpServerSock.listen(5)

    while True:
        print("waiiting in line")
        tcpClintSock,addr = tcpServerSock.accept()
        print("we have been connected")
        while True:
            data = tcpClintSock.recv(BUFSIZE)
            if not data:
                break
            print(data.decode('utf-8'))
        tcpClintSock.close()
    tcpServerSock.close()
