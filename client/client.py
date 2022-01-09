# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
import sys

from PySide6.QtWidgets import QApplication

from client.form.frm_client_config import FrmClientConfig


class Client:
    INSTANCE = None

    def __init__(self):
        super().__init__()
        self.app = None
        self.init()

    def init(self):
        # Check if instance already exists
        if Client.INSTANCE is not None:
            print("Instancja klienta jest juz uruchomiona!")

        # Set global INSTANCE variable to self
        Client.INSTANCE = self

        # Create QApplication instance
        self.app = QApplication(sys.argv)

        # Load and show configuration window
        frm_client_config = FrmClientConfig()
        frm_client_config.show()

        # Start the event loop
        self.app.exec()
