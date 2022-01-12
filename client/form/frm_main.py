# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
from datetime import datetime

from PySide6.QtWidgets import QMainWindow

from client.form.frm_main_gen import Ui_MainWindow

from client.util.message_box import MessageBox


class FrmMain(QMainWindow, Ui_MainWindow):
    def __init__(self, client):
        super(FrmMain, self).__init__()
        self.setupUi(self)
        self.client = client

        # Define events
        self.closeEvent = self.form_closing

        # Set labels
        self.lbl_nickname.setText(self.client.nickname)
        self.lbl_server_status.setText("CONNECTED")

        # Setup buttons
        self.btn_send_message.setEnabled(False)
        self.btn_disconnect_from_receiver.setEnabled(False)

        self.btn_send_invitation.clicked.connect(self.send_invitation)
        self.btn_send_message.clicked.connect(self.send_message)

    def form_closing(self, event):
        self.client.destroy()

    def send_invitation(self):
        if len(self.list_available_users.selectedItems()) != 1:
            MessageBox.show_message_box("Blad przy wysylaniu zaproszenia", "Wybierz tylko jednego rozmowce z listy!")
            return

        self.btn_send_invitation.setEnabled(False)

        # Ask server about receiver IP and port
        self.client.client_socket.send_string("[INVITE]^{0}".format(self.list_available_users.selectedItems[0]))

    def send_message(self):
        now = datetime.now()

        stream = "[MSG]^{0}".format(self.tb_message.text())

        if self.client.server_mode:
            self.client.p2p_server.server_socket.socket.send(stream.encode())
        elif not self.client.server_mode:
            self.client.p2p_client.socket.send(stream.encode())

        self.list_messages.addItem("[JA][{0}] > {1}".format(now.strftime("%Y-%m-%d %H:%M"), self.tb_message.text()))

        self.tb_message.clear()
