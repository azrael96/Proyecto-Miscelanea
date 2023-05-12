from PySide6 import QtWidgets
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QWidget

from system.resources import constants, functions
from system.views.Vendedor.ui_deudas import Ui_deudas

class DeudasWidget(QWidget):
    def __init__(self, data, caja):
        QWidget.__init__(self)
        self.ui = Ui_deudas()
        self.data = data
        self.caja = caja

        def makeAbono():
            abono = self.ui.textAdd.text()
            row = self.ui.tableDeuda.currentRow()
            if row != -1:
                if abono != "":
                    cod = self.ui.tableDeuda.item(row, 0).text()
                    saldo = float(self.ui.tableDeuda.item(row, 2).text())
                    abono = float(abono)
                    if abono > 0:
                        if abono <= saldo:
                            self.data.editDeuda(cod, abono, saldo, self.caja)
                            self.clear()
                            self.fillTableDeuda()
                        else:
                            functions.popQMessageBox(constants.TYPE_WARNING, "Error en el proceso", "El abono es mayor al saldo")
                    else:
                        functions.popQMessageBox(constants.TYPE_WARNING, "Error en el proceso", "El abono debe ser mayor a 0")
                else:
                    functions.popQMessageBox(constants.TYPE_WARNING, "Error en el proceso", "Debe digitar una cantidad a abonar")
            else:
                functions.popQMessageBox(constants.TYPE_WARNING, "Error en el proceso", constants.NO_SELECTION)

        def selectDeuda():
            row = self.ui.tableDeuda.currentRow()
            cedula = self.ui.tableDeuda.item(row, 1).text()
            saldo = self.ui.tableDeuda.item(row, 2).text()
            total = self.ui.tableDeuda.item(row, 3).text()
            abono = self.ui.tableDeuda.item(row, 4).text()

            cliente = self.data.getCliente(cedula)

            self.ui.textCedula.setText(cedula)
            self.ui.textDirec.setText(cliente[5])
            self.ui.textName.setText(cliente[0]+" "+cliente[1]+" "+cliente[2]+" "+cliente[3])
            self.ui.textTelefono.setText(cliente[4])

            self.ui.textTotal.setText(total)
            self.ui.textSaldo.setText(saldo)
            self.ui.textAbono.setText(abono)

        functions.theme(self.ui.frame, constants.moduleTheme)

        self.ui.buttonTrans.clicked.connect(makeAbono)
        self.ui.tableDeuda.itemClicked.connect(selectDeuda)

        self.reset()

    def reset(self):
        self.fillTableDeuda()
        self.setEnable()
        self.clear()

    def clear(self):
        self.ui.textCedula.setText("")
        self.ui.textDirec.setText("")
        self.ui.textName.setText("")
        self.ui.textTelefono.setText("")

        self.ui.textTotal.setText("")
        self.ui.textSaldo.setText("")
        self.ui.textAbono.setText("")
        self.ui.textAdd.setText("")

    def setEnable(self):
        self.ui.textCedula.setEnabled(False)
        self.ui.textDirec.setEnabled(False)
        self.ui.textName.setEnabled(False)
        self.ui.textTelefono.setEnabled(False)

        self.ui.textTotal.setEnabled(False)
        self.ui.textSaldo.setEnabled(False)
        self.ui.textAbono.setEnabled(False)

    def fillTableDeuda(self):
        data = self.data.getListDeuda()
        self.ui.tableDeuda.clear()
        self.ui.tableDeuda.setColumnCount(5)
        self.ui.tableDeuda.setRowCount(0)
        self.ui.tableDeuda.setHorizontalHeaderLabels(["ID", "Cedula", "Saldo", "Total", "Abono"])
        self.ui.tableDeuda.setColumnHidden(0, True)
        self.ui.tableDeuda.setColumnHidden(4, True)

        if len(data) != 0:
            self.ui.tableDeuda.setRowCount(len(data))
            numrow = 0
            for row in data:
                numcol = 0
                for col in row:
                    self.ui.tableDeuda.setItem(numrow, numcol, QtWidgets.QTableWidgetItem(str(col)))
                    numcol += 1
                numrow += 1
