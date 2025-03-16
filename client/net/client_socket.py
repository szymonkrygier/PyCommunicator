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
        received_data = ""

        try:
            received_data = self.socket.recv(2048).decode()
        except socket.error:
            message_box = QMessageBox()
            message_box.setWindowTitle("Utracono polaczenie z serwerem!")
            message_box.setText("Wystapil blad przy odbieraniu danych. Prawdopodobnie serwer zostal zamkniety."
                                " Aplikacja zostanie zamknieta.")
            message_box.exec()
            self.client.destroy()

        return received_data
