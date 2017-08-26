#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/23 17:40.

import socketserver
import json,os

class MyTCPHandler(socketserver.BaseRequestHandler):

    def put(self,*args):
        """receive client file"""
        cmd_dic = args[0]
        filename = cmd_dic["filename"]
        filesize = cmd_dic["size"]
        if os.path.isfile(filename):
            f = open(filename+"copy","wb")
        else:
            f = open(filename, "wb")
        self.request.send("200 ok".encode("utf-8"))
        receive_size = 0
        while receive_size < filesize:
            data = self.request.recv(1024)
            f.write(data)
            receive_size += len(data)
        else:
            print("file [%s] has uploaded..."%filename)

    def handle(self):

        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data.decode('utf-8'))
                cmd_dic = json.loads(self.data.decode())
                action = cmd_dic["action"]
                if hasattr(self,action):
                    func = getattr(self,action)
                    func(cmd_dic)
                # if not self.data:#client break
                #     print(self.client_address,"break")
                #     break
                self.request.send(self.data.upper())
            except ConnectionResetError as e:
                print("err:",e)
                break

if __name__ == "__main__":
    HOST,PORT = "localhost",9966
    #create the server,binding to localhost on port 9966
    server = socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
    server.serve_forever()


