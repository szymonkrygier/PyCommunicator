# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frm_client_config.ui'
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
    QPushButton, QSizePolicy, QWidget)

class Ui_form_client_config(object):
    def setupUi(self, form_client_config):
        if not form_client_config.objectName():
            form_client_config.setObjectName(u"form_client_config")
        form_client_config.resize(442, 244)
        self.lbl_app_title = QLabel(form_client_config)
        self.lbl_app_title.setObjectName(u"lbl_app_title")
        self.lbl_app_title.setGeometry(QRect(10, 10, 291, 31))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.lbl_app_title.setFont(font)
        self.gb_client_config = QGroupBox(form_client_config)
        self.gb_client_config.setObjectName(u"gb_client_config")
        self.gb_client_config.setGeometry(QRect(10, 50, 421, 111))
        self.tb_nick = QLineEdit(self.gb_client_config)
        self.tb_nick.setObjectName(u"tb_nick")
        self.tb_nick.setGeometry(QRect(180, 10, 221, 22))
        self.lbl_nickname = QLabel(self.gb_client_config)
        self.lbl_nickname.setObjectName(u"lbl_nickname")
        self.lbl_nickname.setGeometry(QRect(10, 10, 131, 21))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.lbl_nickname.setFont(font1)
        self.lbl_server_ip = QLabel(self.gb_client_config)
        self.lbl_server_ip.setObjectName(u"lbl_server_ip")
        self.lbl_server_ip.setGeometry(QRect(10, 40, 151, 21))
        self.lbl_server_ip.setFont(font1)
        self.tb_server_ip = QLineEdit(self.gb_client_config)
        self.tb_server_ip.setObjectName(u"tb_server_ip")
        self.tb_server_ip.setGeometry(QRect(180, 40, 221, 22))
        self.lbl_server_port = QLabel(self.gb_client_config)
        self.lbl_server_port.setObjectName(u"lbl_server_port")
        self.lbl_server_port.setGeometry(QRect(10, 70, 161, 21))
        self.lbl_server_port.setFont(font1)
        self.tb_server_port = QLineEdit(self.gb_client_config)
        self.tb_server_port.setObjectName(u"tb_server_port")
        self.tb_server_port.setGeometry(QRect(180, 70, 221, 22))
        self.btn_connect = QPushButton(form_client_config)
        self.btn_connect.setObjectName(u"btn_connect")
        self.btn_connect.setGeometry(QRect(10, 170, 421, 31))
        self.lbl_autor = QLabel(form_client_config)
        self.lbl_autor.setObjectName(u"lbl_autor")
        self.lbl_autor.setGeometry(QRect(10, 220, 161, 16))

        self.retranslateUi(form_client_config)

        QMetaObject.connectSlotsByName(form_client_config)
    # setupUi

    def retranslateUi(self, form_client_config):
        form_client_config.setWindowTitle(QCoreApplication.translate("form_client_config", u"Komunikator P2P - Konfiguracja klienta", None))
        self.lbl_app_title.setText(QCoreApplication.translate("form_client_config", u"Komunikator P2P - Konfiguracja klienta", None))
        self.gb_client_config.setTitle("")
        self.lbl_nickname.setText(QCoreApplication.translate("form_client_config", u"Nazwa wy\u015bwietlana:", None))
        self.lbl_server_ip.setText(QCoreApplication.translate("form_client_config", u"IP serwera centralnego:", None))
        self.lbl_server_port.setText(QCoreApplication.translate("form_client_config", u"Port serwera centralnego:", None))
        self.btn_connect.setText(QCoreApplication.translate("form_client_config", u"Po\u0142\u0105cz z serwerem centralnym", None))
        self.lbl_autor.setText(QCoreApplication.translate("form_client_config", u"Szymon Krygier WCY19IJ1N1", None))
    # retranslateUi

