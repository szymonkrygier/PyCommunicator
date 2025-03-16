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
import signal

from common.util.logger import Logger

from server.thread.server_handler import ServerHandler


class Server:
    def __init__(self, server_ip: str, server_port: int):
        super().__init__()
        self.server_ip = server_ip
        self.server_port = server_port
        self.server_handler = None

        # Set signal handlers
        signal.signal(signal.SIGINT, self.handle_signal)
        signal.signal(signal.SIGTERM, self.handle_signal)

        # Init server
        self.init()

    def init(self):
        # Start server socket handler
        self.server_handler = ServerHandler(self.server_ip, self.server_port)
        self.server_handler.daemon = True
        self.server_handler.start()

        self.server_handler.join()

    def handle_signal(self):
        self.destroy()

    def destroy(self):
        Logger.log("Server is being destroyed...")

        # Send info to all clients
        self.server_handler.send_string_to_all_users("[SERVERCLOSING]")

        Logger.log("Server destroyed. Closing application.")
        exit(0)
