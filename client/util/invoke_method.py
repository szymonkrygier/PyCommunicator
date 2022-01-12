# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
from typing import Callable

from PySide6.QtCore import QObject, Signal, Slot

from PySide6.QtGui import QGuiApplication


class InvokeMethod(QObject):
    def __init__(self, method: Callable):
        super().__init__()

        main_thread = QGuiApplication.instance().thread()
        self.moveToThread(main_thread)
        self.setParent(QGuiApplication.instance())
        self.method = method
        self.called.connect(self.execute)
        self.called.emit()

    called = Signal()

    @Slot()
    def execute(self):
        self.method()
        self.setParent(None)
