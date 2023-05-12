from PySide6 import QtWidgets
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QWidget

from system.resources import constants, functions
from system.views.Vendedor.ui_gastos import Ui_gastos

rx20 = ("^[0-9]{20}$")
class GastosWidget(QWidget):
    def __init__(self, data, caja):
        QWidget.__init__(self)
        self.setObjectName("gastos")
        self.ui = Ui_gastos()
        self.ui.setupUi(self)
        self.data = data
        self.caja = caja

        def registrar():
            decripcion = self.ui.textDes.text()
            valor = self.ui.textValor.text()
            caj = self.caja

            if valor != "" and decripcion != "":
                self.data.addGastos(decripcion, valor, caj)
                self.reset()
            else:
                functions.popQMessageBox(constants.TYPE_WARNING, "Error en el proceso", constants.LOGIN_MSJ3)

        self.ui.textValor.setValidator(QRegularExpressionValidator(rx20, self))
        functions.theme(self.ui.frame, constants.moduleTheme)
        self.ui.buttonReg.clicked.connect(registrar)
        self.reset()

    def reset(self):
        self.clear()
        self.fillTableGastos()

    def fillTableGastos(self):
        data = self.data.getListGastos(self.caja)
        self.ui.tableGastos.clear()
        self.ui.tableGastos.setColumnCount(2)
        self.ui.tableGastos.setRowCount(0)
        self.ui.tableGastos.setHorizontalHeaderLabels(["Descripción", "Valor"])

        if len(data) != 0:
            self.ui.tableGastos.setRowCount(len(data))
            numrow = 0
            for row in data:
                numcol = 0
                for col in row:
                    self.ui.tableGastos.setItem(numrow, numcol, QtWidgets.QTableWidgetItem(str(col)))
                    numcol += 1
                numrow += 1

    def clear(self):
        self.ui.textValor.setText("")
        self.ui.textDes.setText("")
