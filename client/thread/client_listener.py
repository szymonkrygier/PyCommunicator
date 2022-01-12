# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
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
