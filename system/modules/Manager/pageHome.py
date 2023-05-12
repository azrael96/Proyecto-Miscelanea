from PySide6 import QtCore
from PySide6.QtWidgets import QWidget
from datetime import datetime

from system.views.Manager.ui_home import Ui_home

class HomeWidget(QWidget):
    def __init__(self, data, ced):
        QWidget.__init__(self)
        self.setObjectName("home")
        self.ui = Ui_home()
        self.ui.setupUi(self)
        self.data = data

        def updateUser():
            user = self.data.getUsuario(ced)
            cedula = user[0]
            nombre = user[1] + " " + user[2] + " " + user[3] + " " + user[4]
            dir = user[5]
            tel = user[6]
            rol = user[7]
            alias = user[8]

            self.ui.textWelcome.setText("Bienvenido \n" + nombre)
            self.ui.textUser.setText(alias)
            self.ui.textTel.setText(tel)
            self.ui.textRol.setText(rol)
            self.ui.textDir.setText(dir)
            self.ui.textCed.setText(cedula)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(lambda: self.ui.textTime.setText(datetime.now().strftime("%H:%M:%S")))
        self.timer.timeout.connect(lambda: self.ui.textDate.setText(datetime.now().strftime("%Y-%m-%d")))
        self.timer.start()

        updateUser()

    def reset(self):
        pass

