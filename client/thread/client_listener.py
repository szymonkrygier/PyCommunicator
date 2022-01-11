# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
import threading


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
