# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
from PySide6.QtWidgets import QMainWindow

from client.form.frm_main_gen import Ui_MainWindow


class FrmMain(QMainWindow, Ui_MainWindow):
    def __init__(self, client):
        super(FrmMain, self).__init__()
        self.setupUi(self)
        self.client = client

        # Define events
        self.closeEvent = self.form_closing

        # Set nickname
        self.lbl_nickname.setText(self.client.nickname)

    def form_closing(self, event):
        self.client.destroy()
