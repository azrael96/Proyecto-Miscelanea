from PySide6 import QtCore
from PySide6.QtWidgets import QWidget
from datetime import datetime

from system.resources import constants, functions
from system.views.Vendedor.ui_home2 import Ui_home2

class Home2Widget(QWidget):
    def __init__(self, data, ced, apertura, caja, window):
        QWidget.__init__(self)
        self.setObjectName("home2")
        self.ui = Ui_home2()
        self.ui.setupUi(self)
        self.data = data
        self.apertura = apertura
        self.caja = caja

        def cerrarCaja():
            self.data.cerrarCaja(self.caja, self.apertura)
            ape = self.ui.textApertura.text()
            cie = self.ui.textCierre.text()
            functions.popQMessageBox(constants.TYPE_INFO, "Proceso Exitoso", "La caja se cerro con: \n un valor de apertura de: "+ape+" \n y un valor de cierre de: "+cie)
            window.close()

        def updateUser():
            user = self.data.getUsuario(ced)
            cedula = user[0]
            nombre = user[1] + " " + user[2] + " " + user[3] + " " + user[4]
            dir = user[5]
            tel = user[6]
            rol = user[7]
            alias = user[8]

            self.ui.textWelcome.setText("Bienvenido, " + nombre)
            self.ui.textUser.setText(alias)
            self.ui.textTel.setText(tel)
            self.ui.textRol.setText(rol)
            self.ui.textDir.setText(dir)
            self.ui.textCed.setText(cedula)

        functions.theme(self.ui.frame, constants.moduleTheme)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(lambda: self.ui.textTime.setText(datetime.now().strftime("%H:%M:%S")))
        self.timer.timeout.connect(lambda: self.ui.textDate.setText(datetime.now().strftime("%Y-%m-%d")))
        self.timer.start()

        self.ui.proAddButton.clicked.connect(cerrarCaja)

        updateUser()
        self.reset()

    def reset(self):
        self.updateCaja()

    def updateCaja(self):
        cierre = str(self.data.cierreActual(self.caja, self.apertura))
        self.ui.textApertura.setText(str(self.apertura))
        self.ui.textCierre.setText(cierre)