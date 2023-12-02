import socket
import traceback


class TCP_receiver:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self,host,port):

         self.sock.connect((host,port))


    def write_logs(self,data,filename:str):
        logs = open(filename, 'a')
        logs.write(str(data) + '\n')
        logs.close()

    def receive_data(self):
        data = self.sock.recv(1024)
        return data


    def disconnect(self):
        self.sock.close()