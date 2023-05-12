from PySide6.QtCore import QParallelAnimationGroup, QEasingCurve, QPropertyAnimation, QEvent, QTimer
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMessageBox

from system.resources import constants, functions

GLOBAL_STATE = False
MENU_WIDTH = 240
TIME_ANIMATION = 500
LEFT_BOX_WIDTH = 240
RIGHT_BOX_WIDTH = 240
BTN_LEFT_BOX_COLOR = "background-color: #3C6B4A;"
BTN_RIGHT_BOX_COLOR = "background-color: #FFF59D;"
MENU_SELECTED_STYLESHEET = """
    border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 245, 157, 255), stop:0.5 rgba(85, 170, 255, 0));
    background-color: #3C6B4A;
    """

def popQMessageBox(type, title, msj):
    msgBox = QMessageBox()
    functions.theme(msgBox, constants.msjBoxTheme)
    if type == "Information":
        QMessageBox.information(msgBox, title, msj)
    if type == "Critical":
        QMessageBox.critical(msgBox, title, msj)
    if type == "Warning":
        QMessageBox.warning(msgBox, title, msj)

# RETURN STATUS
def returnStatus(self):
    return GLOBAL_STATE

# MAXIMIZE/RESTORE
def maximize_restore(self):
    global GLOBAL_STATE
    status = GLOBAL_STATE
    if status == False:
        self.showMaximized()
        GLOBAL_STATE = True
        self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
        self.ui.maximizeRestoreAppBtn.setToolTip("Restore")
        self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))
        self.ui.frame_size_grip.hide()
    else:
        GLOBAL_STATE = False
        self.showNormal()
        self.resize(self.width() + 1, self.height() + 1)
        self.ui.appMargins.setContentsMargins(10, 10, 10, 10)
        self.ui.maximizeRestoreAppBtn.setToolTip("Maximize")
        self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))
        self.ui.frame_size_grip.show()

# SET STATUS
def setStatus(self, status):
    global GLOBAL_STATE
    GLOBAL_STATE = status

# TOGGLE MENU
def toggleMenu(self, enable):
    if enable:
        # GET WIDTH
        width = self.ui.leftMenuBg.width()
        maxExtend = MENU_WIDTH
        standard = 60

        # SET MAX WIDTH
        if width == 60:
            widthExtended = maxExtend
        else:
            widthExtended = standard

        # ANIMATION
        self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
        self.animation.setDuration(TIME_ANIMATION)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

# TOGGLE LEFT BOX
def toggleLeftBox(self, enable):
    if enable:
        # GET WIDTH
        width = self.ui.extraLeftBox.width()
        widthRightBox = self.ui.extraRightBox.width()
        maxExtend = LEFT_BOX_WIDTH
        color = BTN_LEFT_BOX_COLOR
        standard = 0

        # GET BTN STYLE
        style = self.ui.toggleLeftBox.styleSheet()

        # SET MAX WIDTH
        if width == 0:
            widthExtended = maxExtend
            # SELECT BTN
            self.ui.toggleLeftBox.setStyleSheet(style + color)
            if widthRightBox != 0:
                style = self.ui.settingsTopBtn.styleSheet()
                self.ui.settingsTopBtn.setStyleSheet(style.replace(BTN_RIGHT_BOX_COLOR, ''))
        else:
            widthExtended = standard
            # RESET BTN
            self.ui.toggleLeftBox.setStyleSheet(style.replace(color, ''))

    start_box_animation(self, width, widthRightBox, "left")

# TOGGLE RIGHT BOX
def toggleRightBox(self, enable):
    if enable:
        # GET WIDTH
        width = self.ui.extraRightBox.width()
        widthLeftBox = self.ui.extraLeftBox.width()
        maxExtend = RIGHT_BOX_WIDTH
        color = BTN_RIGHT_BOX_COLOR
        standard = 0

        # GET BTN STYLE
        style = self.ui.settingsTopBtn.styleSheet()

        # SET MAX WIDTH
        if width == 0:
            widthExtended = maxExtend
            # SELECT BTN
            self.ui.settingsTopBtn.setStyleSheet(style + color)
            if widthLeftBox != 0:
                style = self.ui.toggleLeftBox.styleSheet()
                self.ui.toggleLeftBox.setStyleSheet(style.replace(BTN_LEFT_BOX_COLOR, ''))
        else:
            widthExtended = standard
            # RESET BTN
            self.ui.settingsTopBtn.setStyleSheet(style.replace(color, ''))

        start_box_animation(self, widthLeftBox, width, "right")

# ANIMATION
def start_box_animation(self, left_box_width, right_box_width, direction):
    right_width = 0
    left_width = 0

    # Check values
    if left_box_width == 0 and direction == "left":
        left_width = 240
    else:
        left_width = 0
    # Check values
    if right_box_width == 0 and direction == "right":
        right_width = 240
    else:
        right_width = 0

    # ANIMATION LEFT BOX
    self.left_box = QPropertyAnimation(self.ui.extraLeftBox, b"minimumWidth")
    self.left_box.setDuration(TIME_ANIMATION)
    self.left_box.setStartValue(left_box_width)
    self.left_box.setEndValue(left_width)
    self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

    # ANIMATION RIGHT BOX
    self.right_box = QPropertyAnimation(self.ui.extraRightBox, b"minimumWidth")
    self.right_box.setDuration(TIME_ANIMATION)
    self.right_box.setStartValue(right_box_width)
    self.right_box.setEndValue(right_width)
    self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

    # GROUP ANIMATION
    self.group = QParallelAnimationGroup()
    self.group.addAnimation(self.left_box)
    self.group.addAnimation(self.right_box)
    self.group.start()

# IMPORT THEMES FILES QSS/CSS
def theme(self, file):
    str = open(file, 'r').read()
    self.setStyleSheet(str)

############################################################

# DOUBLE CLICK TO MAXIMIZE
class Person:
    def dobleClickMaximizeRestore(self, event):
        if event.type() == QEvent.MouseButtonDblClick:
            QTimer.singleShot(250, lambda: maximize_restore(self))