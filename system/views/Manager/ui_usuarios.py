# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'usuarioswmmbrl.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_usuarios(object):
    def setupUi(self, usuarios):
        if not usuarios.objectName():
            usuarios.setObjectName(u"usuarios")
        usuarios.resize(1182, 608)
        usuarios.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(usuarios)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(usuarios)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_3.setFont(font)

        self.verticalLayout_2.addWidget(self.label_3)

        self.frame_28 = QFrame(self.frame)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.frame_28)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_27)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_16 = QLabel(self.frame_27)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.verticalLayout_28.addWidget(self.label_16)

        self.usuTable = QTableWidget(self.frame_27)
        if (self.usuTable.columnCount() < 11):
            self.usuTable.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.usuTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.usuTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.usuTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.usuTable.rowCount() < 3):
            self.usuTable.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.usuTable.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.usuTable.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.usuTable.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.usuTable.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.usuTable.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.usuTable.setItem(0, 2, __qtablewidgetitem8)
        self.usuTable.setObjectName(u"usuTable")
        self.usuTable.setMinimumSize(QSize(0, 0))
        self.usuTable.setMaximumSize(QSize(16777215, 16777215))
        self.usuTable.setFrameShape(QFrame.NoFrame)
        self.usuTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.usuTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.usuTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.usuTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.usuTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.usuTable.setShowGrid(True)
        self.usuTable.setGridStyle(Qt.SolidLine)
        self.usuTable.setSortingEnabled(False)
        self.usuTable.setRowCount(3)
        self.usuTable.setColumnCount(11)
        self.usuTable.horizontalHeader().setVisible(True)
        self.usuTable.horizontalHeader().setCascadingSectionResizes(False)
        self.usuTable.horizontalHeader().setDefaultSectionSize(120)
        self.usuTable.horizontalHeader().setStretchLastSection(True)
        self.usuTable.verticalHeader().setVisible(False)
        self.usuTable.verticalHeader().setCascadingSectionResizes(False)
        self.usuTable.verticalHeader().setHighlightSections(False)
        self.usuTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_28.addWidget(self.usuTable)

        self.frame_26 = QFrame(self.frame_27)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer)

        self.usuAddButton = QPushButton(self.frame_26)
        self.usuAddButton.setObjectName(u"usuAddButton")
        self.usuAddButton.setMinimumSize(QSize(120, 30))
        self.usuAddButton.setFont(font)
        self.usuAddButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-check-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.usuAddButton.setIcon(icon)

        self.horizontalLayout_14.addWidget(self.usuAddButton)

        self.usuEditButton = QPushButton(self.frame_26)
        self.usuEditButton.setObjectName(u"usuEditButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usuEditButton.sizePolicy().hasHeightForWidth())
        self.usuEditButton.setSizePolicy(sizePolicy)
        self.usuEditButton.setMinimumSize(QSize(120, 30))
        self.usuEditButton.setFont(font)
        self.usuEditButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.usuEditButton.setIcon(icon1)

        self.horizontalLayout_14.addWidget(self.usuEditButton)

        self.usuDelButton = QPushButton(self.frame_26)
        self.usuDelButton.setObjectName(u"usuDelButton")
        self.usuDelButton.setMinimumSize(QSize(120, 30))
        self.usuDelButton.setFont(font)
        self.usuDelButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.usuDelButton.setIcon(icon2)

        self.horizontalLayout_14.addWidget(self.usuDelButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_2)


        self.verticalLayout_28.addWidget(self.frame_26)


        self.horizontalLayout_15.addWidget(self.frame_27)

        self.frame_25 = QFrame(self.frame_28)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(450, 0))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_25)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_9)

        self.label_15 = QLabel(self.frame_25)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.verticalLayout_27.addWidget(self.label_15)

        self.frame_23 = QFrame(self.frame_25)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.formLayout_7 = QFormLayout(self.frame_23)
        self.formLayout_7.setObjectName(u"formLayout_7")
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

        self.labelVersion_14 = QLabel(self.frame_23)
        self.labelVersion_14.setObjectName(u"labelVersion_14")
        self.labelVersion_14.setLineWidth(1)
        self.labelVersion_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_7.setWidget(4, QFormLayout.LabelRole, self.labelVersion_14)

        self.usuCedText = QLineEdit(self.frame_23)
        self.usuCedText.setObjectName(u"usuCedText")
        self.usuCedText.setMinimumSize(QSize(0, 30))
        self.usuCedText.setFrame(True)
        self.usuCedText.setEchoMode(QLineEdit.Normal)

        self.formLayout_7.setWidget(4, QFormLayout.FieldRole, self.usuCedText)

        self.labelVersion_17 = QLabel(self.frame_23)
        self.labelVersion_17.setObjectName(u"labelVersion_17")
        self.labelVersion_17.setLineWidth(1)
        self.labelVersion_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_7.setWidget(5, QFormLayout.LabelRole, self.labelVersion_17)

        self.usuRolCombo = QComboBox(self.frame_23)
        self.usuRolCombo.addItem("")
        self.usuRolCombo.addItem("")
        self.usuRolCombo.addItem("")
        self.usuRolCombo.setObjectName(u"usuRolCombo")
        self.usuRolCombo.setFont(font)
        self.usuRolCombo.setAutoFillBackground(False)
        self.usuRolCombo.setIconSize(QSize(16, 16))
        self.usuRolCombo.setFrame(True)

        self.formLayout_7.setWidget(5, QFormLayout.FieldRole, self.usuRolCombo)

        self.labelVersion_16 = QLabel(self.frame_23)
        self.labelVersion_16.setObjectName(u"labelVersion_16")
        self.labelVersion_16.setLineWidth(1)
        self.labelVersion_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_7.setWidget(6, QFormLayout.LabelRole, self.labelVersion_16)

        self.usuNickText = QLineEdit(self.frame_23)
        self.usuNickText.setObjectName(u"usuNickText")
        self.usuNickText.setMinimumSize(QSize(0, 30))

        self.formLayout_7.setWidget(6, QFormLayout.FieldRole, self.usuNickText)

        self.labelVersion_18 = QLabel(self.frame_23)
        self.labelVersion_18.setObjectName(u"labelVersion_18")
        self.labelVersion_18.setLineWidth(1)
        self.labelVersion_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_7.setWidget(7, QFormLayout.LabelRole, self.labelVersion_18)

        self.usuConText = QLineEdit(self.frame_23)
        self.usuConText.setObjectName(u"usuConText")
        self.usuConText.setMinimumSize(QSize(0, 30))

        self.formLayout_7.setWidget(7, QFormLayout.FieldRole, self.usuConText)

        self.labelVersion_13 = QLabel(self.frame_23)
        self.labelVersion_13.setObjectName(u"labelVersion_13")
        self.labelVersion_13.setLineWidth(1)
        self.labelVersion_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_7.setWidget(8, QFormLayout.LabelRole, self.labelVersion_13)

        self.usuDirText = QLineEdit(self.frame_23)
        self.usuDirText.setObjectName(u"usuDirText")
        self.usuDirText.setMinimumSize(QSize(0, 30))

        self.formLayout_7.setWidget(8, QFormLayout.FieldRole, self.usuDirText)

        self.labelVersion_15 = QLabel(self.frame_23)
        self.labelVersion_15.setObjectName(u"labelVersion_15")
        self.labelVersion_15.setLineWidth(1)
        self.labelVersion_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_7.setWidget(9, QFormLayout.LabelRole, self.labelVersion_15)

        self.usuTelText = QLineEdit(self.frame_23)
        self.usuTelText.setObjectName(u"usuTelText")
        self.usuTelText.setMinimumSize(QSize(0, 30))

        self.formLayout_7.setWidget(9, QFormLayout.FieldRole, self.usuTelText)


        self.verticalLayout_27.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_25)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)

        self.usuSaveButton = QPushButton(self.frame_24)
        self.usuSaveButton.setObjectName(u"usuSaveButton")
        self.usuSaveButton.setMinimumSize(QSize(120, 30))
        self.usuSaveButton.setFont(font)
        self.usuSaveButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.usuSaveButton.setIcon(icon)

        self.horizontalLayout_13.addWidget(self.usuSaveButton)

        self.usuCancelButton = QPushButton(self.frame_24)
        self.usuCancelButton.setObjectName(u"usuCancelButton")
        self.usuCancelButton.setMinimumSize(QSize(120, 30))
        self.usuCancelButton.setFont(font)
        self.usuCancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.usuCancelButton.setIcon(icon2)

        self.horizontalLayout_13.addWidget(self.usuCancelButton)

        self.usuClearButton = QPushButton(self.frame_24)
        self.usuClearButton.setObjectName(u"usuClearButton")
        self.usuClearButton.setMinimumSize(QSize(120, 30))
        self.usuClearButton.setFont(font)
        self.usuClearButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-reload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.usuClearButton.setIcon(icon3)

        self.horizontalLayout_13.addWidget(self.usuClearButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)


        self.verticalLayout_27.addWidget(self.frame_24)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_10)


        self.horizontalLayout_15.addWidget(self.frame_25)


        self.verticalLayout_2.addWidget(self.frame_28)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(usuarios)

        self.usuRolCombo.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(usuarios)
    # setupUi

    def retranslateUi(self, usuarios):
        usuarios.setWindowTitle(QCoreApplication.translate("usuarios", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("usuarios", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Usuarios</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("usuarios", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Lista de Usuarios</span></p></body></html>", None))
        ___qtablewidgetitem = self.usuTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("usuarios", u"0", None));
        ___qtablewidgetitem1 = self.usuTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("usuarios", u"Nueva columna", None));
        ___qtablewidgetitem2 = self.usuTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("usuarios", u"1", None));
        ___qtablewidgetitem3 = self.usuTable.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("usuarios", u"New Row", None));
        ___qtablewidgetitem4 = self.usuTable.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("usuarios", u"New Row", None));
        ___qtablewidgetitem5 = self.usuTable.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("usuarios", u"New Row", None));

        __sortingEnabled = self.usuTable.isSortingEnabled()
        self.usuTable.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.usuTable.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("usuarios", u"Nombre ", None));
        ___qtablewidgetitem7 = self.usuTable.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("usuarios", u"C\u00e9dula", None));
        ___qtablewidgetitem8 = self.usuTable.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("usuarios", u"Rol", None));
        self.usuTable.setSortingEnabled(__sortingEnabled)

        self.usuAddButton.setText(QCoreApplication.translate("usuarios", u"Agregar", None))
        self.usuEditButton.setText(QCoreApplication.translate("usuarios", u"Editar", None))
        self.usuDelButton.setText(QCoreApplication.translate("usuarios", u"Eliminar", None))
        self.label_15.setText(QCoreApplication.translate("usuarios", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Usuario Seleccionado</span></p></body></html>", None))
        self.labelVersion_12.setText(QCoreApplication.translate("usuarios", u"Nombre1", None))
        self.usuNomText.setText("")
        self.usuNomText.setPlaceholderText(QCoreApplication.translate("usuarios", u"Ingrese el primer nombre", None))
        self.labelVersion_20.setText(QCoreApplication.translate("usuarios", u"Nombre2", None))
        self.usuNom2Text.setText("")
        self.usuNom2Text.setPlaceholderText(QCoreApplication.translate("usuarios", u"Ingrese el segundo nombre", None))
        self.labelVersion_21.setText(QCoreApplication.translate("usuarios", u"Apellido1", None))
        self.usuApe1Text.setText("")
        self.usuApe1Text.setPlaceholderText(QCoreApplication.translate("usuarios", u"Ingrese el primer apellido", None))
        self.labelVersion_22.setText(QCoreApplication.translate("usuarios", u"Apellido2", None))
        self.usuApe2Text.setText("")
        self.usuApe2Text.setPlaceholderText(QCoreApplication.translate("usuarios", u"Ingrese el segundo apellido", None))
        self.labelVersion_14.setText(QCoreApplication.translate("usuarios", u"C\u00e9dula", None))
        self.usuCedText.setText("")
        self.usuCedText.setPlaceholderText(QCoreApplication.translate("usuarios", u"Ingrese el numero de c\u00e9dula", None))
        self.labelVersion_17.setText(QCoreApplication.translate("usuarios", u"Rol", None))
        self.usuRolCombo.setItemText(0, QCoreApplication.translate("usuarios", u"Fotocopiado", None))
        self.usuRolCombo.setItemText(1, QCoreApplication.translate("usuarios", u"Impresi\u00f3n", None))
        self.usuRolCombo.setItemText(2, QCoreApplication.translate("usuarios", u"Laminado", None))

        self.usuRolCombo.setPlaceholderText(QCoreApplication.translate("usuarios", u"Seleccione una opci\u00f3n", None))
        self.labelVersion_16.setText(QCoreApplication.translate("usuarios", u"Alias", None))
        self.usuNickText.setText("")
        self.usuNickText.setPlaceholderText(QCoreApplication.translate("usuarios", u"Ingrese el alias", None))
        self.labelVersion_18.setText(QCoreApplication.translate("usuarios", u"Contrase\u00f1a", None))
        self.usuConText.setText("")
        self.usuConText.setPlaceholderText(QCoreApplication.translate("usuarios", u"Ingrese la contrase\u00f1a", None))
        self.labelVersion_13.setText(QCoreApplication.translate("usuarios", u"Direcci\u00f3n", None))
        self.usuDirText.setText("")
        self.usuDirText.setPlaceholderText(QCoreApplication.translate("usuarios", u"Ingrese la direcci\u00f3n", None))
        self.labelVersion_15.setText(QCoreApplication.translate("usuarios", u"Tel\u00e9fono", None))
        self.usuTelText.setText("")
        self.usuTelText.setPlaceholderText(QCoreApplication.translate("usuarios", u"Ingrese el numero de tel\u00e9fono", None))
        self.usuSaveButton.setText(QCoreApplication.translate("usuarios", u"Confirmar", None))
        self.usuCancelButton.setText(QCoreApplication.translate("usuarios", u"Cancelar", None))
        self.usuClearButton.setText(QCoreApplication.translate("usuarios", u"Limpiar", None))
    # retranslateUi

