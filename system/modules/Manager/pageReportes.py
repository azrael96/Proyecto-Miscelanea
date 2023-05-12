from PySide6.QtWidgets import QWidget

from system.resources import constants, functions
from system.views.Manager.ui_reportes import Ui_reportes

codigo = ""
pressed = ""
class ReportesWidget(QWidget):
    def __init__(self, data):
        QWidget.__init__(self)
        self.setObjectName("reportes")
        self.ui = Ui_reportes()
        self.ui.setupUi(self)
        self.data = data

        functions.theme(self.ui.frame, constants.moduleTheme)

    def reset(self):
        pass
