from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QRegularExpressionValidator
from PySide6.QtWidgets import QWidget
from datetime import date as fecha

from system.resources import constants, functions, pdf_printer
from system.views.Vendedor.ui_ventas import Ui_ventas
from system.modules.Vendedor.clienteDialog import ClientDialog

cat_dic = {}
rx20 = ("^[0-9]{20}$")
class VentasWidget(QWidget):
    def __init__(self, data, caja):
        QWidget.__init__(self)
        self.setObjectName("ventas")
        self.ui = Ui_ventas()
        self.ui.setupUi(self)
        self.data = data
        self.caja = caja
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.ui.textCantAdd.setValidator(QRegularExpressionValidator(rx20, self))

        def enableFilters(val):
            self.ui.catProFilCombo.setEnabled(val)
            self.ui.nomProFilText.setEnabled(val)
            self.ui.pedBusButton.setEnabled(val)

        def filtrarProductos():
            nom = self.ui.nomProFilText.text()
            cat = self.ui.catProFilCombo.currentText()
            self.fillTablePro(cat, nom, None)
            enableFilters(False)
            self.clearStart()

        def restartFilters():
            self.fillTablePro("", "", None)
            self.ui.nomProFilText.setText("")
            self.ui.catProFilCombo.setCurrentIndex(-1)
            enableFilters(True)
            self.clearStart()

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

            stockProducto = self.data.getCantStock(codigo)
            self.ui.textCantDis.setText(str(stockProducto[0]))
            self.ui.textPrecioPro.setText(str(stockProducto[1]))

            self.ui.nomProSelText.setText(nom)
            self.ui.desProSelText.setText(des)
            self.ui.catProSelText.setText(cat)
            self.ui.canProSelText.setText(str(cant))
            selectImg()

        def delVenta():
            row = self.ui.tableFactura.currentRow()
            if row != -1:
                self.ui.tableFactura.removeRow(row)
                sumTotal()
            else:
                functions.popQMessageBox(constants.TYPE_WARNING, "Error en el proceso", constants.NO_SELECTION)

        def addVenta():
            def alreadyInVentas():
                nonlocal codigo
                notOnVentas = True
                for i in range(self.ui.tableFactura.rowCount()):
                    prodNow = self.ui.tableFactura.item(i, 0).text()
                    if prodNow == codigo:
                        notOnVentas = False
                return notOnVentas

            proSelected = self.ui.proTable.currentRow()

            cantAdd = self.ui.textCantAdd.text()
            cantDis = self.ui.textCantDis.text()
            codigo = self.ui.proTable.item(proSelected, 0).text()

            if proSelected != -1 and cantAdd != "":
                if alreadyInVentas():
                    if int(cantAdd) >= 1:
                        if int(cantAdd) <= int(cantDis):
                            nombre = self.ui.nomProSelText.text()
                            precio = self.ui.textPrecioPro.text()
                            total = str(float(cantAdd) * float(precio))
                            stock = self.data.getCantStock(codigo)
                            StockCod = stock[2]
                            self.ui.tableFactura.insertRow(self.ui.tableFactura.rowCount())
                            item = QtWidgets.QTableWidgetItem(codigo)
                            self.ui.tableFactura.setItem(self.ui.tableFactura.rowCount() - 1, 0, item)
                            item = QtWidgets.QTableWidgetItem(nombre)
                            self.ui.tableFactura.setItem(self.ui.tableFactura.rowCount() - 1, 1, item)
                            item = QtWidgets.QTableWidgetItem(cantAdd)
                            self.ui.tableFactura.setItem(self.ui.tableFactura.rowCount() - 1, 2, item)
                            item = QtWidgets.QTableWidgetItem(precio)
                            self.ui.tableFactura.setItem(self.ui.tableFactura.rowCount() - 1, 3, item)
                            item = QtWidgets.QTableWidgetItem(total)
                            self.ui.tableFactura.setItem(self.ui.tableFactura.rowCount() - 1, 4, item)
                            item = QtWidgets.QTableWidgetItem(str(StockCod))
                            self.ui.tableFactura.setItem(self.ui.tableFactura.rowCount() - 1, 5, item)
                            self.clearStart()
                            sumTotal()
                            self.fillTablePro("", "", None)
                        else:
                            functions.popQMessageBox(constants.TYPE_WARNING, "Error en el proceso", "La cantidad de producto a vender es mayor a lo que se tiene en stock")
                    else:
                        functions.popQMessageBox(constants.TYPE_WARNING, "Error en el proceso", "La cantidad de producto a vender tiene que ser mayor a 1")
                else:
                    functions.popQMessageBox(constants.TYPE_WARNING, "Error en el proceso", "El producto ya esta en la lista de productos a facturar")
            else:
                functions.popQMessageBox(constants.TYPE_WARNING, "Error en el proceso", "Nesesita selecionar un producto e introducir una cantidad")

        def sumTotal():
            sum = 0
            for i in range(self.ui.tableFactura.rowCount()):
                cant = self.ui.tableFactura.item(i, 4).text()
                sum = sum + float(cant)
            self.ui.TextTotal.setText(str(sum))

        def reiniciar():
            self.clearStart()
            self.fillTablePro("", "", None)
            self.fillTableVentas()

        def facturar():
            tip = self.ui.comboBoxMetodo.currentText()
            tot = self.ui.TextTotal.text()

            if tot != "" and tip != "":
                caj = self.caja
                date = fecha.today()

                dlgClient = ClientDialog(self.data)
                dlgClient.exec()
                cli = dlgClient.ui.usuCedText.text()
                if cli != "":
                    factura = self.data.addFactura(tip, date, tot, caj, cli)
                    metodo = self.ui.comboBoxMetodo.currentText()
                    if metodo == "Deuda":
                        self.data.addDeuda("En Deuda", 0, tot, tot, cli)

                    for i in range(self.ui.tableFactura.rowCount()):
                        precio = self.ui.tableFactura.item(i, 3).text()
                        cant = self.ui.tableFactura.item(i, 2).text()
                        pro = self.ui.tableFactura.item(i, 0).text()
                        sto = self.ui.tableFactura.item(i, 5).text()
                        self.data.addVenta(precio, cant, factura, pro, sto)

                    reiniciar()
                    pdf_printer.makeFacturaPDF(self.data.getInfoFactura(factura), factura)
                    functions.popQMessageBox(constants.TYPE_INFO, "Factura Realizada", "Factura guardada en el pdf con nombre: fac" + str(factura))
                else:
                    functions.popQMessageBox(constants.TYPE_CRITIC, "Factura Cancelada", "Se canceló el proceso de facturación")
            else:
                functions.popQMessageBox(constants.TYPE_WARNING, "Error en el proceso", constants.LOGIN_MSJ3)

        functions.theme(self.ui.frame, constants.moduleTheme)

        self.ui.pedBusButton.clicked.connect(filtrarProductos)
        self.ui.pedResButton.clicked.connect(restartFilters)
        self.ui.proTable.itemClicked.connect(selectProducto)

        self.ui.venButtonAdd.clicked.connect(addVenta)
        self.ui.venButtonDel.clicked.connect(delVenta)
        self.ui.venButtonRei.clicked.connect(reiniciar)
        self.ui.venButtonFac.clicked.connect(facturar)

        self.reset()
        self.fillTableVentas()

    def reset(self):
        self.fillTablePro("", "", None)
        self.fillCombo()
        self.disableStart()
        self.clearStart()

    def fillTableVentas(self):
        self.ui.tableFactura.clear()
        self.ui.tableFactura.setColumnCount(6)
        self.ui.tableFactura.setRowCount(0)
        self.ui.tableFactura.setHorizontalHeaderLabels(["ProductID", "Producto", "Cantidad", "Valor/unidad", "Total", "StockID"])
        self.ui.tableFactura.setColumnHidden(0, True)
        self.ui.tableFactura.setColumnHidden(5, True)

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

        met_list = ["Efectivo", "Deuda"]
        self.ui.comboBoxMetodo.clear()
        self.ui.comboBoxMetodo.addItems(met_list)
        self.ui.comboBoxMetodo.setCurrentIndex(-1)

    def disableStart(self):
        self.ui.nomProSelText.setEnabled(False)
        self.ui.desProSelText.setEnabled(False)
        self.ui.catProSelText.setEnabled(False)
        self.ui.canProSelText.setEnabled(False)
        self.ui.textCantDis.setEnabled(False)
        self.ui.TextTotal.setEnabled(False)
        self.ui.textPrecioPro.setEnabled(False)

    def clearStart(self):
        self.ui.nomProFilText.setText("")
        self.ui.nomProSelText.setText("")
        self.ui.desProSelText.setText("")
        self.ui.catProSelText.setText("")
        self.ui.canProSelText.setText("")
        self.ui.textPrecioPro.setText("")
        self.ui.textCantDis.setText("")
        self.ui.textCantAdd.setText("")
        self.ui.proFotLabel.setPixmap(QPixmap())
        self.ui.comboBoxMetodo.setCurrentIndex(-1)
        self.ui.catProFilCombo.setCurrentIndex(-1)