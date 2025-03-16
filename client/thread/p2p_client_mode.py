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
from datetime import datetime

import threading

import socket

from client.crypto.rsa_crypto import RSACrypto

from client.util.invoke_method import InvokeMethod


class P2PClientMode(threading.Thread):
    def __init__(self, p2p_client, client_info):
        super(P2PClientMode, self).__init__()
        self.p2p_client = p2p_client
        self.client_info = client_info
        self.connected_to_receiver = True

    def run(self):
        while self.connected_to_receiver:
            try:
                received_data = self.p2p_client.socket.recv(2048)
            except socket.error:
                self.p2p_client.disconnect_from_receiver()
                self.connected_to_receiver = False
                self.p2p_client.socket.close()
                return

            self.process_data_from_receiver(received_data)

    def process_data_from_receiver(self, data):
        data_split = data.decode().split("^")
        command = data_split[0]

        # [MSG] - Received message
        if command == "[MSG]":
            now = datetime.now()
            message = data_split[1]

            decrypted_message = RSACrypto.decrypt(message, self.p2p_client.client.private_key)

            InvokeMethod(lambda: self.p2p_client.client.main_form.list_messages.addItem("[{0}][{1}] > {2}"
                                                                   .format(self.client_info.nickname,
                                                                           now.strftime("%Y-%m-%d %H:%M"),
                                                                           decrypted_message.decode())))
        # [DISCONNECT] - Receiver disconnected
        if command == "[DISCONNECT]":
            self.p2p_client.disconnect_from_receiver()
