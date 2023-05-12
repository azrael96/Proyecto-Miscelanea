from PySide6 import QtWidgets
from PySide6.QtGui import QPixmap, QRegularExpressionValidator
from PySide6.QtWidgets import QWidget

from system.resources import constants, functions
from system.views.Vendedor.ui_stock import Ui_stock

cat_dic = {}
stock = ""
rx20 = ("^[0-9]{20}$")
class StockWidget(QWidget):
    def __init__(self, data):
        QWidget.__init__(self)
        self.setObjectName("stock")
        self.ui = Ui_stock()
        self.ui.setupUi(self)
        self.data = data

        self.ui.textCanTrans.setValidator(QRegularExpressionValidator(rx20, self))
        self.ui.textValVen.setValidator(QRegularExpressionValidator(rx20, self))

        def enableFilters(val):
            self.ui.catProFilCombo.setEnabled(val)
            self.ui.nomProFilText.setEnabled(val)
            self.ui.pedBusButton.setEnabled(val)

        def filtrarProductos():
            nom = self.ui.nomProFilText.text()
            cat = self.ui.catProFilCombo.currentText()
            self.fillTablePro(cat, nom, None)
            enableFilters(False)
            clearProducto()
            clearStock()

        def restartFilters():
            self.fillTablePro("", "", None)
            self.ui.nomProFilText.setText("")
            self.ui.catProFilCombo.setCurrentIndex(-1)
            enableFilters(True)
            clearProducto()
            clearStock()

        def clearProducto():
            self.ui.nomProSelText.setText("")
            self.ui.desProSelText.setText("")
            self.ui.catProSelText.setText("")
            self.ui.canProSelText.setText("")
            self.ui.proFotLabel.setPixmap(QPixmap())
            self.ui.textCanStock.setText("")
            self.ui.textCosLote.setText("")
            global stock
            stock = ""
            #self.ui.invTable.clear()
            self.fillTableInv()

        def selectProducto():
            def selectImg():
                nonlocal codigo
                pix = QPixmap()
                bydata = self.data.getFotoProducto(codigo)
                if pix.loadFromData(bydata[0]):
                    self.ui.proFotLabel.setPixmap(pix)

            row = self.ui.proTable.currentRow()
            codigo = self.ui.proTable.item(row, 0).text()
            nom = self.ui.proTable.item(row, 1).text()
            des = self.ui.proTable.item(row, 2).text()
            cat = self.ui.proTable.item(row, 3).text()
            cant = self.data.getCantTotalInventario(codigo)

            self.ui.nomProSelText.setText(nom)
            self.ui.desProSelText.setText(des)
            self.ui.catProSelText.setText(cat)
            self.ui.canProSelText.setText(str(cant))

            stockProducto = self.data.getCantStock(codigo)
            self.ui.textCanStock.setText(str(stockProducto[0]))
            self.ui.textCosLote.setText(str(stockProducto[1]))
            global stock
            stock = stockProducto[2]

            self.fillTableInv()
            selectImg()
            clearStock()

        def clearStock():
            self.ui.textCanLote.setText("")
            self.ui.textCanTrans.setText("")
            self.ui.textValVen.setText("")

        def selectLote():
            row = self.ui.invTable.currentRow()
            codigo = self.ui.invTable.item(row, 0).text()
            can = self.ui.invTable.item(row, 2).text()

            self.ui.textCanLote.setText(can)

            self.ui.textCanTrans.setText("")
            self.ui.textValVen.setText("")

        def trasnferStock():
            global stock
            cantTransfer = self.ui.textCanTrans.text()
            cantLote = self.ui.textCanLote.text()
            valor = self.ui.textValVen.text()
            row = self.ui.invTable.currentRow()

            if stock != "" and row != -1:
                inv = self.ui.invTable.item(row, 0).text()
                if cantTransfer != "" and valor != "":
                    cantTransfer = int(cantTransfer)
                    cantLote = int(cantLote)
                    if cantLote >= cantTransfer:
                        self.data.editStock(stock, cantTransfer, valor, inv)
                        self.fillTablePro("","", None)
                        self.fillTableInv()
                        clearStock()
                    else:
                        functions.popQMessageBox(constants.TYPE_WARNING, "Error en el proceso", "El valor a trasferir es mayor a la cantidad en el lote")
                else:
                    functions.popQMessageBox(constants.TYPE_WARNING, "Error en el proceso", constants.LOGIN_MSJ3)
            else:
                functions.popQMessageBox(constants.TYPE_WARNING, "Error en el proceso", constants.NO_SELECTION)

        functions.theme(self.ui.frame, constants.moduleTheme)

        self.ui.pedBusButton.clicked.connect(filtrarProductos)
        self.ui.pedResButton.clicked.connect(restartFilters)
        self.ui.ButtonTrans.clicked.connect(trasnferStock)

        self.ui.proTable.itemClicked.connect(selectProducto)
        self.ui.invTable.itemClicked.connect(selectLote)

        self.reset()

    def disableStart(self):
        self.ui.nomProSelText.setEnabled(False)
        self.ui.desProSelText.setEnabled(False)
        self.ui.catProSelText.setEnabled(False)
        self.ui.canProSelText.setEnabled(False)
        self.ui.textCanStock.setEnabled(False)
        self.ui.textCosLote.setEnabled(False)
        self.ui.textCanLote.setEnabled(False)

    def clearStart(self):
        self.ui.nomProFilText.setText("")
        self.ui.nomProSelText.setText("")
        self.ui.desProSelText.setText("")
        self.ui.catProSelText.setText("")
        self.ui.canProSelText.setText("")
        self.ui.textCanStock.setText("")
        self.ui.textCosLote.setText("")
        self.ui.textCanLote.setText("")
        self.ui.textValVen.setText("")
        self.ui.textCanTrans.setText("")
        self.ui.proFotLabel.setPixmap(QPixmap())

    def reset(self):
        self.fillTablePro("", "", None)
        self.fillCombo()
        self.fillTableInv()
        self.disableStart()
        self.clearStart()

    def fillTablePro(self, cat, nom, dat):
        if dat != None:
            data = dat
        else:
            data = self.data.getListProducto(cat, nom)
        self.ui.proTable.clear()
        self.ui.proTable.setColumnCount(4)
        self.ui.proTable.setRowCount(0)
        self.ui.proTable.setHorizontalHeaderLabels(["ID", "Nombre", "Descripción", "Categoria"])
        self.ui.proTable.setColumnHidden(0, True)
        self.ui.proTable.setColumnHidden(2, True)
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

    def fillTableInv(self):

        self.ui.invTable.clear()
        self.ui.invTable.setColumnCount(4)
        self.ui.invTable.setRowCount(0)
        self.ui.invTable.setHorizontalHeaderLabels(["ID", "Nombre", "Cantidad", "Costo"])
        self.ui.invTable.setColumnHidden(0, True)

        row = self.ui.proTable.currentRow()
        producto = ""
        if row != -1:
            producto = self.ui.proTable.item(row, 0).text()

        if producto != "":
            inv = self.data.getListProductoInventario(producto)
            if len(inv) != 0:
                self.ui.invTable.setRowCount(len(inv))
                numrow = 0
                for row in inv:
                    numcol = 0
                    for col in row:
                        self.ui.invTable.setItem(numrow, numcol, QtWidgets.QTableWidgetItem(str(col)))
                        numcol += 1
                    numrow += 1

    def fillCombo(self):
        data = self.data.getNamesCategoria()
        if len(data) != 0:
            global cat_dic
            cat_list = []
            for row in data:
                cat_dic[row[0]] = row[1]
                cat_list.append(self.tr(row[1]))

            self.ui.catProFilCombo.clear()
            self.ui.catProFilCombo.addItems(cat_list)
            self.ui.catProFilCombo.setCurrentIndex(-1)

