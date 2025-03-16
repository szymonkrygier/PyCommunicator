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

from client.crypto.rsa_crypto import RSACrypto

from client.thread.p2p_server_mode import P2PServerMode

from client.util.invoke_method import InvokeMethod
from client.util.message_box import MessageBox

from common.auth.client_info import ClientInfo

from common.net.server_socket import ServerSocket


class P2PServer(threading.Thread):
    def __init__(self, client):
        super(P2PServer, self).__init__()
        self.server_socket = ServerSocket()
        self.is_running = True
        self.client = client
        self.port = 0
        self.connected_client_handler = None

    def run(self):
        result, opened_port = self.server_socket.open_port_range("", 20010, 20020, 2)
        self.port = opened_port

        while self.is_running:
            client_socket, client_address = self.server_socket.socket.accept()

            # Accept client if client is not talking to someone else
            if self.connected_client_handler is None and not self.client.busy:
                # Get invitation details
                invitation = client_socket.recv(2048).decode().split("^")
                if invitation[0] != "[INVITE]":
                    client_socket.close()
                    return

                # Ask client if he wants to talk
                InvokeMethod(lambda: self.answer_invitation(invitation[1], client_socket, client_address[0],
                                                            client_address[1], invitation[2]))

            # Send info to client that user is talking with someone else
            else:
                client_socket.send("[BUSY]".encode())
                client_socket.close()

    def answer_invitation(self, nickname, client_socket, ip, port, receiver_public_key):
        client_answer = MessageBox.show_message_box_yes_no(
            "Nowe zaproszenie do rozmowy", "Uzytkownik {0} wyslal Ci zaproszenie do rozmowy".
                format(nickname), "Czy chcesz przyjac zaproszenie?")

        # Accept receiver
        if client_answer:
            # Generate public and private key pair
            public_key, private_key = RSACrypto.generate_keys()

            self.client.public_key = public_key
            self.client.private_key = private_key

            client_socket.send("[ACCEPTED]^{0}".format(public_key.decode()).encode())

            client_info = ClientInfo(nickname, ip, port, receiver_public_key,
                                     client_socket)

            self.client.server_mode = True
            self.client.busy = True

            self.client.main_form.btn_send_message.setEnabled(True)
            self.client.main_form.btn_disconnect_from_receiver.setEnabled(True)
            self.client.main_form.btn_send_invitation.setEnabled(False)
            self.client.main_form.lbl_current_receiver.setText(nickname)

            self.connected_client_handler = P2PServerMode(self, client_info)
            self.connected_client_handler.daemon = True
            self.connected_client_handler.start()
        elif not client_answer:
            client_socket.send("[DECLINED]".encode())
            client_socket.close()

    def disconnect_from_receiver(self):
        # Send info to receiver
        try:
            self.connected_client_handler.client_info.client_socket.send("[DISCONNECT]".encode())
        except socket.error:
            pass
        except AttributeError:
            pass

        # Update main form
        InvokeMethod(lambda: self.client.main_form.clear_form())

        self.connected_client_handler.client_info.client_socket.close()
        self.connected_client_handler.connected_to_server = False
        self.connected_client_handler = None

        self.client.busy = False

    def destroy(self):
        self.disconnect_from_receiver()
        self.server_socket.socket.close()
        self.server_socket = None
        self.is_running = False
