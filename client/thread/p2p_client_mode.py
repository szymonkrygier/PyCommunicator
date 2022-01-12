# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
from datetime import datetime

import threading

import socket

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

        print("Received data:{0}".format(data))

        # [MSG] - Received message
        if command == "[MSG]":
            now = datetime.now()
            message = data_split[1]

            InvokeMethod(self.p2p_client.client.main_form.list_messages.addItem("[{0}][{1}] > {2}"
                                                                   .format(self.client_info.nickname,
                                                                           now.strftime("%Y-%m-%d %H:%M"), message)))
        # [DISCONNECT] - Receiver disconnected
        if command == "[DISCONNECT]":
            self.p2p_client.disconnect_from_receiver()
