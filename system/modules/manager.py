from system.resources import constants, functions, connector
from system.modules.Manager.pageCategorias import CategoriasWidget
from system.modules.Manager.pageUsuarios import UsuariosWidget
from system.modules.Manager.pageProductos import ProductosWidget
from system.modules.Manager.pagePedidos import PedidosWidget
from system.modules.Manager.pageInventario import InventarioWidget
from system.modules.Manager.pageHome import HomeWidget
from system.modules.Manager.pageReportes import ReportesWidget
from system.views.ui_Manager import Ui_MainWindow as Ui_ManagerWindow

from PySide6.QtCore import QEvent, QTimer
from PySide6.QtGui import Qt, QColor
from PySide6.QtWidgets import QMainWindow, QGraphicsDropShadowEffect, QPushButton, QSizeGrip

class MainWindow(QMainWindow):
    def __init__(self, usercod):
        QMainWindow.__init__(self)
        self.ui = Ui_ManagerWindow()
        self.ui.setupUi(self)
        self.data = connector.DatabaseLink()

        #CREATE THE MODULES
        self.moduleCategorias = CategoriasWidget(self.data)
        self.moduleUsuarios = UsuariosWidget(self.data)
        self.moduleProductos = ProductosWidget(self.data)
        self.modulePedidos = PedidosWidget(self.data)
        self.moduleInventario = InventarioWidget(self.data)
        self.moduleHome = HomeWidget(self.data, usercod)
        self.moduleReportes = ReportesWidget(self.data)

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
            self.shadow.setBlurRadius(20)
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

            # LEFT MENUS
            self.ui.btn_home.clicked.connect(self.buttonClick)
            self.ui.btn_pedidos.clicked.connect(self.buttonClick)
            self.ui.btn_reportes.clicked.connect(self.buttonClick)
            self.ui.btn_inventario.clicked.connect(self.buttonClick)
            self.ui.btn_usuarios.clicked.connect(self.buttonClick)
            self.ui.btn_categorias.clicked.connect(self.buttonClick)
            self.ui.btn_productos.clicked.connect(self.buttonClick)

            # Make invisible no use buttons
            self.ui.settingsTopBtn.setVisible(False)

        def configModules():
            # ADD THE SYSTEM MODULES
            self.ui.stackedWidget.addWidget(self.moduleCategorias)
            self.ui.stackedWidget.addWidget(self.moduleUsuarios)
            self.ui.stackedWidget.addWidget(self.moduleProductos)
            self.ui.stackedWidget.addWidget(self.modulePedidos)
            self.ui.stackedWidget.addWidget(self.moduleInventario)
            self.ui.stackedWidget.addWidget(self.moduleHome)
            self.ui.stackedWidget.addWidget(self.moduleReportes)

            # SET THE STARTING MODULE
            self.ui.stackedWidget.setCurrentWidget(self.moduleHome)

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
            self.moduleHome.reset()
            self.ui.stackedWidget.setCurrentWidget(self.moduleHome)

        if btnName == "btn_pedidos":
            self.modulePedidos.reset()
            self.ui.stackedWidget.setCurrentWidget(self.modulePedidos)

        if btnName == "btn_reportes":
            self.moduleReportes.reset()
            self.ui.stackedWidget.setCurrentWidget(self.moduleReportes)

        if btnName == "btn_inventario":
            self.moduleInventario.reset()
            self.ui.stackedWidget.setCurrentWidget(self.moduleInventario)

        if btnName == "btn_usuarios":
            self.moduleUsuarios.reset()
            self.ui.stackedWidget.setCurrentWidget(self.moduleUsuarios)

        if btnName == "btn_categorias":
            self.moduleCategorias.reset()
            self.ui.stackedWidget.setCurrentWidget(self.moduleCategorias)

        if btnName == "btn_productos":
            self.moduleProductos.reset()
            self.ui.stackedWidget.setCurrentWidget(self.moduleProductos)

        resetStyle(btnName)
        btn.setStyleSheet(selectMenu(btn.styleSheet()))

    # MOUSE CLICK EVENTS
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()