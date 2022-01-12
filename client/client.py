# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
import sys

from PySide6.QtWidgets import QApplication

from client.form.frm_client_config import FrmClientConfig

from client.thread.client_listener import ClientListener

from client.thread.p2p_client import P2PClient

from client.thread.p2p_server import P2PServer


class Client:
    def __init__(self):
        super().__init__()
        self.app = None
        self.nickname = None
        self.client_socket = None  # For client-server communication
        self.main_form = None
        self.being_destroyed = False
        self.p2p_client = None
        self.p2p_server = None
        self.server_mode = False
        self.busy = False
        self.init()

    # Client initialization - create app instance, start the event loop
    def init(self):
        # Create QApplication instance
        self.app = QApplication(sys.argv)

        # Load and show configuration window
        frm_client_config = FrmClientConfig(self)
        frm_client_config.show()

        # Start the event loop
        self.app.exec()

    # Client post initialization (after connecting to server) - launch P2P and client listener threads
    def post_init(self):
        client_listener = ClientListener(self)
        client_listener.daemon = True
        client_listener.start()

        self.p2p_client = P2PClient()

        self.p2p_server = P2PServer()
        self.p2p_server.daemon = True
        self.p2p_server.start()

    # Destroy client - close sockets, destroy application
    def destroy(self):
        self.being_destroyed = True

        # Send info to server
        self.client_socket.send_string("[DISCONNECT]")

        self.app.exit()
        exit(0)
