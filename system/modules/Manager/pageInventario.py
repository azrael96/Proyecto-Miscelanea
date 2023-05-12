from PySide6 import QtWidgets
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget

from system.resources import constants, functions
from system.views.Manager.ui_inventario import Ui_inventario

codigo = ""
pressed = ""
class InventarioWidget(QWidget):
    def __init__(self, data):
        QWidget.__init__(self)
        self.setObjectName("inventario")
        self.ui = Ui_inventario()
        self.ui.setupUi(self)
        self.data = data

        def selectItem():
            def selectImg():
                pix = QPixmap()
                bydata = self.data.getFotoProducto(codigo)
                if pix.loadFromData(bydata[0]):
                    self.ui.proFotLabel.setPixmap(pix)

            row = self.ui.proTable.currentRow()
            codigo = self.ui.proTable.item(row, 3).text()

            items = self.data.getOneProducto(codigo)

            self.ui.proNomText.setText(items[0])
            self.ui.proDesText.setText(items[1])
            self.ui.proCatCombo.setText(items[2])
            selectImg()

        functions.theme(self.ui.frame, constants.moduleTheme)
        self.ui.proTable.itemClicked.connect(selectItem)
        self.reset()

    def reset(self):
        self.fillTable()
        self.setDisable()
        self.clear()

    def clear(self):
        self.ui.proFotLabel.setPixmap(QPixmap())
        self.ui.proNomText.setText("")
        self.ui.proDesText.setText("")
        self.ui.proCatCombo.setText("")

    def setDisable(self):
        self.ui.proNomText.setEnabled(False)
        self.ui.proDesText.setEnabled(False)
        self.ui.proCatCombo.setEnabled(False)

    def fillTable(self):
        data = self.data.getListInventario()
        self.ui.proTable.clear()
        self.ui.proTable.setColumnCount(4)
        self.ui.proTable.setRowCount(0)
        self.ui.proTable.setHorizontalHeaderLabels(["Producto", "Cantidad", "Costo", "Cod"])
        self.ui.proTable.setColumnHidden(3, True)

        if len(data) != 0:
            self.ui.proTable.setRowCount(len(data))
            numrow = 0
            for row in data:
                numcol = 0
                for col in row:
                    self.ui.proTable.setItem(numrow, numcol, QtWidgets.QTableWidgetItem(str(col)))
                    numcol += 1
                numrow += 1

