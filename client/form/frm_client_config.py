# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
from PySide6.QtWidgets import QWidget, QMessageBox

from client.form.frm_client_config_gen import Ui_form_client_config

from client.form.frm_main import FrmMain

from client.net.client_socket import ClientSocket

from client.util.message_box import MessageBox


class FrmClientConfig(QWidget, Ui_form_client_config):
    def __init__(self, client):
        super(FrmClientConfig, self).__init__()
        self.setupUi(self)
        self.client = client

        # btn_connect
        self.btn_connect.clicked.connect(self.button_clicked)

    def button_clicked(self):
        # Get user input
        nickname = self.tb_nick.text()
        server_ip = self.tb_server_ip.text()
        server_port = self.tb_server_port.text()

        # Check user input
        if not nickname or not server_ip or not server_port:
            MessageBox.show_message_box("Brak wymaganych danych", "Uzupelnij wszystkie wymagane dane!")
            return

        # Validate nickname
        if nickname.__contains__('^'):
            MessageBox.show_message_box("Niepoprawny nickname", "Nick zawiera niedozwolony znak: '^'")
            return

        # Connect to server
        self.client.client_socket = ClientSocket(self.client)
        if not self.client.client_socket.connect(server_ip, int(server_port)):
            MessageBox.show_message_box("Blad polaczenia z serwerem",
                                        "Blad polaczenia z serwerem {0}. Upewnij sie, ze adres IP oraz port sa poprawne"
                                        .format(str(server_ip + ":" + str(server_port))))
            return

        # Authenticate client
        self.client.client_socket.send_string("[AUTH]^{0}".format(nickname))
        received_data = self.client.client_socket.receive_string()

        # Check response
        if received_data.startswith("[NAMETAKEN]"):
            MessageBox.show_message_box("Nickname jest zajety", "Nick {0} jest juz zajety! Uzyj innego nicku.".
                                        format(nickname))
            self.client.client_socket.socket.shutdown()
            return
        elif received_data.startswith("[AUTHENTICATED]"):
            self.client.nickname = nickname
            self.hide()
            self.client.main_form = FrmMain(self.client)
            self.client.main_form.show()
            self.client.post_init()
        else:
            return
