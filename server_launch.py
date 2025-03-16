# PyCommunicator
# Copyright (C) 2022-2025 Szymon Krygier <szymon.krygier@pulsax.pl>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
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
