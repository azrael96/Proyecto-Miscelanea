# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gastosDVVROZ.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_gastos(object):
    def setupUi(self, gastos):
        if not gastos.objectName():
            gastos.setObjectName(u"gastos")
        gastos.resize(1182, 608)
        gastos.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(gastos)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(gastos)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.frame_21 = QFrame(self.frame)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_20 = QFrame(self.frame_21)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_20)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_18 = QLabel(self.frame_20)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.verticalLayout_24.addWidget(self.label_18)

        self.tableGastos = QTableWidget(self.frame_20)
        if (self.tableGastos.columnCount() < 2):
            self.tableGastos.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableGastos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableGastos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableGastos.rowCount() < 12):
            self.tableGastos.setRowCount(12)
        font1 = QFont()
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tableGastos.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableGastos.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableGastos.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableGastos.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableGastos.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableGastos.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableGastos.setVerticalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableGastos.setVerticalHeaderItem(7, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableGastos.setVerticalHeaderItem(8, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableGastos.setVerticalHeaderItem(9, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableGastos.setVerticalHeaderItem(10, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableGastos.setVerticalHeaderItem(11, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableGastos.setItem(0, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableGastos.setItem(0, 1, __qtablewidgetitem15)
        self.tableGastos.setObjectName(u"tableGastos")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableGastos.sizePolicy().hasHeightForWidth())
        self.tableGastos.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(51, 51, 51, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableGastos.setPalette(palette)
        self.tableGastos.setFrameShape(QFrame.NoFrame)
        self.tableGastos.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableGastos.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableGastos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableGastos.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableGastos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableGastos.setShowGrid(True)
        self.tableGastos.setGridStyle(Qt.SolidLine)
        self.tableGastos.setSortingEnabled(False)
        self.tableGastos.horizontalHeader().setVisible(True)
        self.tableGastos.horizontalHeader().setCascadingSectionResizes(True)
        self.tableGastos.horizontalHeader().setDefaultSectionSize(200)
        self.tableGastos.horizontalHeader().setStretchLastSection(True)
        self.tableGastos.verticalHeader().setVisible(False)
        self.tableGastos.verticalHeader().setCascadingSectionResizes(False)
        self.tableGastos.verticalHeader().setHighlightSections(False)
        self.tableGastos.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_24.addWidget(self.tableGastos)


        self.horizontalLayout_12.addWidget(self.frame_20)

        self.frame_19 = QFrame(self.frame_21)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_19)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_5)

        self.label_17 = QLabel(self.frame_19)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.verticalLayout_23.addWidget(self.label_17)

        self.frame_18 = QFrame(self.frame_19)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.formLayout_6 = QFormLayout(self.frame_18)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.labelVersion_9 = QLabel(self.frame_18)
        self.labelVersion_9.setObjectName(u"labelVersion_9")
        self.labelVersion_9.setLineWidth(1)
        self.labelVersion_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.labelVersion_9)

        self.textDes = QLineEdit(self.frame_18)
        self.textDes.setObjectName(u"textDes")
        self.textDes.setMinimumSize(QSize(0, 30))

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.textDes)

        self.labelVersion_8 = QLabel(self.frame_18)
        self.labelVersion_8.setObjectName(u"labelVersion_8")
        self.labelVersion_8.setLineWidth(1)
        self.labelVersion_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.labelVersion_8)

        self.textValor = QLineEdit(self.frame_18)
        self.textValor.setObjectName(u"textValor")
        self.textValor.setMinimumSize(QSize(0, 30))

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.textValor)


        self.verticalLayout_23.addWidget(self.frame_18)

        self.frame_22 = QFrame(self.frame_19)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_5)

        self.buttonReg = QPushButton(self.frame_22)
        self.buttonReg.setObjectName(u"buttonReg")
        self.buttonReg.setMinimumSize(QSize(150, 30))
        self.buttonReg.setFont(font)
        self.buttonReg.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-data-transfer-down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonReg.setIcon(icon)

        self.horizontalLayout_13.addWidget(self.buttonReg)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_6)


        self.verticalLayout_23.addWidget(self.frame_22)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_6)


        self.horizontalLayout_12.addWidget(self.frame_19)


        self.verticalLayout_2.addWidget(self.frame_21)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(gastos)

        QMetaObject.connectSlotsByName(gastos)
    # setupUi

    def retranslateUi(self, gastos):
        gastos.setWindowTitle(QCoreApplication.translate("gastos", u"Form", None))
        self.label.setText(QCoreApplication.translate("gastos", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Retiros a la Caja</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("gastos", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Listado de Retiros</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableGastos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("gastos", u"0", None));
        ___qtablewidgetitem1 = self.tableGastos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("gastos", u"1", None));
        ___qtablewidgetitem2 = self.tableGastos.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("gastos", u"New Row", None));
        ___qtablewidgetitem3 = self.tableGastos.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("gastos", u"Nueva fila", None));
        ___qtablewidgetitem4 = self.tableGastos.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("gastos", u"Nueva fila", None));
        ___qtablewidgetitem5 = self.tableGastos.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("gastos", u"New Row", None));
        ___qtablewidgetitem6 = self.tableGastos.verticalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("gastos", u"New Row", None));
        ___qtablewidgetitem7 = self.tableGastos.verticalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("gastos", u"New Row", None));
        ___qtablewidgetitem8 = self.tableGastos.verticalHeaderItem(6)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("gastos", u"New Row", None));
        ___qtablewidgetitem9 = self.tableGastos.verticalHeaderItem(7)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("gastos", u"New Row", None));
        ___qtablewidgetitem10 = self.tableGastos.verticalHeaderItem(8)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("gastos", u"New Row", None));
        ___qtablewidgetitem11 = self.tableGastos.verticalHeaderItem(9)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("gastos", u"New Row", None));
        ___qtablewidgetitem12 = self.tableGastos.verticalHeaderItem(10)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("gastos", u"New Row", None));
        ___qtablewidgetitem13 = self.tableGastos.verticalHeaderItem(11)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("gastos", u"New Row", None));

        __sortingEnabled = self.tableGastos.isSortingEnabled()
        self.tableGastos.setSortingEnabled(False)
        ___qtablewidgetitem14 = self.tableGastos.item(0, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("gastos", u"Descripci\u00f3n", None));
        ___qtablewidgetitem15 = self.tableGastos.item(0, 1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("gastos", u"Valor", None));
        self.tableGastos.setSortingEnabled(__sortingEnabled)

        self.label_17.setText(QCoreApplication.translate("gastos", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Registrar Retiro</span></p></body></html>", None))
        self.labelVersion_9.setText(QCoreApplication.translate("gastos", u"Motivo:", None))
        self.textDes.setText("")
        self.textDes.setPlaceholderText(QCoreApplication.translate("gastos", u"Ingrese el motivo del retiro", None))
        self.labelVersion_8.setText(QCoreApplication.translate("gastos", u"Valor", None))
        self.textValor.setText("")
        self.textValor.setPlaceholderText(QCoreApplication.translate("gastos", u"Ingrese la cantidad a retirar", None))
        self.buttonReg.setText(QCoreApplication.translate("gastos", u"Registrar", None))
    # retranslateUi

