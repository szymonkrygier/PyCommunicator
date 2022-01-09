# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
from typing import NamedTuple

class ClientInfo(NamedTuple):
    nickname: str
    address: str
    public_key: str
