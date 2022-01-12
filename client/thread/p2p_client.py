# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
import socket

from client.thread.p2p_client_mode import P2PClientMode

from client.util.message_box import MessageBox

from common.auth.client_info import ClientInfo


class P2PClient:
    def __init__(self, client):
        super().__init__()
        self.client = client
        self.socket = None
        self.connected_to_receiver = False
        self.connected_server_handler = None

    def send_invitation(self, ip, port, receiver):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.socket.connect((ip, port))
        except socket.error:
            self.socket.close()
            MessageBox.show_message_box("Zaproszenie nie zostalo wyslane", "Uzytkownik {0} nie jest osiagalny!"
                                        .format(receiver))
            return

        # Send invitation and get response
        self.socket.send("[INVITE]^{0}^{1}".format(self.client.nickname, "publickey").encode())

        received_data = self.socket.recv(2048).decode()

        if received_data.startswith("[BUSY]"):
            MessageBox.show_message_box("Uzytkownik jest zajety", "Uzytkownik {0} rozmawia aktualnie z kims innym!"
                                        .format(receiver))
            self.client.main_form.btn_send_invitation(True)
            self.socket.close()
            self.socket = None
            return
        elif received_data.startswith("[DECLINED]"):
            MessageBox.show_message_box("Uzytkownik odrzucil zaproszenie", "Uzytkownik {0} odrzucil Twoje zaproszenie!"
                                        .format(receiver))
            self.client.main_form.btn_send_invitation(True)
            self.socket.close()
            self.socket = None
            return
        elif received_data.startswith("ACCEPTED"):
            data_split = received_data.split("^")

            self.connected_to_receiver = True

            self.client.main_form.btn_send_message.setEnabled(True)
            self.client.main_form.btn_disconnect_from_receiver.setEnabled(True)
            self.client.main_form.btn_send_invitation(False)
            self.client.main_form.lbl_current_receiver.setText(receiver)

            self.client.busy = True
            self.client.server_mode = False

            client_info = ClientInfo(receiver, ip, port, data_split[1], self.socket)

            self.connected_server_handler = P2PClientMode(client_info)
            self.connected_server_handler.daemon = True
            self.connected_server_handler.start()
        else:
            return

    def disconnect_from_receiver(self):
        self.client.main_form.btn_send_message.setEnabled(False)
        self.client.main_form.btn_disconnect_from_receiver.setEnabled(False)
        self.client.main_form.btn_send_invitation(True)
        self.client.main_form.lbl_current_receiver.setText("BRAK ROZMOWCY")

        try:
            self.socket.send("[DISCONNECT]".encode())
        except socket.error:
            pass

        self.socket.close()
        self.socket = None
        self.client.busy = False
