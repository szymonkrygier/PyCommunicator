# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
import threading

import socket


class ClientHandler(threading.Thread):
    def __init__(self, client_socket: socket, client_info):
        super(ClientHandler, self).__init__()
        self.client_socket: socket = client_socket
        self.client_info = client_info

    def run(self):
        # Receive loop
        while True:
            received_data = self.client_socket.recv(2048)
            self.parse_data_from_client(received_data)

    def parse_data_from_client(self, data):
        data_split = data.decode().split("^")

        if data.decode().startswith('[AUTH]'):
            nickname = data_split[1]
            self.client_info.nickname = nickname
