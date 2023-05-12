# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'categoriaskrUrUy.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_categorias(object):
    def setupUi(self, categorias):
        if not categorias.objectName():
            categorias.setObjectName(u"categorias")
        categorias.resize(1182, 608)
        categorias.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(categorias)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(categorias)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_4.setFont(font)

        self.verticalLayout_2.addWidget(self.label_4)

        self.frame_34 = QFrame(self.frame)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_33 = QFrame(self.frame_34)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_33)
        self.verticalLayout_31.setSpacing(9)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(9, 9, 9, 9)
        self.label_18 = QLabel(self.frame_33)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)
        self.label_18.setMargin(1)

        self.verticalLayout_31.addWidget(self.label_18)

        self.catTable = QTableWidget(self.frame_33)
        if (self.catTable.columnCount() < 2):
            self.catTable.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.catTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.catTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.catTable.rowCount() < 11):
            self.catTable.setRowCount(11)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.catTable.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.catTable.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.catTable.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.catTable.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.catTable.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.catTable.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.catTable.setVerticalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.catTable.setVerticalHeaderItem(7, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.catTable.setVerticalHeaderItem(8, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.catTable.setVerticalHeaderItem(9, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.catTable.setVerticalHeaderItem(10, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.catTable.setItem(0, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.catTable.setItem(0, 1, __qtablewidgetitem14)
        self.catTable.setObjectName(u"catTable")
        self.catTable.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.catTable.sizePolicy().hasHeightForWidth())
        self.catTable.setSizePolicy(sizePolicy)
        self.catTable.setFrameShape(QFrame.NoFrame)
        self.catTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.catTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.catTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.catTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.catTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.catTable.setShowGrid(True)
        self.catTable.setGridStyle(Qt.SolidLine)
        self.catTable.setSortingEnabled(False)
        self.catTable.horizontalHeader().setVisible(True)
        self.catTable.horizontalHeader().setCascadingSectionResizes(True)
        self.catTable.horizontalHeader().setDefaultSectionSize(120)
        self.catTable.horizontalHeader().setStretchLastSection(True)
        self.catTable.verticalHeader().setVisible(False)
        self.catTable.verticalHeader().setCascadingSectionResizes(False)
        self.catTable.verticalHeader().setHighlightSections(False)
        self.catTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_31.addWidget(self.catTable)


        self.horizontalLayout_19.addWidget(self.frame_33)

        self.frame_2 = QFrame(self.frame_34)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_19.addWidget(self.frame_2)

        self.frame_31 = QFrame(self.frame_34)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_31)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.catDelButton = QPushButton(self.frame_31)
        self.catDelButton.setObjectName(u"catDelButton")
        self.catDelButton.setMinimumSize(QSize(120, 30))
        self.catDelButton.setFont(font)
        self.catDelButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.catDelButton.setIcon(icon)

        self.verticalLayout_3.addWidget(self.catDelButton)

        self.catEditButton = QPushButton(self.frame_31)
        self.catEditButton.setObjectName(u"catEditButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.catEditButton.sizePolicy().hasHeightForWidth())
        self.catEditButton.setSizePolicy(sizePolicy1)
        self.catEditButton.setMinimumSize(QSize(120, 30))
        self.catEditButton.setFont(font)
        self.catEditButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.catEditButton.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.catEditButton)

        self.catAddButton = QPushButton(self.frame_31)
        self.catAddButton.setObjectName(u"catAddButton")
        self.catAddButton.setMinimumSize(QSize(120, 30))
        self.catAddButton.setFont(font)
        self.catAddButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/cil-check-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.catAddButton.setIcon(icon2)

        self.verticalLayout_3.addWidget(self.catAddButton)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)


        self.horizontalLayout_19.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.frame_34)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy2)
        self.frame_32.setMinimumSize(QSize(450, 0))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_32)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_2)

        self.label_17 = QLabel(self.frame_32)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.verticalLayout_30.addWidget(self.label_17)

        self.frame_29 = QFrame(self.frame_32)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.formLayout_8 = QFormLayout(self.frame_29)
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.labelVersion_21 = QLabel(self.frame_29)
        self.labelVersion_21.setObjectName(u"labelVersion_21")
        self.labelVersion_21.setLineWidth(1)
        self.labelVersion_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.labelVersion_21)

        self.catNomText = QLineEdit(self.frame_29)
        self.catNomText.setObjectName(u"catNomText")
        self.catNomText.setMinimumSize(QSize(0, 30))

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.catNomText)

        self.labelVersion_23 = QLabel(self.frame_29)
        self.labelVersion_23.setObjectName(u"labelVersion_23")
        self.labelVersion_23.setLineWidth(1)
        self.labelVersion_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.labelVersion_23)

        self.catDesText = QLineEdit(self.frame_29)
        self.catDesText.setObjectName(u"catDesText")
        self.catDesText.setMinimumSize(QSize(0, 30))

        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.catDesText)


        self.verticalLayout_30.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.frame_32)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer)

        self.catSaveButton = QPushButton(self.frame_30)
        self.catSaveButton.setObjectName(u"catSaveButton")
        self.catSaveButton.setMinimumSize(QSize(120, 30))
        self.catSaveButton.setFont(font)
        self.catSaveButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.catSaveButton.setIcon(icon2)

        self.horizontalLayout_17.addWidget(self.catSaveButton)

        self.catCancelButton = QPushButton(self.frame_30)
        self.catCancelButton.setObjectName(u"catCancelButton")
        self.catCancelButton.setMinimumSize(QSize(120, 30))
        self.catCancelButton.setFont(font)
        self.catCancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.catCancelButton.setIcon(icon)

        self.horizontalLayout_17.addWidget(self.catCancelButton)

        self.catClearButton = QPushButton(self.frame_30)
        self.catClearButton.setObjectName(u"catClearButton")
        self.catClearButton.setMinimumSize(QSize(120, 30))
        self.catClearButton.setFont(font)
        self.catClearButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-reload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.catClearButton.setIcon(icon3)

        self.horizontalLayout_17.addWidget(self.catClearButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_2)


        self.verticalLayout_30.addWidget(self.frame_30)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer)


        self.horizontalLayout_19.addWidget(self.frame_32)


        self.verticalLayout_2.addWidget(self.frame_34)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(categorias)

        QMetaObject.connectSlotsByName(categorias)
    # setupUi

    def retranslateUi(self, categorias):
        categorias.setWindowTitle(QCoreApplication.translate("categorias", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("categorias", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Categor\u00edas</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("categorias", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Lista de Categor\u00edas</span></p></body></html>", None))
        ___qtablewidgetitem = self.catTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("categorias", u"Nombre ", None));
        ___qtablewidgetitem1 = self.catTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("categorias", u"Descripci\u00f3n", None));
        ___qtablewidgetitem2 = self.catTable.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("categorias", u"New Row", None));
        ___qtablewidgetitem3 = self.catTable.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("categorias", u"New Row", None));
        ___qtablewidgetitem4 = self.catTable.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("categorias", u"New Row", None));
        ___qtablewidgetitem5 = self.catTable.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("categorias", u"New Row", None));
        ___qtablewidgetitem6 = self.catTable.verticalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("categorias", u"New Row", None));
        ___qtablewidgetitem7 = self.catTable.verticalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("categorias", u"New Row", None));
        ___qtablewidgetitem8 = self.catTable.verticalHeaderItem(6)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("categorias", u"New Row", None));
        ___qtablewidgetitem9 = self.catTable.verticalHeaderItem(7)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("categorias", u"New Row", None));
        ___qtablewidgetitem10 = self.catTable.verticalHeaderItem(8)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("categorias", u"New Row", None));
        ___qtablewidgetitem11 = self.catTable.verticalHeaderItem(9)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("categorias", u"New Row", None));
        ___qtablewidgetitem12 = self.catTable.verticalHeaderItem(10)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("categorias", u"New Row", None));

        __sortingEnabled = self.catTable.isSortingEnabled()
        self.catTable.setSortingEnabled(False)
        ___qtablewidgetitem13 = self.catTable.item(0, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("categorias", u"Nombre ", None));
        ___qtablewidgetitem14 = self.catTable.item(0, 1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("categorias", u"Descripci\u00f3n", None));
        self.catTable.setSortingEnabled(__sortingEnabled)

        self.catDelButton.setText(QCoreApplication.translate("categorias", u"Eliminar", None))
        self.catEditButton.setText(QCoreApplication.translate("categorias", u"Editar", None))
        self.catAddButton.setText(QCoreApplication.translate("categorias", u"Agregar", None))
        self.label_17.setText(QCoreApplication.translate("categorias", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Categor\u00eda Seleccionada</span></p></body></html>", None))
        self.labelVersion_21.setText(QCoreApplication.translate("categorias", u"Nombre", None))
        self.catNomText.setText("")
        self.catNomText.setPlaceholderText(QCoreApplication.translate("categorias", u"Ingrese el nombre de la categor\u00eda", None))
        self.labelVersion_23.setText(QCoreApplication.translate("categorias", u"Descripci\u00f3n", None))
        self.catDesText.setText("")
        self.catDesText.setPlaceholderText(QCoreApplication.translate("categorias", u"Ingrese la descripci\u00f3n de la categor\u00eda", None))
        self.catSaveButton.setText(QCoreApplication.translate("categorias", u"Confirmar", None))
        self.catCancelButton.setText(QCoreApplication.translate("categorias", u"Cancelar", None))
        self.catClearButton.setText(QCoreApplication.translate("categorias", u"Limpiar", None))
    # retranslateUi

