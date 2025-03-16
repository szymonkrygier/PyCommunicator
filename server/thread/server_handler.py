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
import socket
import threading

from common.auth.client_info import ClientInfo

from common.net.server_socket import ServerSocket

from common.util.logger import Logger

from server.thread.client_handler import ClientHandler


class ServerHandler(threading.Thread):
    MAX_CONNECTIONS = 10  # Max client count

    def __init__(self, server_ip: str, server_port: int):
        super(ServerHandler, self).__init__()
        self.connected_clients = []  # All connected clients
        self.server_socket = ServerSocket()
        self.server_ip = server_ip
        self.server_port = server_port

    def run(self):
        # Open server socket
        try:
            self.server_socket.open(self.server_ip, self.server_port, ServerHandler.MAX_CONNECTIONS)
        except socket.error:
            Logger.log("Nie mozna otworzyc serwera pod adresem {0}".format(str(self.server_ip + ":" +
                                                                               str(self.server_port))))
            exit(1)

        Logger.log("Serwer zostal otworzony pod adresem {0}".format(str(self.server_ip + ":" + str(self.server_port))))

        # Handler loop
        while True:
            client_socket, client_address = self.server_socket.socket.accept()
            Logger.log("Nowe polaczenie klienta z adresu {0}".format(client_address[0] + ":" + str(client_address[1])))

            client_info = ClientInfo("", client_address[0], client_address[1], "", client_socket)

            self.connected_clients.append(client_info)
            client_thread = ClientHandler(self, client_info)
            client_thread.daemon = True
            client_thread.start()

    def remove_client(self, client_socket: socket):
        for client in self.connected_clients:
            if client.client_socket == client_socket:
                self.connected_clients.remove(client)
                Logger.log("Klient o adresie {0} i nicku {1} zostal usuniety z serwera".format(
                    client.ip + ":" + str(client.port), client.nickname))

                # Send list of connected users to all clients
                self.send_available_users()
                break

    def send_string_to_all_users(self, data):
        for client in self.connected_clients:
            if client.nickname != "":
                client.client_socket.send(data)

    def send_available_users(self):
        available_users = ""

        for client in self.connected_clients:
            if client.nickname != "":
                available_users = available_users + "^" + client.nickname

        self.send_string_to_all_users(("[AVAILABLE]" + available_users).encode())
