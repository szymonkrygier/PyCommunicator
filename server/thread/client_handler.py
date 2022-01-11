 # Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
import threading

import socket

from common.util.logger import Logger


class ClientHandler(threading.Thread):
    def __init__(self, server_handler, client_info):
        super(ClientHandler, self).__init__()
        self.server_handler = server_handler
        self.client_info = client_info
        self.connected = True

    def run(self):
        # Receive loop
        while self.connected:
            try:
                received_data = self.client_info.client_socket.recv(2048)
            except socket.error:
                self.connected = False
                self.server_handler.remove_client(self.client_info)
                return

            self.parse_data_from_client(received_data)

    def parse_data_from_client(self, data):
        data_split = data.decode().split("^")
        command = data_split[0]

        # [AUTH] - Client authentication
        if command == "[AUTH]":
            nickname = data_split[1]

            # Check if client with same nickname already exists
            for client_entry in self.server_handler.connected_clients:
                if client_entry.nickname == nickname:
                    self.client_info.client_socket.send("[NAMETAKEN]".encode())
                    self.client_info.client_socket.close()
                    self.server_handler.connected_clients.remove(self.client_info)
                    self.connected = False
                    Logger.log("Klient o adresie {0} zostal wyrzucony: nickname {1} jest juz zajety!".format(
                        self.client_info.ip + ":" + str(self.client_info.port), nickname))
                    return

            # Authenticate client if nickname is not taken
            self.client_info.nickname = nickname
            self.client_info.client_socket.send("[AUTHENTICATED]".encode())
            Logger.log("Poprawna autentykacja klienta o adresie {0} i nickname {1}".format(
                self.client_info.ip + ":" + str(self.client_info.port), nickname))
            self.server_handler.send_available_users()
        # [DISCONNECT] - Client disconnected from server
        elif command == "[DISCONNECT]":
            self.connected = False
            self.server_handler.remove_client(self.client_info.client_socket)
