from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget

from system.resources import constants, functions
from system.views.Manager.ui_categorias import Ui_categorias

codigo = ""
pressed = ""
class CategoriasWidget(QWidget):
    def __init__(self, data):
        QWidget.__init__(self)
        self.setObjectName("categorias")
        self.ui = Ui_categorias()
        self.ui.setupUi(self)
        self.data = data

        def switchDelDisable(val):
            self.ui.catNomText.setEnabled(val)
            self.ui.catDesText.setEnabled(val)
            self.ui.catClearButton.setEnabled(val)

        def selectItem():
            global codigo
            row = self.ui.catTable.currentRow()
            codigo = self.ui.catTable.item(row, 0).text()
            nom = self.ui.catTable.item(row, 1).text()
            des = self.ui.catTable.item(row, 2).text()
            self.ui.catNomText.setText(nom)
            self.ui.catDesText.setText(des)

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
                self.data.delCategoria(codigo)
                switchDelDisable(True)

            nombre = self.ui.catNomText.text()
            descripcion = self.ui.catDesText.text()

            if nombre != "" and descripcion != "":
                if pressed == "add":
                    self.data.addCategoria(nombre, descripcion)
                if pressed == "edit":
                    self.data.editCategoria(codigo, nombre, descripcion)
                    self.clearCod()
                self.clear()
                self.fillTable()
                self.switchDisable(False)
            else:
                functions.popQMessageBox(constants.TYPE_WARNING, "Error en el guardado", constants.LOGIN_MSJ3)

        self.ui.catClearButton.clicked.connect(self.clear)
        self.ui.catSaveButton.clicked.connect(save)
        self.ui.catCancelButton.clicked.connect(cancel)
        self.ui.catAddButton.clicked.connect(add)
        self.ui.catEditButton.clicked.connect(edit)
        self.ui.catDelButton.clicked.connect(delete)

        self.ui.catTable.itemClicked.connect(selectItem)
        functions.theme(self.ui.frame, constants.moduleTheme)
        self.reset()

    def reset(self):
        self.clear()
        self.fillTable()
        self.switchDisable(False)

    def clearCod(self):
        global codigo
        codigo = ""
        self.ui.catTable.setCurrentCell(-1, -1)

    def switchDisable(self, val):
        self.ui.catNomText.setEnabled(val)
        self.ui.catDesText.setEnabled(val)
        self.ui.catClearButton.setEnabled(val)
        self.ui.catSaveButton.setEnabled(val)
        self.ui.catCancelButton.setEnabled(val)

        self.ui.catTable.setEnabled(not val)
        self.ui.catEditButton.setEnabled(not val)
        self.ui.catAddButton.setEnabled(not val)
        self.ui.catDelButton.setEnabled(not val)

    def clear(self):
        self.ui.catNomText.setText("")
        self.ui.catDesText.setText("")

    def fillTable(self):
        data = self.data.getListCategoria()
        self.clearCod()
        self.ui.catTable.clear()
        self.ui.catTable.setColumnCount(3)
        self.ui.catTable.setRowCount(0)
        self.ui.catTable.setHorizontalHeaderLabels(["Codigo", "Nombre", "Descripcion"])
        self.ui.catTable.setColumnHidden(0, True)

        if len(data) != 0:
            self.ui.catTable.setRowCount(len(data))
            numrow = 0
            for row in data:
                numcol = 0
                for col in row:
                    self.ui.catTable.setItem(numrow, numcol, QtWidgets.QTableWidgetItem(str(col)))
                    numcol += 1
                numrow += 1