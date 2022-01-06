# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QListView, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1061, 625)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.list_available_users = QListView(self.centralwidget)
        self.list_available_users.setObjectName(u"list_available_users")
        self.list_available_users.setGeometry(QRect(10, 40, 241, 241))
        self.lbl_available_users = QLabel(self.centralwidget)
        self.lbl_available_users.setObjectName(u"lbl_available_users")
        self.lbl_available_users.setGeometry(QRect(10, 10, 241, 21))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lbl_available_users.setFont(font)
        self.list_messages = QListView(self.centralwidget)
        self.list_messages.setObjectName(u"list_messages")
        self.list_messages.setGeometry(QRect(260, 40, 791, 471))
        self.tb_message = QLineEdit(self.centralwidget)
        self.tb_message.setObjectName(u"tb_message")
        self.tb_message.setGeometry(QRect(260, 520, 681, 22))
        self.btn_send_message = QPushButton(self.centralwidget)
        self.btn_send_message.setObjectName(u"btn_send_message")
        self.btn_send_message.setGeometry(QRect(950, 520, 101, 24))
        self.gb_status = QGroupBox(self.centralwidget)
        self.gb_status.setObjectName(u"gb_status")
        self.gb_status.setGeometry(QRect(10, 350, 241, 191))
        self.gb_status.setFont(font)
        self.lbl_server_status_title = QLabel(self.gb_status)
        self.lbl_server_status_title.setObjectName(u"lbl_server_status_title")
        self.lbl_server_status_title.setGeometry(QRect(10, 80, 201, 21))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        self.lbl_server_status_title.setFont(font1)
        self.lbl_server_status = QLabel(self.gb_status)
        self.lbl_server_status.setObjectName(u"lbl_server_status")
        self.lbl_server_status.setGeometry(QRect(10, 100, 141, 21))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(False)
        self.lbl_server_status.setFont(font2)
        self.lbl_current_receiver = QLabel(self.gb_status)
        self.lbl_current_receiver.setObjectName(u"lbl_current_receiver")
        self.lbl_current_receiver.setGeometry(QRect(10, 150, 221, 21))
        self.lbl_current_receiver.setFont(font2)
        self.lbl_current_receiver_title = QLabel(self.gb_status)
        self.lbl_current_receiver_title.setObjectName(u"lbl_current_receiver_title")
        self.lbl_current_receiver_title.setGeometry(QRect(10, 130, 141, 21))
        self.lbl_current_receiver_title.setFont(font1)
        self.lbl_nickname = QLabel(self.gb_status)
        self.lbl_nickname.setObjectName(u"lbl_nickname")
        self.lbl_nickname.setGeometry(QRect(10, 50, 141, 21))
        self.lbl_nickname.setFont(font2)
        self.lbl_nickname_title = QLabel(self.gb_status)
        self.lbl_nickname_title.setObjectName(u"lbl_nickname_title")
        self.lbl_nickname_title.setGeometry(QRect(10, 30, 201, 21))
        self.lbl_nickname_title.setFont(font1)
        self.btn_send_invitation = QPushButton(self.centralwidget)
        self.btn_send_invitation.setObjectName(u"btn_send_invitation")
        self.btn_send_invitation.setGeometry(QRect(10, 290, 241, 24))
        self.lbl_autor = QLabel(self.centralwidget)
        self.lbl_autor.setObjectName(u"lbl_autor")
        self.lbl_autor.setGeometry(QRect(10, 560, 151, 16))
        self.lbl_chatbox = QLabel(self.centralwidget)
        self.lbl_chatbox.setObjectName(u"lbl_chatbox")
        self.lbl_chatbox.setGeometry(QRect(260, 10, 241, 21))
        self.lbl_chatbox.setFont(font)
        self.btn_disconnect_from_receiver = QPushButton(self.centralwidget)
        self.btn_disconnect_from_receiver.setObjectName(u"btn_disconnect_from_receiver")
        self.btn_disconnect_from_receiver.setGeometry(QRect(10, 320, 241, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1061, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_available_users.setText(QCoreApplication.translate("MainWindow", u"Dost\u0119pni u\u017cytkownicy", None))
        self.btn_send_message.setText(QCoreApplication.translate("MainWindow", u"Wy\u015blij", None))
        self.gb_status.setTitle(QCoreApplication.translate("MainWindow", u"Status", None))
        self.lbl_server_status_title.setText(QCoreApplication.translate("MainWindow", u"Po\u0142\u0105czenie z serwerem centralnym:", None))
        self.lbl_server_status.setText(QCoreApplication.translate("MainWindow", u"Niepod\u0142\u0105czony", None))
        self.lbl_current_receiver.setText(QCoreApplication.translate("MainWindow", u"BRAK ROZM\u00d3WCY", None))
        self.lbl_current_receiver_title.setText(QCoreApplication.translate("MainWindow", u"Obecnie rozmawiasz z:", None))
        self.lbl_nickname.setText(QCoreApplication.translate("MainWindow", u"Unknown", None))
        self.lbl_nickname_title.setText(QCoreApplication.translate("MainWindow", u"Nazwa wy\u015bwietlana:", None))
        self.btn_send_invitation.setText(QCoreApplication.translate("MainWindow", u"Wy\u015blij zaproszenie", None))
        self.lbl_autor.setText(QCoreApplication.translate("MainWindow", u"Szymon Krygier WCY19IJ1N1", None))
        self.lbl_chatbox.setText(QCoreApplication.translate("MainWindow", u"Chatbox", None))
        self.btn_disconnect_from_receiver.setText(QCoreApplication.translate("MainWindow", u"Roz\u0142\u0105cz od u\u017cytkownika", None))
    # retranslateUi

