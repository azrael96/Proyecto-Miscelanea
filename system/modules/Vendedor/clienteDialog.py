from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QDialog

from system.resources import functions, constants
from system.views.Vendedor.ui_cliente import Ui_Dialog

rx20 = ("^[0-9]{32}$")
class ClientDialog(QDialog):
    def __init__(self, data):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.data = data

        functions.theme(self.ui.frame, constants.moduleTheme)
        self.ui.usuCedText.setValidator(QRegularExpressionValidator(rx20, self))
        self.ui.usuTelText.setValidator(QRegularExpressionValidator(rx20, self))

        def setEnabled(val):
            self.ui.usuNomText.setEnabled(val)
            self.ui.usuNom2Text.setEnabled(val)
            self.ui.usuApe1Text.setEnabled(val)
            self.ui.usuApe2Text.setEnabled(val)
            self.ui.usuDirText.setEnabled(val)
            self.ui.usuTelText.setEnabled(val)

        def cancelar():
            self.ui.usuCedText.setText("")
            self.close()

        def verificar():
            cedula = self.ui.usuCedText.text()
            if cedula != "":
                self.ui.labelError.setText("")
                cliente = self.data.getCliente(cedula)
                if cliente != None:
                    setEnabled(False)
                    self.ui.usuNomText.setText(cliente[0])
                    self.ui.usuNom2Text.setText(cliente[1])
                    self.ui.usuApe1Text.setText(cliente[2])
                    self.ui.usuApe2Text.setText(cliente[3])
                    self.ui.usuTelText.setText(cliente[4])
                    self.ui.usuDirText.setText(cliente[5])
                else:
                    setEnabled(True)
            else:
                self.ui.labelError.setText("Debe ingresar una cedula")

        def facturar():
            cedula = self.ui.usuCedText.text()
            if cedula != "":
                self.ui.labelError.setText("")
                cliente = self.data.getCliente(cedula)
                if cliente == None:
                    add()
                else:
                    self.close()
            else:
                self.ui.labelError.setText("Debe ingresar una cedula")

        def add():
            nom1 = self.ui.usuNomText.text()
            nom2 = self.ui.usuNom2Text.text()
            ape1 = self.ui.usuApe1Text.text()
            ape2 = self.ui.usuApe2Text.text()
            ced = self.ui.usuCedText.text()
            direc = self.ui.usuDirText.text()
            tel = self.ui.usuTelText.text()

            if nom1 != "" and nom2 != "" and ape1 != "" and ape2 != "" and ced != "" and direc != "" and tel != "":
                self.data.addCliente(nom1, nom2, ape1, ape2, ced, direc, tel)
                self.close()
            else:
                self.ui.labelError.setText("Debe completar todo el formulario")

        self.ui.cliButtonCan.clicked.connect(cancelar)
        self.ui.cliButtonVer.clicked.connect(verificar)
        self.ui.cliButtonFac.clicked.connect(facturar)

        setEnabled(False)

