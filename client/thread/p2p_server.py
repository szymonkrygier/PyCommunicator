# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
import socket

import threading

from PySide6.QtWidgets import QMessageBox

from client.thread.p2p_server_mode import P2PServerMode

from common.auth.client_info import ClientInfo

from common.net.server_socket import ServerSocket


class P2PServer(threading.Thread):
    def __init__(self, client):
        super(P2PServer, self).__init__()
        self.server_socket = ServerSocket()
        self.is_connected = True
        self.client = client
        self.connected_client_handler = None

    def run(self):
        self.server_socket.open("", 20009, 2)

        while self.is_connected:
            client_socket, client_address = self.server_socket.socket.accept()

            # Accept client if client is not talking to someone else
            if self.connected_client_handler is None and not self.client.busy:
                # Get invitation details
                invitation = self.server_socket.socket.recv(2048).decode().split("^")
                if invitation[0] != "[INVITE]":
                    client_socket.close()
                    return

                # Ask client if he wants to talk
                message_box = QMessageBox
                message_box.setWindowTitle("Nowe zaproszenie do rozmowy")
                message_box.setText("Uzytkownik {0} wyslal Ci zaproszenie do rozmowy".format(invitation[1]))
                message_box.setInformativeText("Czy chcesz przyjac zaproszenie?")
                message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                message_box.setDefaultButton(QMessageBox.Yes)
                message_box_result = message_box.exec()

                # Accept receiver
                if message_box_result == QMessageBox.Yes:
                    client_socket.send("[ACCEPTED]^{0}".encode())

                    client_info = ClientInfo(invitation[1], client_address[0], client_address[1], invitation[2],
                                             client_socket)

                    self.client.server_mode = True
                    self.client.busy = True

                    self.connected_client_handler = P2PServerMode(self, client_info)
                    self.connected_client_handler.daemon = True
                    self.connected_client_handler.start()
                elif message_box_result == QMessageBox.No:
                    client_socket.send("[DECLINED]".encode())
                    client_socket.close()

            # Send info to client that user is talking with someone else
            else:
                client_socket.send("[BUSY]".encode())
                client_socket.close()
