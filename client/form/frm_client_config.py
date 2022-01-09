# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
from PySide6.QtWidgets import QWidget, QMessageBox

from client.form.frm_client_config_gen import Ui_form_client_config


class FrmClientConfig(QWidget, Ui_form_client_config):
    def __init__(self):
        super(FrmClientConfig, self).__init__()
        self.nickname = None
        self.server_ip = None
        self.server_port = None
        self.setupUi(self)

        # btn_connect
        self.btn_connect.clicked.connect(self.button_clicked)

    def button_clicked(self):
        # Get user input
        self.nickname = self.tb_nick.text()
        self.server_ip = self.tb_server_ip.text()
        self.server_port = self.tb_server_port.text()

        # Check user input
        if not self.nickname or not self.server_ip or not self.server_port:
            message_box = QMessageBox()
            message_box.setWindowTitle("Brak wymaganych danych")
            message_box.setText("Uzupelnij wszystkie wymagane dane!")
            message_box.exec()
            return

        if self.nickname.__contains__('^'):
            message_box = QMessageBox()
            message_box.setWindowTitle("Niepoprawny nickname")
            message_box.setText("Nick zawiera niedozwolony znak: '^'")
            message_box.exec()
            return
