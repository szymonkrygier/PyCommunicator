# PyCommunicator
# Copyright (C) 2022-2025 Szymon Krygier <szymon.krygier@pulsax.pl>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import base64

from datetime import datetime

from PySide6.QtWidgets import QMainWindow

from client.crypto.rsa_crypto import RSACrypto

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
        self.btn_disconnect_from_receiver.clicked.connect(self.disconnect_from_receiver)

    def form_closing(self, event):
        self.client.destroy()

    def send_invitation(self):
        if len(self.list_available_users.selectedItems()) != 1:
            MessageBox.show_message_box("Blad przy wysylaniu zaproszenia", "Wybierz tylko jednego rozmowce z listy!")
            return

        self.btn_send_invitation.setEnabled(False)

        # Ask server about receiver IP and port
        selected_items = self.list_available_users.selectedItems()
        self.client.client_socket.send_string("[INVITE]^{0}".format(selected_items[0].text()))

    def send_message(self):
        if self.tb_message.text() == "":
            return

        now = datetime.now()

        public_key = None

        if self.client.server_mode:
            public_key = self.client.p2p_server.connected_client_handler.client_info.public_key
        elif not self.client.server_mode:
            public_key = self.client.p2p_client.connected_server_handler.client_info.public_key

        encrypted_message = RSACrypto.encrypt(self.tb_message.text().encode(), public_key)

        self.list_messages.addItem("[JA][{0}] > {1}".format(now.strftime("%Y-%m-%d %H:%M"), self.tb_message.text()))

        stream = "[MSG]^{0}".format(encrypted_message)

        self.tb_message.clear()

        if self.client.server_mode:
            self.client.p2p_server.connected_client_handler.client_info.client_socket.send(stream.encode())
        elif not self.client.server_mode:
            self.client.p2p_client.socket.send(stream.encode())

    def clear_form(self):
        self.client.main_form.list_messages.clear()
        self.client.main_form.btn_send_message.setEnabled(False)
        self.client.main_form.btn_disconnect_from_receiver.setEnabled(False)
        self.client.main_form.btn_send_invitation.setEnabled(True)
        self.client.main_form.lbl_current_receiver.setText("BRAK ROZMOWCY")

    def disconnect_from_receiver(self):
        if self.client.server_mode:
            self.client.p2p_server.disconnect_from_receiver()
        elif not self.client.server_mode:
            self.client.p2p_client.disconnect_from_receiver()
