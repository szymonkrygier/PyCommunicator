# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
import socket
import threading

from common.auth.client_info import ClientInfo

from common.net.server_socket import ServerSocket

from server.thread.client_handler import ClientHandler


class ServerHandler(threading.Thread):
    MAX_CONNECTIONS = 20

    def __init__(self, server_ip: str, server_port: int):
        super(ServerHandler, self).__init__()
        self.connected_clients = []
        self.server_socket = ServerSocket()
        self.server_ip = server_ip
        self.server_port = server_port

    def run(self):
        # Open server socket
        try:
            self.server_socket.open(self.server_ip, self.server_port, ServerHandler.MAX_CONNECTIONS)
        except socket.error:
            print("Nie mozna otworzyc serwera pod adresem {0}".format(str(self.server_ip + ":" + self.server_port)))
            exit(1)

        print("Serwer zostal otworzony pod adresem {0}".format(str(self.server_ip + ":" + self.server_port)))

        # Handler loop
        while True:
            client_socket, client_address = self.server_socket.socket.accept()

            client_info = ClientInfo("", client_address, "")

            self.connected_clients.append(client_info)
            client_thread = ClientHandler(client_socket, client_info)
            client_thread.daemon = True
            client_thread.start()
