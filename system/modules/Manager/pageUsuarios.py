from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QRegularExpressionValidator

from system.resources import constants, functions
from system.views.Manager.ui_usuarios import Ui_usuarios

codigo = ""
pressed = ""
rx20 = ("^[0-9]{20}$")
rx32 = ("^[0-9]{32}$")
class UsuariosWidget(QWidget):
    def __init__(self, data):
        QWidget.__init__(self)
        self.setObjectName("usuarios")
        self.ui = Ui_usuarios()
        self.ui.setupUi(self)
        self.data = data

        def switchDelDisable(val):
            self.ui.usuNomText.setEnabled(val)
            self.ui.usuNom2Text.setEnabled(val)
            self.ui.usuApe1Text.setEnabled(val)
            self.ui.usuApe2Text.setEnabled(val)
            self.ui.usuCedText.setEnabled(val)
            self.ui.usuDirText.setEnabled(val)
            self.ui.usuTelText.setEnabled(val)
            self.ui.usuNickText.setEnabled(val)
            self.ui.usuConText.setEnabled(val)
            self.ui.usuRolCombo.setEnabled(val)
            self.ui.usuClearButton.setEnabled(val)

        def selectItem():
            global codigo
            row = self.ui.usuTable.currentRow()
            codigo = self.ui.usuTable.item(row, 0).text()
            nom1 = self.ui.usuTable.item(row, 1).text()
            nom2 = self.ui.usuTable.item(row, 2).text()
            ape1 = self.ui.usuTable.item(row, 3).text()
            ape2 = self.ui.usuTable.item(row, 4).text()
            dir = self.ui.usuTable.item(row, 5).text()
            tel = self.ui.usuTable.item(row, 6).text()
            rol = self.ui.usuTable.item(row, 7).text()
            nic = self.ui.usuTable.item(row, 8).text()
            con = self.ui.usuTable.item(row, 9).text()

            self.ui.usuNomText.setText(nom1)
            self.ui.usuNom2Text.setText(nom2)
            self.ui.usuApe1Text.setText(ape1)
            self.ui.usuApe2Text.setText(ape2)
            self.ui.usuCedText.setText(codigo)
            self.ui.usuDirText.setText(dir)
            self.ui.usuTelText.setText(tel)
            self.ui.usuNickText.setText(nic)
            self.ui.usuConText.setText(con)
            self.ui.usuRolCombo.setCurrentText(rol)

        def add():
            global pressed
            pressed = "add"

            self.clear()
            self.clearCod()
            self.switchDisable(True)

        def edit():
            global codigo, pressed
            if codigo != "":
                self.switchDisable(True)
                self.ui.usuCedText.setEnabled(False)
                pressed = "edit"
            else:
                functions.popQMessageBox(constants.TYPE_WARNING, "Error en el proceso", constants.NO_SELECTION)

        def delete():
            global codigo, pressed
            if codigo != "":
                self.switchDisable(True)
                switchDelDisable(False)
                pressed = "del"
            else:
                functions.popQMessageBox(constants.TYPE_WARNING, "Error en el proceso", constants.NO_SELECTION)

        def cancel():
            self.switchDisable(False)
            self.clear()
            self.clearCod()

        def save():
            global codigo, pressed

            if pressed == "del":
                self.data.delUsuario(codigo)
                switchDelDisable(True)

            nom1 = self.ui.usuNomText.text()
            nom2 = self.ui.usuNom2Text.text()
            ape1 = self.ui.usuApe1Text.text()
            ape2 = self.ui.usuApe2Text.text()
            ced = self.ui.usuCedText.text()
            direc = self.ui.usuDirText.text()
            tel = self.ui.usuTelText.text()
            nic = self.ui.usuNickText.text()
            con = self.ui.usuConText.text()
            rol = self.ui.usuRolCombo.currentText()

            if nom1 != "" and  ape1 != "" and ced != "" and direc != "" and tel != "" and nic != "" and con != "" and rol != "":
                if pressed == "add":
                    if self.data.cedulaDontExist(ced):
                        self.data.addUsuario(nom1, nom2, ape1, ape2, ced, direc, tel, rol, nic, con)
                    else:
                        functions.popQMessageBox(constants.TYPE_CRITIC, "Error en el proceso", "La cedula ya existe")
                if pressed == "edit":
                    self.data.editUsuario(ced, nom1, nom2, ape1, ape2, direc, tel, rol, nic, con)
                    self.clearCod()
                self.clear()
                self.fillTable()
                self.switchDisable(False)
            else:
                functions.popQMessageBox(constants.TYPE_WARNING, "Error en el proceso", constants.LOGIN_MSJ3)

        self.ui.usuClearButton.clicked.connect(self.clear)
        self.ui.usuSaveButton.clicked.connect(save)
        self.ui.usuCancelButton.clicked.connect(cancel)
        self.ui.usuAddButton.clicked.connect(add)
        self.ui.usuEditButton.clicked.connect(edit)
        self.ui.usuDelButton.clicked.connect(delete)

        functions.theme(self.ui.frame, constants.moduleTheme)
        self.ui.usuTable.itemClicked.connect(selectItem)

        self.ui.usuCedText.setValidator(QRegularExpressionValidator(rx20, self))
        self.ui.usuTelText.setValidator(QRegularExpressionValidator(rx32, self))

        self.reset()

    def reset(self):
        self.clear()
        self.fillTable()
        self.fillCombo()
        self.switchDisable(False)

    def clearCod(self):
        global codigo
        codigo = ""
        self.ui.usuTable.setCurrentCell(-1, -1)

    def clear(self):
        self.ui.usuNomText.setText("")
        self.ui.usuNom2Text.setText("")
        self.ui.usuApe1Text.setText("")
        self.ui.usuApe2Text.setText("")
        self.ui.usuCedText.setText("")
        self.ui.usuConText.setText("")
        self.ui.usuDirText.setText("")
        self.ui.usuTelText.setText("")
        self.ui.usuNickText.setText("")
        self.ui.usuRolCombo.setCurrentIndex(-1)

    def switchDisable(self, val):
        self.ui.usuNomText.setEnabled(val)
        self.ui.usuNom2Text.setEnabled(val)
        self.ui.usuApe1Text.setEnabled(val)
        self.ui.usuApe2Text.setEnabled(val)
        self.ui.usuCedText.setEnabled(val)
        self.ui.usuConText.setEnabled(val)
        self.ui.usuDirText.setEnabled(val)
        self.ui.usuTelText.setEnabled(val)
        self.ui.usuNickText.setEnabled(val)
        self.ui.usuRolCombo.setEnabled(val)
        self.ui.usuClearButton.setEnabled(val)
        self.ui.usuSaveButton.setEnabled(val)
        self.ui.usuCancelButton.setEnabled(val)

        self.ui.usuTable.setEnabled(not val)
        self.ui.usuEditButton.setEnabled(not val)
        self.ui.usuAddButton.setEnabled(not val)
        self.ui.usuDelButton.setEnabled(not val)

    def fillTable(self):
        data = self.data.getListUsuario()
        self.clearCod()
        self.ui.usuTable.clear()
        self.ui.usuTable.setColumnCount(10)
        self.ui.usuTable.setRowCount(0)
        self.ui.usuTable.setHorizontalHeaderLabels(["Cédula", "Nombre1", "Nombre2", "Apellido1", "Apellido2", "Dirección", "Teléfono", "Rol", "Nick", "Contraseña"])

        if len(data) != 0:
            self.ui.usuTable.setRowCount(len(data))
            numrow = 0
            for row in data:
                numcol = 0
                for col in row:
                    self.ui.usuTable.setItem(numrow, numcol, QtWidgets.QTableWidgetItem(str(col)))
                    numcol += 1
                numrow += 1

    def fillCombo(self):

        list2 = [
            self.tr('Admin'),
            self.tr('Vendedor'),
        ]

        self.ui.usuRolCombo.clear()
        self.ui.usuRolCombo.addItems(list2)
        self.ui.usuRolCombo.setCurrentIndex(-1)

