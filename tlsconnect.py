#!/usr/bin/python3.4


import socket
import sys


class HTTPclient:
    """connection with the 80 port"""

    def __init__(self, host):
        self.target_host = host
        self.target_port = 80

    def getconnection(self):

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.target_host, self.target_port))
        client.send("GET / HTTP/1.1\r\nHost: {0}\r\n\r\n".format(self.target_host).encode())
        response = client.recv(4096)
        client.close
        return response


if __name__ == "__main__":
    user = HTTPclient("www.siteduzero.com")
    print(user.getconnection())
