from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QWidget
from datetime import date as fecha

from system.resources import constants, functions, pdf_printer
from system.views.Vendedor.ui_servicios import Ui_servicios
from system.modules.Vendedor.clienteDialog import ClientDialog

rx20 = ("^[0-9]{20}$")
class ServiciosWidget(QWidget):
    def __init__(self, data, caja):
        QWidget.__init__(self)
        self.setObjectName("servicios")
        self.ui = Ui_servicios()
        self.ui.setupUi(self)
        self.data = data
        self.caja = caja

        self.ui.textValor.setValidator(QRegularExpressionValidator(rx20, self))
        self.ui.textCant.setValidator(QRegularExpressionValidator(rx20, self))

        def registrar():
            nom = self.ui.comboBoxNom.currentText()
            valor = self.ui.textValor.text()
            cant = self.ui.textCant.text()

            if valor != "" and cant != "":
                caj = self.caja
                date = fecha.today()

                dlgClient = ClientDialog(self.data)
                dlgClient.exec()
                cli = dlgClient.ui.usuCedText.text()

                if cli != "":
                    total = float(valor) * float(cant)
                    factura = self.data.addFactura("Efectivo", date, total, caj, cli)
                    self.data.addServicio(nom, valor, cant, factura)

                    pdf_printer.makeFacturaPDF(self.data.getInfoFacturaSer(factura), factura)
                    functions.popQMessageBox(constants.TYPE_INFO, "Factura exitosa", "Factura guardada en el pdf con nombre: fac" + str(factura))
                    self.reset()
                else:
                    functions.popQMessageBox(constants.TYPE_CRITIC, "Factura cancelada", "Se canceló el proceso de facturación")
            else:
                functions.popQMessageBox(constants.TYPE_WARNING, "Error en el proceso", constants.LOGIN_MSJ3)

        functions.theme(self.ui.frame, constants.moduleTheme)
        self.ui.registrarButton.clicked.connect(registrar)
        self.reset()

    def reset(self):
        self.clearStart()
        self.fillCombo()

    def clearStart(self):
        self.ui.textValor.setText("")
        self.ui.textCant.setText("")
        self.ui.comboBoxNom.setCurrentIndex(-1)

    def fillCombo(self):
        met_list = ["Fotocopiado", "Impresión", "Laminado"]
        self.ui.comboBoxNom.clear()
        self.ui.comboBoxNom.addItems(met_list)
        self.ui.comboBoxNom.setCurrentIndex(-1)