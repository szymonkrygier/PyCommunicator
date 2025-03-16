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
