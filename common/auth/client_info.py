# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
from dataclasses import dataclass

import socket


@dataclass
class ClientInfo:
    nickname: str
    ip: str
    port: int
    public_key: str
    client_socket: socket
