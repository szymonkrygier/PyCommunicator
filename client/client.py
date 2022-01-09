# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
import sys

from PySide6.QtWidgets import QApplication

from client.form.frm_client_config import FrmClientConfig


class Client:
    def __init__(self):
        super().__init__()
        self.init()


    def init(self):
        # Create QApplication instance
        app = QApplication(sys.argv)

        # Load and show configuration window
        frm_client_config = FrmClientConfig()
        frm_client_config.show()

        # Start the event loop
        app.exec()
