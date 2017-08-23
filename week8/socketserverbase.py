#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/23 17:40.

import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):

        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data.decode('utf-8'))
                # if not self.data:#client break
                #     print(self.client_address,"break")
                #     break
                self.request.send(self.data.upper())
            except ConnectionResetError as e:
                print("err:",e)
                break

if __name__ == "__main__":
    HOST,PORT = "localhost",6969
    #create the server,binding to localhost on port 9966
    server = socketserver.TCPServer((HOST,PORT),MyTCPHandler)
    server.serve_forever()

