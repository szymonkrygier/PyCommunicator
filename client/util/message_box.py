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
from PySide6.QtWidgets import QMessageBox


class MessageBox:
    @staticmethod
    def show_message_box(title, message):
        message_box = QMessageBox()
        message_box.setWindowTitle(title)
        message_box.setText(message)
        message_box.exec()

    @staticmethod
    def show_message_box_yes_no(title, message, informative):
        message_box = QMessageBox()
        message_box.setWindowTitle(title)
        message_box.setText(message)
        message_box.setInformativeText(informative)
        message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        message_box.setDefaultButton(QMessageBox.Yes)
        message_box_result = message_box.exec()

        if message_box_result == QMessageBox.Yes:
            return True
        else:
            return False
