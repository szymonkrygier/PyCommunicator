# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
import common.check_runtime

import sys

from server.server import Server


def run():
    if len(sys.argv) != 3:
        print("Niepoprawne argumenty! Poprawne uzycie: server_launch.py ip_serwera port_serwera")
        exit(1)

    server_instance = Server(sys.argv[1], int(sys.argv[2]))


if __name__ == "__main__":
    run()
