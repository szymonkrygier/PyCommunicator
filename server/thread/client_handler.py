# PyCommunicator
# Copyright (C) 2022-2025 Szymon Krygier <szymon.krygier@pulsax.pl>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
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
            Logger.log("Klient o adresie {0} i nickname {1} rozlaczyl sie od serwera".format(
                self.client_info.ip + ":" + str(self.client_info.port), self.client_info.nickname))
            self.connected = False
            self.server_handler.remove_client(self.client_info.client_socket)
        # [INVITE] - Send client info to client
        elif command == "[INVITE]":
            for client_entry in self.server_handler.connected_clients:
                if client_entry.nickname == data_split[1]:
                    self.client_info.client_socket\
                        .send("[INVITE]^{0}^{1}"
                              .format(client_entry.ip, data_split[1]).encode())
                    return

            # If not found for some reason
            self.client_info.client_socket.send("[INVITEFAILED]".encode())
