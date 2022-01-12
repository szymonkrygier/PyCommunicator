# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
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
