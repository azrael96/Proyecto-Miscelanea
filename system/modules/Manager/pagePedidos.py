from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QRegularExpressionValidator, QPixmap

from system.resources import constants, functions
from system.views.Manager.ui_pedido import Ui_pedidos

codigoPed = ""
cat_dic = {}
rx20 = ("^[0-9]{20}$")
class PedidosWidget(QWidget):
    def __init__(self, data):
        QWidget.__init__(self)
        self.setObjectName("pedidos")
        self.ui = Ui_pedidos()
        self.ui.setupUi(self)
        self.data = data

        self.ui.canProSelText.setValidator(QRegularExpressionValidator(rx20, self))
        self.ui.pedCosText.setValidator(QRegularExpressionValidator(rx20, self))
        self.ui.pedCanText.setValidator(QRegularExpressionValidator(rx20, self))

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
            selectImg()

        def selectPedido():
            global codigoPed
            row = self.ui.pedTable.currentRow()
            prod = self.ui.pedTable.item(row, 1).text()
            codigoPed = self.ui.pedTable.item(row, 0).text()
            est = "En Proceso" #en la base de datos con cod

            self.ui.pedNomText.setText(prod)
            self.ui.pedEstText.setText(est)

        def enableFilters(val):
            self.ui.catProFilCombo.setEnabled(val)
            self.ui.nomProFilText.setEnabled(val)
            self.ui.pedBusButton.setEnabled(val)
            self.ui.pedEscButton.setEnabled(val)

        def filtrarProductos():
            nom = self.ui.nomProFilText.text()
            cat = self.ui.catProFilCombo.currentText()
            self.fillTablePro(cat, nom, None)
            enableFilters(False)

        def restartFilters():
            self.fillTablePro("", "", None)
            self.ui.nomProFilText.setText("")
            self.ui.catProFilCombo.setCurrentIndex(-1)
            enableFilters(True)

        def productosEscasos():
            dat = self.data.getListProductoEscacez()
            self.fillTablePro("", "", dat)
            enableFilters(False)

        def addPedido():
            unitario = self.ui.pedCosText.text()
            cantidad = self.ui.pedCanText.text()
            row = self.ui.proTable.currentRow()
            producto = ""
            if row != -1:
                producto = self.ui.proTable.item(row, 0).text()

            if producto != "":
                if unitario != "" and cantidad != "":
                    self.data.addPedido(unitario, cantidad, producto)
                    self.clear()
                    self.fillTablePed()
                    self.fillTablePro("", "", None)
                else:
                    functions.popQMessageBox(constants.TYPE_WARNING, "Error en el proceso", constants.LOGIN_MSJ3)
            else:
                functions.popQMessageBox(constants.TYPE_WARNING, "Error en el proceso", constants.NO_SELECTION)

        def receivePedido():
            global codigoPed
            if codigoPed != "":
                changeEstado("Recibido", codigoPed)
                self.data.addInventario(codigoPed)
                codigoPed = ""
            else:
                functions.popQMessageBox(constants.TYPE_WARNING, "Error en el proceso", constants.NO_SELECTION)

        def rejectPedido():
            global codigoPed
            if codigoPed != "":
                changeEstado("Rechazado", codigoPed)
                codigoPed = ""
            else:
                functions.popQMessageBox(constants.TYPE_WARNING, "Error en el proceso", constants.NO_SELECTION)

        def changeEstado(estado, cod):
            self.data.changeEstadoPedido(cod, estado)
            self.fillTablePed()
            global codigoPed

        self.ui.pedBusButton.clicked.connect(filtrarProductos)
        self.ui.pedResButton.clicked.connect(restartFilters)
        self.ui.pedEscButton.clicked.connect(productosEscasos)
        self.ui.pedAddButton.clicked.connect(addPedido)
        self.ui.pedRecButton.clicked.connect(receivePedido)
        self.ui.pedCanButton.clicked.connect(rejectPedido)

        functions.theme(self.ui.frame, constants.moduleTheme)
        self.ui.pedTable.itemClicked.connect(selectPedido)
        self.ui.proTable.itemClicked.connect(selectProducto)

        self.reset()

    def reset(self):
        self.clear()
        self.fillTablePro("", "", None)
        self.fillTablePed()
        self.fillCombo()
        self.setDisable(False)

    def delImg(self):
        self.ui.proFotLabel.setPixmap(QPixmap())

    def clear(self):
        self.ui.nomProFilText.setText("")
        self.ui.catProFilCombo.setCurrentIndex(-1)

        self.ui.nomProSelText.setText("")
        self.ui.desProSelText.setText("")
        self.ui.canProSelText.setText("")
        self.ui.catProSelText.setText("")
        self.delImg()

        self.ui.pedCanText.setText("")
        self.ui.pedCosText.setText("")

        self.ui.pedNomText.setText("")
        self.ui.pedEstText.setText("")

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

    def fillTablePed(self):
        data = self.data.getListPedido()
        self.ui.pedTable.clear()
        self.ui.pedTable.setColumnCount(4)
        self.ui.pedTable.setRowCount(0)
        self.ui.pedTable.setHorizontalHeaderLabels(["ID", "Producto", "Cantidad", "Costo"])
        self.ui.pedTable.setColumnHidden(0, True)
        if len(data) != 0:
            self.ui.pedTable.setRowCount(len(data))
            numrow = 0
            for row in data:
                numcol = 0
                for col in row:
                    self.ui.pedTable.setItem(numrow, numcol, QtWidgets.QTableWidgetItem(str(col)))
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

    def setDisable(self, val):
        self.ui.nomProSelText.setEnabled(val)
        self.ui.desProSelText.setEnabled(val)
        self.ui.canProSelText.setEnabled(val)
        self.ui.catProSelText.setEnabled(val)
        self.ui.pedNomText.setEnabled(val)
        self.ui.pedEstText.setEnabled(val)