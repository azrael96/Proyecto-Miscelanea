# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clienteejyOrx.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(368, 459)
        self.horizontalLayout_4 = QHBoxLayout(Dialog)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame {\n"
"    background-color: #f8f8f2;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.frame_4)
        self.label_23.setObjectName(u"label_23")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_23.setFont(font)
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_23)

        self.labelVersion_14 = QLabel(self.frame_4)
        self.labelVersion_14.setObjectName(u"labelVersion_14")
        self.labelVersion_14.setLineWidth(1)
        self.labelVersion_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.labelVersion_14)

        self.usuCedText = QLineEdit(self.frame_4)
        self.usuCedText.setObjectName(u"usuCedText")
        self.usuCedText.setMinimumSize(QSize(0, 30))
        self.usuCedText.setFrame(True)
        self.usuCedText.setEchoMode(QLineEdit.Normal)

        self.verticalLayout.addWidget(self.usuCedText)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cliButtonVer = QPushButton(self.frame_5)
        self.cliButtonVer.setObjectName(u"cliButtonVer")
        self.cliButtonVer.setMinimumSize(QSize(150, 30))
        self.cliButtonVer.setFont(font)
        self.cliButtonVer.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cliButtonVer.setIcon(icon)

        self.horizontalLayout.addWidget(self.cliButtonVer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.labelError = QLabel(self.frame_2)
        self.labelError.setObjectName(u"labelError")
        self.labelError.setLineWidth(1)
        self.labelError.setTextFormat(Qt.RichText)
        self.labelError.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.labelError)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.frame_23 = QFrame(self.frame_2)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.formLayout_7 = QFormLayout(self.frame_23)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setContentsMargins(0, 0, 0, 0)
        self.labelVersion_12 = QLabel(self.frame_23)
        self.labelVersion_12.setObjectName(u"labelVersion_12")
        self.labelVersion_12.setLineWidth(1)
        self.labelVersion_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.labelVersion_12)

        self.usuNomText = QLineEdit(self.frame_23)
        self.usuNomText.setObjectName(u"usuNomText")
        self.usuNomText.setMinimumSize(QSize(0, 30))

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.usuNomText)

        self.labelVersion_20 = QLabel(self.frame_23)
        self.labelVersion_20.setObjectName(u"labelVersion_20")
        self.labelVersion_20.setLineWidth(1)
        self.labelVersion_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.labelVersion_20)

        self.usuNom2Text = QLineEdit(self.frame_23)
        self.usuNom2Text.setObjectName(u"usuNom2Text")
        self.usuNom2Text.setMinimumSize(QSize(0, 30))

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.usuNom2Text)

        self.labelVersion_21 = QLabel(self.frame_23)
        self.labelVersion_21.setObjectName(u"labelVersion_21")
        self.labelVersion_21.setLineWidth(1)
        self.labelVersion_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_7.setWidget(2, QFormLayout.LabelRole, self.labelVersion_21)

        self.usuApe1Text = QLineEdit(self.frame_23)
        self.usuApe1Text.setObjectName(u"usuApe1Text")
        self.usuApe1Text.setMinimumSize(QSize(0, 30))

        self.formLayout_7.setWidget(2, QFormLayout.FieldRole, self.usuApe1Text)

        self.labelVersion_22 = QLabel(self.frame_23)
        self.labelVersion_22.setObjectName(u"labelVersion_22")
        self.labelVersion_22.setLineWidth(1)
        self.labelVersion_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_7.setWidget(3, QFormLayout.LabelRole, self.labelVersion_22)

        self.usuApe2Text = QLineEdit(self.frame_23)
        self.usuApe2Text.setObjectName(u"usuApe2Text")
        self.usuApe2Text.setMinimumSize(QSize(0, 30))

        self.formLayout_7.setWidget(3, QFormLayout.FieldRole, self.usuApe2Text)

        self.labelVersion_13 = QLabel(self.frame_23)
        self.labelVersion_13.setObjectName(u"labelVersion_13")
        self.labelVersion_13.setLineWidth(1)
        self.labelVersion_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_7.setWidget(4, QFormLayout.LabelRole, self.labelVersion_13)

        self.usuDirText = QLineEdit(self.frame_23)
        self.usuDirText.setObjectName(u"usuDirText")
        self.usuDirText.setMinimumSize(QSize(0, 30))

        self.formLayout_7.setWidget(4, QFormLayout.FieldRole, self.usuDirText)

        self.labelVersion_15 = QLabel(self.frame_23)
        self.labelVersion_15.setObjectName(u"labelVersion_15")
        self.labelVersion_15.setLineWidth(1)
        self.labelVersion_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_7.setWidget(5, QFormLayout.LabelRole, self.labelVersion_15)

        self.usuTelText = QLineEdit(self.frame_23)
        self.usuTelText.setObjectName(u"usuTelText")
        self.usuTelText.setMinimumSize(QSize(0, 30))

        self.formLayout_7.setWidget(5, QFormLayout.FieldRole, self.usuTelText)


        self.verticalLayout_2.addWidget(self.frame_23)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.cliButtonFac = QPushButton(self.frame_3)
        self.cliButtonFac.setObjectName(u"cliButtonFac")
        self.cliButtonFac.setMinimumSize(QSize(150, 30))
        self.cliButtonFac.setFont(font)
        self.cliButtonFac.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-input.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cliButtonFac.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.cliButtonFac)

        self.cliButtonCan = QPushButton(self.frame_3)
        self.cliButtonCan.setObjectName(u"cliButtonCan")
        self.cliButtonCan.setMinimumSize(QSize(150, 30))
        self.cliButtonCan.setFont(font)
        self.cliButtonCan.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cliButtonCan.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.cliButtonCan)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.horizontalLayout_4.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_23.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Informaci\u00f3n del Cliente a Facturar</span></p></body></html>", None))
        self.labelVersion_14.setText(QCoreApplication.translate("Dialog", u"C\u00e9dula:", None))
        self.usuCedText.setText("")
        self.usuCedText.setPlaceholderText(QCoreApplication.translate("Dialog", u"Ingrese la c\u00e9dula", None))
        self.cliButtonVer.setText(QCoreApplication.translate("Dialog", u"Verificar", None))
        self.labelError.setText("")
        self.labelVersion_12.setText(QCoreApplication.translate("Dialog", u"Nombre1", None))
        self.usuNomText.setText("")
        self.usuNomText.setPlaceholderText(QCoreApplication.translate("Dialog", u"Ingrese el primer nombre", None))
        self.labelVersion_20.setText(QCoreApplication.translate("Dialog", u"Nombre2", None))
        self.usuNom2Text.setText("")
        self.usuNom2Text.setPlaceholderText(QCoreApplication.translate("Dialog", u"Ingrese el segundo nombre", None))
        self.labelVersion_21.setText(QCoreApplication.translate("Dialog", u"Apellido1", None))
        self.usuApe1Text.setText("")
        self.usuApe1Text.setPlaceholderText(QCoreApplication.translate("Dialog", u"Ingrese el primer apellido", None))
        self.labelVersion_22.setText(QCoreApplication.translate("Dialog", u"Apellido2", None))
        self.usuApe2Text.setText("")
        self.usuApe2Text.setPlaceholderText(QCoreApplication.translate("Dialog", u"Ingrese el segundo apellido", None))
        self.labelVersion_13.setText(QCoreApplication.translate("Dialog", u"Direcci\u00f3n", None))
        self.usuDirText.setText("")
        self.usuDirText.setPlaceholderText(QCoreApplication.translate("Dialog", u"Ingrese la direcci\u00f3n", None))
        self.labelVersion_15.setText(QCoreApplication.translate("Dialog", u"Tel\u00e9fono", None))
        self.usuTelText.setText("")
        self.usuTelText.setPlaceholderText(QCoreApplication.translate("Dialog", u"Ingrese el tel\u00e9fono", None))
        self.cliButtonFac.setText(QCoreApplication.translate("Dialog", u"Facturar", None))
        self.cliButtonCan.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
    # retranslateUi

