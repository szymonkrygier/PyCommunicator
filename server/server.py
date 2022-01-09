# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1

from server.thread.server_handler import ServerHandler


class Server:
    def __init__(self, server_ip: str, server_port: int):
        super().__init__()
        self.server_ip = server_ip
        self.server_port = server_port
        self.init()

    def init(self):
        # Start server socket handler
        server_handler = ServerHandler(self.server_ip, self.server_port)
        server_handler.daemon = True
        server_handler.start()

        server_handler.join()
