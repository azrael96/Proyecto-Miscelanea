# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'serviciosETXcTs.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_servicios(object):
    def setupUi(self, servicios):
        if not servicios.objectName():
            servicios.setObjectName(u"servicios")
        servicios.resize(1182, 608)
        servicios.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(servicios)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(servicios)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.label_2)

        self.verticalSpacer_4 = QSpacerItem(20, 146, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_16 = QFrame(self.frame_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_16)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_17 = QLabel(self.frame_16)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.verticalLayout_22.addWidget(self.label_17)

        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.formLayout_6 = QFormLayout(self.frame_18)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.labelVersion_7 = QLabel(self.frame_18)
        self.labelVersion_7.setObjectName(u"labelVersion_7")
        self.labelVersion_7.setLineWidth(1)
        self.labelVersion_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.labelVersion_7)

        self.comboBoxNom = QComboBox(self.frame_18)
        self.comboBoxNom.setObjectName(u"comboBoxNom")
        self.comboBoxNom.setFont(font)
        self.comboBoxNom.setAutoFillBackground(False)
        self.comboBoxNom.setIconSize(QSize(16, 16))
        self.comboBoxNom.setFrame(True)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.comboBoxNom)

        self.labelVersion_8 = QLabel(self.frame_18)
        self.labelVersion_8.setObjectName(u"labelVersion_8")
        self.labelVersion_8.setLineWidth(1)
        self.labelVersion_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.labelVersion_8)

        self.textValor = QLineEdit(self.frame_18)
        self.textValor.setObjectName(u"textValor")
        self.textValor.setMinimumSize(QSize(0, 30))

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.textValor)

        self.labelVersion_9 = QLabel(self.frame_18)
        self.labelVersion_9.setObjectName(u"labelVersion_9")
        self.labelVersion_9.setLineWidth(1)
        self.labelVersion_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.labelVersion_9)

        self.textCant = QLineEdit(self.frame_18)
        self.textCant.setObjectName(u"textCant")
        self.textCant.setMinimumSize(QSize(0, 30))

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.textCant)


        self.verticalLayout_22.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_16)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_5)

        self.registrarButton = QPushButton(self.frame_19)
        self.registrarButton.setObjectName(u"registrarButton")
        self.registrarButton.setMinimumSize(QSize(150, 30))
        self.registrarButton.setFont(font)
        self.registrarButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-data-transfer-down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.registrarButton.setIcon(icon)

        self.horizontalLayout_12.addWidget(self.registrarButton)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_6)


        self.verticalLayout_22.addWidget(self.frame_19)


        self.horizontalLayout.addWidget(self.frame_16)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalSpacer_3 = QSpacerItem(20, 146, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(servicios)

        self.comboBoxNom.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(servicios)
    # setupUi

    def retranslateUi(self, servicios):
        servicios.setWindowTitle(QCoreApplication.translate("servicios", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("servicios", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Servicios</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("servicios", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Registrar Servicio</span></p></body></html>", None))
        self.labelVersion_7.setText(QCoreApplication.translate("servicios", u"Seleccionar Servicio", None))
        self.comboBoxNom.setPlaceholderText(QCoreApplication.translate("servicios", u"Seleccione una opci\u00f3n", None))
        self.labelVersion_8.setText(QCoreApplication.translate("servicios", u"Valor Unitario", None))
        self.textValor.setText("")
        self.textValor.setPlaceholderText(QCoreApplication.translate("servicios", u"Ingrese el valor", None))
        self.labelVersion_9.setText(QCoreApplication.translate("servicios", u"Cantidad", None))
        self.textCant.setText("")
        self.textCant.setPlaceholderText(QCoreApplication.translate("servicios", u"Ingrese la cantidad", None))
        self.registrarButton.setText(QCoreApplication.translate("servicios", u"Registrar", None))
    # retranslateUi

