# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
import threading

import socket

from common.util.logger import Logger


class ClientHandler(threading.Thread):
    def __init__(self, server_handler, client_socket: socket, client_info):
        super(ClientHandler, self).__init__()
        self.server_handler = server_handler
        self.client_socket: socket = client_socket
        self.client_info = client_info
        self.connected = True

    def run(self):
        # Receive loop
        while self.connected:

            received_data = self.client_socket.recv(2048)
            self.parse_data_from_client(received_data)

    def parse_data_from_client(self, data):
        data_split = data.decode().split("^")

        if data.decode().startswith("[AUTH]"):
            nickname = data_split[1]

            for (client_socket, client_info) in self.server_handler.connected_clients:
                if client_info.nickname == nickname:
                    Logger.log("Klient o nicku {0} juz istnieje. Klient {1} zostanie rozlaczony!".format(nickname, self.client_info.address))
                    client_socket.send("[NAMETAKEN]".encode())
                    self.server_handler.connected_clients.remove((client_socket, client_info))
                    self.client_socket.close()
                    self.connected = False
                    break

            Logger.log("Poprawna autentykacja klienta {0} o nicku {1}".format(self.client_info.address, nickname))
            self.client_info.nickname = nickname
            self.client_socket.send("[NAMEAVAILABLE]".encode())
