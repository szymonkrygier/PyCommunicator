# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
import socket


class ServerSocket:
    def __init__(self):
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def open(self, server_ip, server_port, max_connections):
        try:
            self.socket.bind((server_ip, server_port))
            self.socket.listen(max_connections)
        except socket.error:
            return False

        return True

    def open_port_range(self, server_ip, min_port, max_port, max_connections):
        bind_ok = False
        current_port = min_port

        while not bind_ok and current_port <= max_port:
            try:
                self.socket.bind((server_ip, current_port))
            except socket.error:
                current_port = current_port + 1
                continue

            bind_ok = True
            break

        if not bind_ok:
            return False, 0

        try:
            self.socket.listen(max_connections)
        except socket.error:
            return False, 0

        return True, current_port
