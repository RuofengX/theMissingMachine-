# -*- coding: utf-8 -*-
from socket import *
import time
# host = '140.143.18.86'      # 获取本地主机名
# port = 575                # 设置端口号


class Connect:
    def __init__(self, mode='server', localhost='192.168.0.1',  target='140.143.18.86', port=576):
        self.sk = socket(AF_INET, SOCK_STREAM)
        self.localhost = localhost
        self.mode = mode
        self.target = target
        self.port = port
        if mode == 'server':
            self.sk.setsockopt(SOL_SOCKET, SO_REUSEPORT, 1)
            self.sk.bind((self.localhost, self.port))
            self.sk.listen(5)
            print('Listening as server')
            self.conn, self.addr = self.sk.accept()
        elif mode == 'client':
            print('Connecting as client')
            self.sk.connect_ex((self.target, self.port))
            self.conn = self.sk
        else:
            print('wrong mode')
            raise Exception
        print('get access')

    def tcp_send(self, content='Hello'):
        print('开始发送')
        self.conn.send(content)
        print('发送成功')
        return

    def tcp_receive(self):
        return self.conn.recv(1024)


if __name__ == '__main__':
    local = Connect(mode='client', target='140.143.18.86')
    while 1:
        text = local.tcp_receive().decode('utf-8')
        print(text)
        time.sleep(5)
