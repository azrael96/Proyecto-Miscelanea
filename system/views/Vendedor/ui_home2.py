# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home2EZLbEQ.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc
import resources_rc

class Ui_home2(object):
    def setupUi(self, home2):
        if not home2.objectName():
            home2.setObjectName(u"home2")
        home2.resize(1182, 608)
        home2.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(home2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(home2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 70))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_17.setFont(font)

        self.verticalLayout_6.addWidget(self.label_17)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_6)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setLayoutDirection(Qt.LeftToRight)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setLayoutDirection(Qt.RightToLeft)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.proFotLabel = QLabel(self.frame_4)
        self.proFotLabel.setObjectName(u"proFotLabel")
        self.proFotLabel.setMinimumSize(QSize(150, 150))
        self.proFotLabel.setMaximumSize(QSize(200, 200))
        self.proFotLabel.setPixmap(QPixmap(u":/images/images/images/Icon.png"))
        self.proFotLabel.setScaledContents(True)
        self.proFotLabel.setAlignment(Qt.AlignCenter)
        self.proFotLabel.setMargin(10)

        self.horizontalLayout_2.addWidget(self.proFotLabel)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.textWelcome = QLabel(self.frame_3)
        self.textWelcome.setObjectName(u"textWelcome")
        self.textWelcome.setStyleSheet(u"color: #8BC34A;\n"
"font: 30pt;")
        self.textWelcome.setTextFormat(Qt.PlainText)
        self.textWelcome.setAlignment(Qt.AlignCenter)
        self.textWelcome.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.textWelcome)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.tags_2 = QFrame(self.frame_8)
        self.tags_2.setObjectName(u"tags_2")
        self.tags_2.setMaximumSize(QSize(16777215, 16777215))
        self.tags_2.setFrameShape(QFrame.StyledPanel)
        self.tags_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.tags_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_7 = QLabel(self.tags_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 25))
        self.label_7.setStyleSheet(u"color: #3B7447;\n"
"font: 16pt;")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_7)

        self.textDate = QLabel(self.tags_2)
        self.textDate.setObjectName(u"textDate")
        self.textDate.setMinimumSize(QSize(0, 25))
        self.textDate.setStyleSheet(u"color: #6AAB6D;\n"
"font: 25pt;")
        self.textDate.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_7.addWidget(self.textDate)


        self.horizontalLayout_4.addWidget(self.tags_2)

        self.fills_2 = QFrame(self.frame_8)
        self.fills_2.setObjectName(u"fills_2")
        self.fills_2.setFrameShape(QFrame.StyledPanel)
        self.fills_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.fills_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, -1, -1, -1)
        self.label_8 = QLabel(self.fills_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 25))
        self.label_8.setStyleSheet(u"color: #3B7447;\n"
"font: 16pt;")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_8)

        self.textTime = QLabel(self.fills_2)
        self.textTime.setObjectName(u"textTime")
        self.textTime.setMinimumSize(QSize(0, 25))
        self.textTime.setStyleSheet(u"color: #6AAB6D;\n"
"font: 25pt;")
        self.textTime.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_8.addWidget(self.textTime)


        self.horizontalLayout_4.addWidget(self.fills_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_16 = QLabel(self.frame_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 70))
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(u"#label_16{\n"
"border-left: 5px;\n"
"border: 5px;\n"
"border-style: solid;\n"
"border-color: #e6e6cc;\n"
"background-color: #f0f0e4;\n"
"}   ")
        self.label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.label_16)

        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"#frame_2{\n"
"border-left: 5px;\n"
"border-bottom: 5px;\n"
"border-right: 5px;\n"
"border-style: solid;\n"
"border-color: #e6e6cc;\n"
"background-color: #f0f0e4;\n"
"}   ")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tags = QFrame(self.frame_2)
        self.tags.setObjectName(u"tags")
        self.tags.setMaximumSize(QSize(180, 16777215))
        self.tags.setFrameShape(QFrame.StyledPanel)
        self.tags.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.tags)
        self.verticalLayout_2.setSpacing(25)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.tags)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 25))
        self.label_2.setStyleSheet(u"color: #3B7447;\n"
"font: 18pt;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.tags)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 25))
        self.label_3.setStyleSheet(u"color: #3B7447;\n"
"font: 18pt;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.tags)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 25))
        self.label_4.setStyleSheet(u"color: #3B7447;\n"
"font: 18pt;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(self.tags)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 25))
        self.label_5.setStyleSheet(u"color: #3B7447;\n"
"font: 18pt;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.tags)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 25))
        self.label_6.setStyleSheet(u"color: #3B7447;\n"
"font: 18pt;")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_9 = QLabel(self.tags)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 25))
        self.label_9.setStyleSheet(u"color: #3B7447;\n"
"font: 18pt;")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_9)

        self.label_10 = QLabel(self.tags)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 25))
        self.label_10.setStyleSheet(u"color: #3B7447;\n"
"font: 18pt;")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_10)


        self.horizontalLayout.addWidget(self.tags)

        self.fills = QFrame(self.frame_2)
        self.fills.setObjectName(u"fills")
        self.fills.setFrameShape(QFrame.StyledPanel)
        self.fills.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.fills)
        self.verticalLayout_3.setSpacing(25)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.textUser = QLabel(self.fills)
        self.textUser.setObjectName(u"textUser")
        self.textUser.setMinimumSize(QSize(0, 25))
        self.textUser.setStyleSheet(u"color: black;\n"
"font: 18pt;")

        self.verticalLayout_3.addWidget(self.textUser)

        self.textCed = QLabel(self.fills)
        self.textCed.setObjectName(u"textCed")
        self.textCed.setMinimumSize(QSize(0, 25))
        self.textCed.setStyleSheet(u"color: black;\n"
"font: 18pt;")

        self.verticalLayout_3.addWidget(self.textCed)

        self.textDir = QLabel(self.fills)
        self.textDir.setObjectName(u"textDir")
        self.textDir.setMinimumSize(QSize(0, 25))
        self.textDir.setStyleSheet(u"color: black;\n"
"font: 18pt;")

        self.verticalLayout_3.addWidget(self.textDir)

        self.textTel = QLabel(self.fills)
        self.textTel.setObjectName(u"textTel")
        self.textTel.setMinimumSize(QSize(0, 25))
        self.textTel.setStyleSheet(u"color: black;\n"
"font: 18pt;")

        self.verticalLayout_3.addWidget(self.textTel)

        self.textRol = QLabel(self.fills)
        self.textRol.setObjectName(u"textRol")
        self.textRol.setMinimumSize(QSize(0, 25))
        self.textRol.setStyleSheet(u"color: black;\n"
"font: 18pt;")

        self.verticalLayout_3.addWidget(self.textRol)

        self.textApertura = QLabel(self.fills)
        self.textApertura.setObjectName(u"textApertura")
        self.textApertura.setMinimumSize(QSize(0, 25))
        self.textApertura.setStyleSheet(u"color: black;\n"
"font: 18pt;")
        self.textApertura.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.textApertura)

        self.textCierre = QLabel(self.fills)
        self.textCierre.setObjectName(u"textCierre")
        self.textCierre.setMinimumSize(QSize(0, 25))
        self.textCierre.setStyleSheet(u"color: black;\n"
"font: 18pt;")
        self.textCierre.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.textCierre)


        self.horizontalLayout.addWidget(self.fills)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 9, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.proAddButton = QPushButton(self.frame_9)
        self.proAddButton.setObjectName(u"proAddButton")
        self.proAddButton.setMinimumSize(QSize(120, 30))
        self.proAddButton.setMaximumSize(QSize(500, 30))
        self.proAddButton.setFont(font)
        self.proAddButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.proAddButton.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #6AAB6D;\n"
"    border-radius: 5px;\n"
"    color: #6AAB6D;\n"
"    background-color: #343b48;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #83B986;\n"
"    border: 2px solid #83B986;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #388E3C;\n"
"    border: 2px solid #FFF59D;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #dbdbdb;\n"
"    border: 2px solid #808080;\n"
"    background-color: #4d4d4d;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-check-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.proAddButton.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.proAddButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_5.addWidget(self.frame_9)


        self.horizontalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_6.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(home2)

        QMetaObject.connectSlotsByName(home2)
    # setupUi

    def retranslateUi(self, home2):
        home2.setWindowTitle(QCoreApplication.translate("home2", u"Form", None))
        self.label_17.setText(QCoreApplication.translate("home2", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:700;\">Sistema de Informaci\u00f3n Miscelanea Iv\u00e1n</span></p></body></html>", None))
        self.textWelcome.setText(QCoreApplication.translate("home2", u"Bienvenido, Wilmar Alexander Rodriguez Bueno", None))
        self.label_7.setText(QCoreApplication.translate("home2", u"Fecha:", None))
        self.textDate.setText(QCoreApplication.translate("home2", u"Fecha", None))
        self.label_8.setText(QCoreApplication.translate("home2", u"Hora:", None))
        self.textTime.setText(QCoreApplication.translate("home2", u"Hora", None))
        self.label_16.setText(QCoreApplication.translate("home2", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700;\">Datos del Usuario</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("home2", u"Alias:", None))
        self.label_3.setText(QCoreApplication.translate("home2", u"C\u00e9dula:", None))
        self.label_4.setText(QCoreApplication.translate("home2", u"Direcci\u00f3n:", None))
        self.label_5.setText(QCoreApplication.translate("home2", u"Tel\u00e9fono:", None))
        self.label_6.setText(QCoreApplication.translate("home2", u"Rol:", None))
        self.label_9.setText(QCoreApplication.translate("home2", u"Valor Apertura:", None))
        self.label_10.setText(QCoreApplication.translate("home2", u"Valor Cierre:", None))
        self.textUser.setText(QCoreApplication.translate("home2", u"Usuario", None))
        self.textCed.setText(QCoreApplication.translate("home2", u"C\u00e9dula", None))
        self.textDir.setText(QCoreApplication.translate("home2", u"Direcci\u00f3n", None))
        self.textTel.setText(QCoreApplication.translate("home2", u"Tel\u00e9fono", None))
        self.textRol.setText(QCoreApplication.translate("home2", u"Rol", None))
        self.textApertura.setText(QCoreApplication.translate("home2", u"apertura", None))
        self.textCierre.setText(QCoreApplication.translate("home2", u"cierre", None))
        self.proAddButton.setText(QCoreApplication.translate("home2", u"Cerrar Caja", None))
    # retranslateUi

