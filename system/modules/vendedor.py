from datetime import datetime

from system.resources import constants, functions, connector

from system.modules.Vendedor.pageVentas import VentasWidget
from system.modules.Vendedor.pageServicios import ServiciosWidget
from system.modules.Vendedor.pageGastos import GastosWidget
from system.modules.Vendedor.pageStock import StockWidget
from system.modules.Vendedor.pageDeudas import DeudasWidget
from system.modules.Vendedor.pageHome2 import Home2Widget

from system.views.ui_Vendedor import Ui_MainWindow as Ui_VendedorWindow

from PySide6.QtCore import QEvent, QTimer
from PySide6.QtGui import Qt, QColor
from PySide6.QtWidgets import QMainWindow, QGraphicsDropShadowEffect, QPushButton, QSizeGrip

class MainWindow(QMainWindow):
    def __init__(self, usercod):
        QMainWindow.__init__(self)
        self.ui = Ui_VendedorWindow()
        self.ui.setupUi(self)
        self.data = connector.DatabaseLink()

        #CREATE THE MODULES
        fecha = datetime.now().strftime("%Y-%m-%d")
        caja = self.data.addCaja(fecha, usercod)

        self.moduleVentas = VentasWidget(self.data, caja[0])
        self.moduleServicios = ServiciosWidget(self.data, caja[0])
        self.moduleGastos = GastosWidget(self.data, caja[0])
        self.moduleStock = StockWidget(self.data)
        self.moduleDeudas = DeudasWidget(self.data, caja[0])
        self.moduleHome2 = Home2Widget(self.data, usercod, caja[1], caja[0], self)

        def configEvents():
            # DOUBLE CLICK TO MAXIMIZE
            def dobleClickMaximizeRestore(event):
                if event.type() == QEvent.MouseButtonDblClick:
                    QTimer.singleShot(250, lambda: functions.maximize_restore(self))

            # MOVE WINDOW / MAXIMIZE / RESTORE
            def moveWindow(event):
                # IF MAXIMIZED CHANGE TO NORMAL
                if functions.returnStatus(self):
                    functions.maximize_restore(self)
                # MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
                    self.dragPos = event.globalPosition().toPoint()
                    event.accept()

            self.ui.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore
            self.ui.titleRightInfo.mouseMoveEvent = moveWindow

        def configVisual():

            #BASIC ATRIBUTES
            self.setWindowTitle(constants.title)
            self.ui.titleRightInfo.setText(constants.manager)
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground, True)

            # DROP SHADOW
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(0)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 100, 0, 150))
            self.ui.bgApp.setGraphicsEffect(self.shadow)

            # RESIZE WINDOW
            self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
            self.sizegrip.setStyleSheet("width: 20px; height: 20px;")

            # SET CUSTOM THEME
            functions.theme(self.ui.styleSheet, constants.mainTheme)

        def configButtons():
            # EXTRA LEFT BOX
            def openCloseLeftBox():
                functions.toggleLeftBox(self, True)

            # EXTRA RIGHT BOX
            def openCloseRightBox():
                functions.toggleRightBox(self, True)

            # OPEN MENU BUTTONS
            self.ui.toggleButton.clicked.connect(lambda: functions.toggleMenu(self, True))
            self.ui.toggleLeftBox.clicked.connect(openCloseLeftBox)
            self.ui.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)
            self.ui.settingsTopBtn.clicked.connect(openCloseRightBox)

            # MINIMIZE
            self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

            # MAXIMIZE
            self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: functions.maximize_restore(self))

            # CLOSE APPLICATION
            self.ui.closeAppBtn.clicked.connect(lambda: self.close())
            #Make invisible no use buttons
            self.ui.closeAppBtn.setVisible(False)
            self.ui.settingsTopBtn.setVisible(False)

            # LEFT MENUS
            self.ui.btn_home.clicked.connect(self.buttonClick)
            self.ui.btn_ventas.clicked.connect(self.buttonClick)
            self.ui.btn_servicios.clicked.connect(self.buttonClick)
            self.ui.btn_gastos.clicked.connect(self.buttonClick)
            self.ui.btn_deudas.clicked.connect(self.buttonClick)
            self.ui.btn_stock.clicked.connect(self.buttonClick)

        def configModules():
            # ADD THE SYSTEM MODULES
            self.ui.stackedWidget.addWidget(self.moduleHome2)
            self.ui.stackedWidget.addWidget(self.moduleVentas)
            self.ui.stackedWidget.addWidget(self.moduleServicios)
            self.ui.stackedWidget.addWidget(self.moduleGastos)
            self.ui.stackedWidget.addWidget(self.moduleStock)
            self.ui.stackedWidget.addWidget(self.moduleDeudas)

            # SET THE STARTING MODULE
            self.ui.stackedWidget.setCurrentWidget(self.moduleHome2)

        # BASIC CONFIGURATION
        configModules()
        configEvents()
        configVisual()
        configButtons()

        #SHOW THE WINDOW
        self.show()

    # MENU BUTTONS FUNCTIONS
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SELECT MENU STYLE
        def selectMenu(getStyle):
            select = getStyle + functions.MENU_SELECTED_STYLESHEET
            return select

        # DESELECT MENU STYLE
        def deselectMenu(getStyle):
            deselect = getStyle.replace(functions.MENU_SELECTED_STYLESHEET, "")
            return deselect

        # RESET SELECTION
        def resetStyle(widget):
            for w in self.ui.topMenu.findChildren(QPushButton):
                if w.objectName() != widget:
                    w.setStyleSheet(deselectMenu(w.styleSheet()))

        # CONNECT MENU BUTTONS TO WIDGET
        if btnName == "btn_home":
            self.moduleHome2.reset()
            self.ui.stackedWidget.setCurrentWidget(self.moduleHome2)

        if btnName == "btn_ventas":
            self.moduleVentas.reset()
            self.ui.stackedWidget.setCurrentWidget(self.moduleVentas)

        if btnName == "btn_servicios":
            self.moduleServicios.reset()
            self.ui.stackedWidget.setCurrentWidget(self.moduleServicios)

        if btnName == "btn_gastos":
            self.moduleGastos.reset()
            self.ui.stackedWidget.setCurrentWidget(self.moduleGastos)

        if btnName == "btn_stock":
            self.moduleStock.reset()
            self.ui.stackedWidget.setCurrentWidget(self.moduleStock)

        if btnName == "btn_deudas":
            self.moduleDeudas.reset()
            self.ui.stackedWidget.setCurrentWidget(self.moduleDeudas)

        resetStyle(btnName)
        btn.setStyleSheet(selectMenu(btn.styleSheet()))

    # MOUSE CLICK EVENTS
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()