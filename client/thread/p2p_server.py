# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
import socket

import threading


class P2PServer(threading.Thread):
    def __init__(self):
        super(P2PServer, self).__init__()
