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
import base64
import socket

from client.crypto.rsa_crypto import RSACrypto

from client.thread.p2p_client_mode import P2PClientMode

from client.util.invoke_method import InvokeMethod

from client.util.message_box import MessageBox

from common.auth.client_info import ClientInfo


class P2PClient:
    def __init__(self, client):
        super().__init__()
        self.client = client
        self.socket = None
        self.connected_to_receiver = False
        self.connected_server_handler = None
        self.match_port = 20010

    def __try_port_range(self, ip, port_min, port_max, receiver):
        connected = False
        current_port = port_min
        hostname = socket.gethostname()

        while not connected and current_port <= port_max:
            if current_port == self.client.p2p_server.port and (str(socket.gethostbyname(hostname)) == ip
                                                                or ip == "127.0.0.1" or ip == "0.0.0.0"
                                                                or ip == "localhost"):
                current_port = current_port + 1
                continue

            try:
                self.socket.connect((ip, current_port))
            except socket.error:
                current_port = current_port + 1
                continue

            connected = True
            break

        if not connected:
            self.socket.close()
            MessageBox.show_message_box("Zaproszenie nie zostalo wyslane", "Uzytkownik {0} nie jest osiagalny!"
                                        .format(receiver))
            return

        self.match_port = current_port

    def send_invitation(self, ip, receiver):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.__try_port_range(ip, 20010, 20020, receiver)

        # Generate public and private key pair
        public_key, private_key = RSACrypto.generate_keys()

        self.client.public_key = public_key
        self.client.private_key = private_key

        # Send invitation and get response
        self.socket.send("[INVITE]^{0}^{1}".format(self.client.nickname, public_key.decode()).encode())

        received_data = self.socket.recv(2048).decode()

        if received_data.startswith("[BUSY]"):
            InvokeMethod(lambda: MessageBox.show_message_box("Uzytkownik jest zajety",
                                                             "Uzytkownik {0} rozmawia aktualnie z kims innym!"
                                                             .format(receiver)))
            self.client.main_form.btn_send_invitation(True)
            self.socket.close()
            self.socket = None
            return
        elif received_data.startswith("[DECLINED]"):
            InvokeMethod(lambda: MessageBox.show_message_box("Uzytkownik odrzucil zaproszenie",
                                                             "Uzytkownik {0} odrzucil Twoje zaproszenie!"
                                                             .format(receiver)))
            self.client.main_form.btn_send_invitation(True)
            self.socket.close()
            self.socket = None
            return
        elif received_data.startswith("[ACCEPTED]"):
            data_split = received_data.split("^")

            self.connected_to_receiver = True

            self.client.main_form.btn_send_message.setEnabled(True)
            self.client.main_form.btn_disconnect_from_receiver.setEnabled(True)
            self.client.main_form.btn_send_invitation.setEnabled(False)
            self.client.main_form.lbl_current_receiver.setText(receiver)

            self.client.busy = True
            self.client.server_mode = False

            client_info = ClientInfo(receiver, ip, self.match_port, data_split[1], None)

            self.connected_server_handler = P2PClientMode(self, client_info)
            self.connected_server_handler.daemon = True
            self.connected_server_handler.start()
        else:
            return

    def disconnect_from_receiver(self):
        # Update main form
        InvokeMethod(lambda: self.client.main_form.clear_form())

        self.client.busy = False

        # Send info to receiver
        try:
            self.socket.send("[DISCONNECT]".encode())
        except socket.error:
            pass

        self.connected_to_receiver = False
        self.connected_server_handler.connected_to_receiver = False
        self.connected_server_handler = None
        self.socket.close()
        self.socket = None
