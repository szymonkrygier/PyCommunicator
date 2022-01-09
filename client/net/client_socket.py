# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
import socket


class ClientSocket:
    def __init__(self):
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, server_ip, server_port):
        try:
            self.socket.connect((server_ip, server_port))
        except socket.error:
            return False

        return True

    def disconnect(self):
        self.socket.close()

    def send_stream(self, data):
        self.socket.send(data)
