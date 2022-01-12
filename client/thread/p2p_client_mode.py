# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
from datetime import datetime

import threading

import socket


class P2PClientMode(threading.Thread):
    def __init__(self, client_info):
        super(P2PClientMode, self).__init__()
        self.client_info = client_info
        self.connected_to_receiver = True

    def run(self):
        # Setup form
        while self.connected_to_receiver:
            try:
                received_data = self.client_info.client_socket.recv(2048)
            except socket.error:
                self.connected_to_receiver = False
                self.client_info.socket.close()
                return

            self.process_data_from_receiver(received_data.decode())

    def process_data_from_receiver(self, data):
        data_split = data.decode().split("^")
        command = data_split[0]

        # [MSG] - Received message
        if command == "[MSG]":
            now = datetime.now()
            message = data_split[1]

            self.p2p_server.client.main_form.list_messages.addItem("[{0}][{1}] > {2}"
                                                                   .format(self.client_info.nickname,
                                                                           now.strftime("%Y-%m-%d %H:%M"), message))
