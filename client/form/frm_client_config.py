from PySide6.QtWidgets import QWidget

from client.form.frm_client_config_gen import Ui_form_client_config


class FrmClientConfig(QWidget, Ui_form_client_config):
    def __init__(self):
        super(FrmClientConfig, self).__init__()
        self.setupUi(self)
        self.btn_connect.setCheckable(True)
        self.btn_connect.clicked.connect(self.button_clicked)


    def button_clicked(self):
        print("Clicked!")
