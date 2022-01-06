from PySide6.QtWidgets import QMainWindow

from client.form.frm_main_gen import Ui_MainWindow


class FrmMain(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(FrmMain, self).__init__()
        self.setupUi(self)
