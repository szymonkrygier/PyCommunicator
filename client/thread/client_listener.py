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

from PySide6.QtWidgets import QMessageBox

from client.util.message_box import MessageBox


class ClientListener(threading.Thread):
    def __init__(self, client):
        super(ClientListener, self).__init__()
        self.client = client

    def run(self):
        # Client listener loop
        while True:
            received_data = self.client.client_socket.receive_string()
            self.parse_data_from_server(received_data)

    def parse_data_from_server(self, data):
        data_split = data.split("^")
        command = data_split[0]

        # [AVAILABLE] - Receive list with available users
        if command == "[AVAILABLE]":
            self.client.main_form.list_available_users.clear()

            for available_user in data_split:
                if available_user == command or available_user == self.client.nickname:
                    continue
                self.client.main_form.list_available_users.addItem(available_user)
        # [SERVERCLOSING] - Handle server closing event
        elif command == "[SERVERCLOSING]":
            MessageBox.show_message_box("Utracono polaczenie z serwerem!",
                                        "Serwer zostal zamkniety. Aplikacja zostanie zamknieta!")
            self.client.destroy()
        # [INVITEFAILED] - Server could not return client info
        elif command == "[INVITEFAILED]":
            MessageBox.show_message_box("Nie mozna wyslac zaproszenia",
                                        "Nie mozna wyslac zaproszenia do rozmowcy. Serwer nie zwrocil danych odbiorcy!")
            self.client.main_form.btn_send_invitation.setEnabled(True)
        # [INVITE] - Receive client info from server
        elif command == "[INVITE]":
            self.client.p2p_client.send_invitation(data_split[1], data_split[2])
