# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
from PySide6.QtWidgets import QWidget, QMessageBox

from client.form.frm_client_config_gen import Ui_form_client_config

from client.form.frm_main import FrmMain

from client.net.client_socket import ClientSocket


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
            message_box = QMessageBox()
            message_box.setWindowTitle("Brak wymaganych danych")
            message_box.setText("Uzupelnij wszystkie wymagane dane!")
            message_box.exec()
            return

        # Validate nickname
        if nickname.__contains__('^'):
            message_box = QMessageBox()
            message_box.setWindowTitle("Niepoprawny nickname")
            message_box.setText("Nick zawiera niedozwolony znak: '^'")
            message_box.exec()
            return

        # Connect to server
        self.client.client_socket = ClientSocket()
        if not self.client.client_socket.connect(server_ip, int(server_port)):
            message_box = QMessageBox()
            message_box.setWindowTitle("Blad polaczenia z serwerem")
            message_box.setText("Blad polaczenia z serwerem {0}. Upewnij sie, ze adres IP oraz port sa poprawne".format(str(server_ip + ":" + str(server_port))))
            message_box.exec()
            return

        # Authenticate client
        self.client.client_socket.send_string("[AUTH]^{0}".format(nickname))
        received_data = self.client.client_socket.receive_string()

        # Check response
        if received_data.startswith("[NAMETAKEN]"):
            message_box = QMessageBox()
            message_box.setWindowTitle("Nickname jest zajety")
            message_box.setText("Nick {0} jest juz zajety! Uzyj innego nicku.".format(nickname))
            message_box.exec()
            self.client.client_socket.socket.shutdown()
            return
        elif received_data.startswith("[AUTHENTICATED]"):
            self.client.nickname = nickname
            self.hide()
            self.client.main_form = FrmMain(self.client)
            self.client.main_form.show()
        else:
            return
