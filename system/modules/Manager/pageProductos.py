from PySide6 import QtWidgets
from PySide6.QtCore import QObject, QByteArray, QBuffer, QIODevice
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtGui import QPixmap

from system.resources import constants, functions, convertor
from system.views.Manager.ui_productos import Ui_productos

codigo = ""
pressed = ""
cat_dic = {}
imgPath = ""

class ProductosWidget(QWidget):
    def __init__(self, data):
        QWidget.__init__(self)
        self.setObjectName("productos")
        self.ui = Ui_productos()
        self.ui.setupUi(self)
        self.data = data

        def switchDelDisable(val):
            self.ui.proNomText.setEnabled(val)
            self.ui.proDesText.setEnabled(val)
            self.ui.proCatCombo.setEnabled(val)
            self.ui.proClearButton.setEnabled(val)
            self.ui.proAddIMGButton.setEnabled(val)
            self.ui.proDelIMGButton.setEnabled(val)

        def selectItem():
            def selectImg():
                pix = QPixmap()
                bydata = self.data.getFotoProducto(codigo)
                if pix.loadFromData(bydata[0]):
                    self.ui.proFotLabel.setPixmap(pix)

            global codigo
            row = self.ui.proTable.currentRow()
            codigo = self.ui.proTable.item(row, 0).text()
            nom = self.ui.proTable.item(row, 1).text()
            des = self.ui.proTable.item(row, 2).text()
            cat = self.ui.proTable.item(row, 3).text()

            self.ui.proNomText.setText(nom)
            self.ui.proDesText.setText(des)
            self.ui.proCatCombo.setCurrentText(cat)
            selectImg()

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
            def pixToByte(pix):
                ba = QByteArray()
                buff = QBuffer(ba)
                buff.open(QIODevice.WriteOnly)
                pix.save(buff, "PNG")
                return ba.data()

            global codigo, pressed, imgPath

            if pressed == "del":
                self.data.delProducto(codigo)
                switchDelDisable(True)

            nom = self.ui.proNomText.text()
            des = self.ui.proDesText.text()
            cat = self.ui.proCatCombo.currentText()
            foto = self.ui.proFotLabel.pixmap()
            fotoBytes = pixToByte(foto)

            if nom != "" and des != "" and cat != "" and foto.depth() != 0:
                if pressed == "add":
                    self.data.addProducto(nom, des, fotoBytes, cat_dic[cat])
                if pressed == "edit":
                    self.data.editProducto(codigo, nom, des, fotoBytes, cat_dic[cat])
                    self.clearCod()
                self.clear()
                self.fillTable()
                self.switchDisable(False)
            else:
                functions.popQMessageBox(constants.TYPE_WARNING, "Error en el proceso", constants.LOGIN_MSJ3)

        def addImg():
            fileName = QFileDialog.getOpenFileName(self, QObject.tr("Open Image"), "/home", QObject.tr("Image Files (*.png *.jpg *.bmp)"))
            fileByte = convertor.convertToBinaryData(fileName[0])
            if fileByte != False:
                pix = QPixmap()
                if pix.loadFromData(fileByte):
                    self.ui.proFotLabel.setPixmap(pix)
                    global imgPath
                    imgPath = fileName[0]
            else:
                functions.popQMessageBox(constants.TYPE_WARNING, "Error en el proceso", constants.MSJ_IMG)

        self.ui.proClearButton.clicked.connect(self.clear)
        self.ui.proSaveButton.clicked.connect(save)
        self.ui.proCancelButton.clicked.connect(cancel)
        self.ui.proAddButton.clicked.connect(add)
        self.ui.proEditButton.clicked.connect(edit)
        self.ui.proDelButton.clicked.connect(delete)
        self.ui.proAddIMGButton.clicked.connect(addImg)
        self.ui.proDelIMGButton.clicked.connect(self.delImg)

        functions.theme(self.ui.frame, constants.moduleTheme)
        self.ui.proTable.itemClicked.connect(selectItem)

        self.reset()

    def reset(self):
        self.clear()
        self.fillTable()
        self.fillCombo()
        self.switchDisable(False)

    def delImg(self):
        self.ui.proFotLabel.setPixmap(QPixmap())

    def clear(self):
        self.ui.proNomText.setText("")
        self.ui.proDesText.setText("")
        self.ui.proCatCombo.setCurrentIndex(-1)
        self.delImg()

    def clearCod(self):
        global codigo
        codigo = ""
        self.ui.proTable.setCurrentCell(-1, -1)

    def fillTable(self):
        data = self.data.getListProducto("", "")
        self.clearCod()
        self.ui.proTable.clear()
        self.ui.proTable.setColumnCount(4)
        self.ui.proTable.setRowCount(0)
        self.ui.proTable.setHorizontalHeaderLabels(["ID", "Nombre", "Descripción", "Categoria"])
        self.ui.proTable.setColumnHidden(0, True)
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

        self.ui.proCatCombo.clear()
        self.ui.proCatCombo.setCurrentIndex(-1)

        if len(data) != 0:
            global cat_dic
            cat_list = []
            for row in data:
                cat_dic[row[1]] = row[0]
                cat_list.append(self.tr(row[1]))
            self.ui.proCatCombo.addItems(cat_list)

    def switchDisable(self, val):
        self.ui.proNomText.setEnabled(val)
        self.ui.proDesText.setEnabled(val)
        self.ui.proCatCombo.setEnabled(val)
        self.ui.proClearButton.setEnabled(val)
        self.ui.proSaveButton.setEnabled(val)
        self.ui.proCancelButton.setEnabled(val)
        self.ui.proAddIMGButton.setEnabled(val)
        self.ui.proDelIMGButton.setEnabled(val)

        self.ui.proTable.setEnabled(not val)
        self.ui.proEditButton.setEnabled(not val)
        self.ui.proAddButton.setEnabled(not val)
        self.ui.proDelButton.setEnabled(not val)

