# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'deudaskWvHKV.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_deudas(object):
    def setupUi(self, deudas):
        if not deudas.objectName():
            deudas.setObjectName(u"deudas")
        deudas.resize(1182, 608)
        deudas.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(deudas)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(deudas)
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

        self.frame_39 = QFrame(self.frame)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_34 = QFrame(self.frame_39)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_34)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_23 = QLabel(self.frame_34)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)

        self.verticalLayout_30.addWidget(self.label_23)

        self.tableDeuda = QTableWidget(self.frame_34)
        if (self.tableDeuda.columnCount() < 3):
            self.tableDeuda.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableDeuda.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableDeuda.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableDeuda.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableDeuda.rowCount() < 11):
            self.tableDeuda.setRowCount(11)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableDeuda.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableDeuda.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableDeuda.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableDeuda.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableDeuda.setVerticalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableDeuda.setVerticalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableDeuda.setVerticalHeaderItem(6, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableDeuda.setVerticalHeaderItem(7, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableDeuda.setVerticalHeaderItem(8, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableDeuda.setVerticalHeaderItem(9, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableDeuda.setVerticalHeaderItem(10, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableDeuda.setItem(0, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableDeuda.setItem(0, 1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableDeuda.setItem(0, 2, __qtablewidgetitem16)
        self.tableDeuda.setObjectName(u"tableDeuda")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableDeuda.sizePolicy().hasHeightForWidth())
        self.tableDeuda.setSizePolicy(sizePolicy)
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
        self.tableDeuda.setPalette(palette)
        self.tableDeuda.setFrameShape(QFrame.NoFrame)
        self.tableDeuda.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableDeuda.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableDeuda.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableDeuda.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableDeuda.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableDeuda.setShowGrid(True)
        self.tableDeuda.setGridStyle(Qt.SolidLine)
        self.tableDeuda.setSortingEnabled(False)
        self.tableDeuda.horizontalHeader().setVisible(True)
        self.tableDeuda.horizontalHeader().setCascadingSectionResizes(True)
        self.tableDeuda.horizontalHeader().setDefaultSectionSize(200)
        self.tableDeuda.horizontalHeader().setStretchLastSection(True)
        self.tableDeuda.verticalHeader().setVisible(False)
        self.tableDeuda.verticalHeader().setCascadingSectionResizes(False)
        self.tableDeuda.verticalHeader().setHighlightSections(False)
        self.tableDeuda.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_30.addWidget(self.tableDeuda)

        self.frame_33 = QFrame(self.frame_34)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")

        self.verticalLayout_30.addWidget(self.frame_33)


        self.horizontalLayout_19.addWidget(self.frame_34)

        self.frame_38 = QFrame(self.frame_39)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_38)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_24 = QLabel(self.frame_38)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)

        self.verticalLayout_31.addWidget(self.label_24)

        self.frame_35 = QFrame(self.frame_38)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.formLayout_10 = QFormLayout(self.frame_35)
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.labelVersion_21 = QLabel(self.frame_35)
        self.labelVersion_21.setObjectName(u"labelVersion_21")
        self.labelVersion_21.setLineWidth(1)
        self.labelVersion_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_10.setWidget(0, QFormLayout.LabelRole, self.labelVersion_21)

        self.textName = QLineEdit(self.frame_35)
        self.textName.setObjectName(u"textName")
        self.textName.setMinimumSize(QSize(0, 30))

        self.formLayout_10.setWidget(0, QFormLayout.FieldRole, self.textName)

        self.labelVersion_23 = QLabel(self.frame_35)
        self.labelVersion_23.setObjectName(u"labelVersion_23")
        self.labelVersion_23.setLineWidth(1)
        self.labelVersion_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_10.setWidget(1, QFormLayout.LabelRole, self.labelVersion_23)

        self.textCedula = QLineEdit(self.frame_35)
        self.textCedula.setObjectName(u"textCedula")
        self.textCedula.setMinimumSize(QSize(0, 30))

        self.formLayout_10.setWidget(1, QFormLayout.FieldRole, self.textCedula)

        self.labelVersion_22 = QLabel(self.frame_35)
        self.labelVersion_22.setObjectName(u"labelVersion_22")
        self.labelVersion_22.setLineWidth(1)
        self.labelVersion_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_10.setWidget(2, QFormLayout.LabelRole, self.labelVersion_22)

        self.textTelefono = QLineEdit(self.frame_35)
        self.textTelefono.setObjectName(u"textTelefono")
        self.textTelefono.setMinimumSize(QSize(0, 30))

        self.formLayout_10.setWidget(2, QFormLayout.FieldRole, self.textTelefono)

        self.labelVersion_19 = QLabel(self.frame_35)
        self.labelVersion_19.setObjectName(u"labelVersion_19")
        self.labelVersion_19.setLineWidth(1)
        self.labelVersion_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_10.setWidget(3, QFormLayout.LabelRole, self.labelVersion_19)

        self.textDirec = QLineEdit(self.frame_35)
        self.textDirec.setObjectName(u"textDirec")
        self.textDirec.setMinimumSize(QSize(0, 30))

        self.formLayout_10.setWidget(3, QFormLayout.FieldRole, self.textDirec)


        self.verticalLayout_31.addWidget(self.frame_35)

        self.label_25 = QLabel(self.frame_38)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)

        self.verticalLayout_31.addWidget(self.label_25)

        self.frame_36 = QFrame(self.frame_38)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_36)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.textTotal = QLineEdit(self.frame_36)
        self.textTotal.setObjectName(u"textTotal")
        self.textTotal.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.textTotal, 1, 0, 1, 1)

        self.labelVersion_20 = QLabel(self.frame_36)
        self.labelVersion_20.setObjectName(u"labelVersion_20")
        self.labelVersion_20.setLineWidth(1)
        self.labelVersion_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelVersion_20, 0, 0, 1, 1)

        self.labelVersion_25 = QLabel(self.frame_36)
        self.labelVersion_25.setObjectName(u"labelVersion_25")
        self.labelVersion_25.setLineWidth(1)
        self.labelVersion_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelVersion_25, 0, 1, 1, 1)

        self.textSaldo = QLineEdit(self.frame_36)
        self.textSaldo.setObjectName(u"textSaldo")
        self.textSaldo.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.textSaldo, 1, 1, 1, 1)

        self.labelVersion_24 = QLabel(self.frame_36)
        self.labelVersion_24.setObjectName(u"labelVersion_24")
        self.labelVersion_24.setLineWidth(1)
        self.labelVersion_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelVersion_24, 2, 0, 1, 1)

        self.labelVersion_26 = QLabel(self.frame_36)
        self.labelVersion_26.setObjectName(u"labelVersion_26")
        self.labelVersion_26.setLineWidth(1)
        self.labelVersion_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelVersion_26, 2, 1, 1, 1)

        self.textAbono = QLineEdit(self.frame_36)
        self.textAbono.setObjectName(u"textAbono")
        self.textAbono.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.textAbono, 3, 0, 1, 1)

        self.textAdd = QLineEdit(self.frame_36)
        self.textAdd.setObjectName(u"textAdd")
        self.textAdd.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.textAdd, 3, 1, 1, 1)


        self.verticalLayout_31.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.frame_38)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_9)

        self.buttonTrans = QPushButton(self.frame_37)
        self.buttonTrans.setObjectName(u"buttonTrans")
        self.buttonTrans.setMinimumSize(QSize(150, 30))
        self.buttonTrans.setFont(font)
        self.buttonTrans.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-chevron-double-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonTrans.setIcon(icon)

        self.horizontalLayout_18.addWidget(self.buttonTrans)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_10)


        self.verticalLayout_31.addWidget(self.frame_37)


        self.horizontalLayout_19.addWidget(self.frame_38)


        self.verticalLayout_2.addWidget(self.frame_39)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(deudas)

        QMetaObject.connectSlotsByName(deudas)
    # setupUi

    def retranslateUi(self, deudas):
        deudas.setWindowTitle(QCoreApplication.translate("deudas", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("deudas", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Deudas</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("deudas", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Lista de Deudas</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableDeuda.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("deudas", u"0", None));
        ___qtablewidgetitem1 = self.tableDeuda.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("deudas", u"1", None));
        ___qtablewidgetitem2 = self.tableDeuda.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("deudas", u"2", None));
        ___qtablewidgetitem3 = self.tableDeuda.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("deudas", u"New Row", None));
        ___qtablewidgetitem4 = self.tableDeuda.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("deudas", u"New Row", None));
        ___qtablewidgetitem5 = self.tableDeuda.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("deudas", u"New Row", None));
        ___qtablewidgetitem6 = self.tableDeuda.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("deudas", u"New Row", None));
        ___qtablewidgetitem7 = self.tableDeuda.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("deudas", u"New Row", None));
        ___qtablewidgetitem8 = self.tableDeuda.verticalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("deudas", u"New Row", None));
        ___qtablewidgetitem9 = self.tableDeuda.verticalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("deudas", u"New Row", None));
        ___qtablewidgetitem10 = self.tableDeuda.verticalHeaderItem(7)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("deudas", u"New Row", None));
        ___qtablewidgetitem11 = self.tableDeuda.verticalHeaderItem(8)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("deudas", u"New Row", None));
        ___qtablewidgetitem12 = self.tableDeuda.verticalHeaderItem(9)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("deudas", u"New Row", None));
        ___qtablewidgetitem13 = self.tableDeuda.verticalHeaderItem(10)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("deudas", u"New Row", None));

        __sortingEnabled = self.tableDeuda.isSortingEnabled()
        self.tableDeuda.setSortingEnabled(False)
        ___qtablewidgetitem14 = self.tableDeuda.item(0, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("deudas", u"C\u00e9dula", None));
        ___qtablewidgetitem15 = self.tableDeuda.item(0, 1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("deudas", u"Nombre", None));
        ___qtablewidgetitem16 = self.tableDeuda.item(0, 2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("deudas", u"Saldo", None));
        self.tableDeuda.setSortingEnabled(__sortingEnabled)

        self.label_24.setText(QCoreApplication.translate("deudas", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Informaci\u00f3n de la Deuda</span></p></body></html>", None))
        self.labelVersion_21.setText(QCoreApplication.translate("deudas", u"Deudor", None))
        self.textName.setText("")
        self.labelVersion_23.setText(QCoreApplication.translate("deudas", u"C\u00e9dula", None))
        self.textCedula.setText("")
        self.labelVersion_22.setText(QCoreApplication.translate("deudas", u"Tel\u00e9fono", None))
        self.textTelefono.setText("")
        self.labelVersion_19.setText(QCoreApplication.translate("deudas", u"Direcci\u00f3n", None))
        self.textDirec.setText("")
        self.label_25.setText(QCoreApplication.translate("deudas", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Valores de la Deuda</span></p></body></html>", None))
        self.textTotal.setText("")
        self.labelVersion_20.setText(QCoreApplication.translate("deudas", u"Total deuda", None))
        self.labelVersion_25.setText(QCoreApplication.translate("deudas", u"Saldo pendiente", None))
        self.textSaldo.setText("")
        self.labelVersion_24.setText(QCoreApplication.translate("deudas", u"Abono actual", None))
        self.labelVersion_26.setText(QCoreApplication.translate("deudas", u"A\u00f1adir al Abono", None))
        self.textAbono.setText("")
        self.textAbono.setPlaceholderText("")
        self.textAdd.setText("")
        self.textAdd.setPlaceholderText(QCoreApplication.translate("deudas", u"Ingrese la cantidad a abonar", None))
        self.buttonTrans.setText(QCoreApplication.translate("deudas", u"Abonar", None))
    # retranslateUi

