# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
import socket

from PySide6.QtWidgets import QMessageBox


class ClientSocket:
    def __init__(self, client):
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client = client

    def connect(self, server_ip, server_port):
        try:
            self.socket.connect((server_ip, server_port))
        except socket.error:
            return False

        return True

    def disconnect(self):
        self.socket.close()

    def send_string(self, data: str):
        try:
            self.socket.send(data.encode())
        except socket.error:
            # Destroy application
            if not self.client.being_destroyed:
                # Show info to user
                message_box = QMessageBox()
                message_box.setWindowTitle("Utracono polaczenie z serwerem!")
                message_box.setText("Utracono polaczenie z serwerem. Aplikacja zostanie zamknieta.")
                message_box.exec()

                # Destroy client
                self.client.destroy()

    def receive_string(self):
        return self.socket.recv(2048).decode()
