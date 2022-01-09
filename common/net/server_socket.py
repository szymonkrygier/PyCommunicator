# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
import socket


class ServerSocket:
    def __init__(self):
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def open(self, server_ip, server_port, max_connections):
        self.socket.bind((server_ip, server_port))
        self.socket.listen(max_connections)
