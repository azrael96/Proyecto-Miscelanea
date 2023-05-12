import sys

from system.modules import manager, vendedor
from system.resources import constants, functions, connector
from PySide6 import QtCore
from PySide6.QtGui import Qt, QIcon
from PySide6.QtWidgets import QMainWindow, QApplication

from system.views.ui_Login import Ui_MainWindow as Ui_LoginWindow

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(self.size())

        self.data = connector.DatabaseLink()
        self.ui.creditsLabel.setText(self.data.conexionStatus())

        functions.theme(self.ui.styleSheet, constants.loginTheme)
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())
        self.ui.closeAppBtn.clicked.connect(lambda: self.close())
        self.ui.loginButton.clicked.connect(lambda: self.validar(self.ui.userText.text(), self.ui.passText.text()))

        self.show()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()
            event.accept()
        self.ui.titleRightInfo.mouseMoveEvent = self.mouseMoveEvent

    def keyPressEvent(self, event):
        if event.key() in (QtCore.Qt.Key_Enter, QtCore.Qt.Key_Return):
            self.validar(self.ui.userText.text(), self.ui.passText.text())

    def validar(self, nick, passw):

        def errorMsj(type, msj):
            functions.popQMessageBox(type, "Error en el Login", msj)
            self.ui.userText.setText("")
            self.ui.passText.setText("")

        def openWindow(val, usercod):
            global window
            window.close()
            if val == constants.WINDOW_TYPE_ADMIN:
                window = manager.MainWindow(usercod)
            if val == constants.WINDOW_TYPE_VENDEDOR:
                window = vendedor.MainWindow(usercod)
            window.show()

        if nick != "" and passw != "":
            valores = self.data.loginUser(nick, passw)
            if valores != None:
                    if valores[0] == True:
                        openWindow(valores[1], valores[2])
                    else:
                        errorMsj(constants.TYPE_CRITIC, constants.LOGIN_MSJ1)
            else:
                errorMsj(constants.TYPE_CRITIC, constants.LOGIN_MSJ2)
        else:
            errorMsj(constants.TYPE_WARNING, constants.LOGIN_MSJ3)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("images/images/Icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())