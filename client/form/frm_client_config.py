from PySide6.QtWidgets import QWidget, QMessageBox

from client.form.frm_client_config_gen import Ui_form_client_config


class FrmClientConfig(QWidget, Ui_form_client_config):
    def __init__(self):
        super(FrmClientConfig, self).__init__()
        self.setupUi(self)

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
