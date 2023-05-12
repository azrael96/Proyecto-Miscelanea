# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inventarioeogaSK.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_inventario(object):
    def setupUi(self, inventario):
        if not inventario.objectName():
            inventario.setObjectName(u"inventario")
        inventario.resize(1182, 608)
        self.verticalLayout_2 = QVBoxLayout(inventario)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(inventario)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.frame_22 = QFrame(self.frame)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_22)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(16777215, 16777215))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_20)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_14 = QLabel(self.frame_20)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.verticalLayout_24.addWidget(self.label_14)

        self.proTable = QTableWidget(self.frame_20)
        if (self.proTable.columnCount() < 3):
            self.proTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.proTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.proTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.proTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.proTable.rowCount() < 11):
            self.proTable.setRowCount(11)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(6, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(7, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(8, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(9, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(10, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.proTable.setItem(0, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.proTable.setItem(0, 1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.proTable.setItem(0, 2, __qtablewidgetitem16)
        self.proTable.setObjectName(u"proTable")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proTable.sizePolicy().hasHeightForWidth())
        self.proTable.setSizePolicy(sizePolicy)
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
        self.proTable.setPalette(palette)
        self.proTable.setFrameShape(QFrame.NoFrame)
        self.proTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.proTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.proTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.proTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.proTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.proTable.setShowGrid(True)
        self.proTable.setGridStyle(Qt.SolidLine)
        self.proTable.setSortingEnabled(False)
        self.proTable.horizontalHeader().setVisible(True)
        self.proTable.horizontalHeader().setCascadingSectionResizes(True)
        self.proTable.horizontalHeader().setDefaultSectionSize(200)
        self.proTable.horizontalHeader().setStretchLastSection(True)
        self.proTable.verticalHeader().setVisible(False)
        self.proTable.verticalHeader().setCascadingSectionResizes(False)
        self.proTable.verticalHeader().setHighlightSections(False)
        self.proTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_24.addWidget(self.proTable)


        self.horizontalLayout_12.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_22)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(5000, 16777215))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_21)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_6)

        self.label_13 = QLabel(self.frame_21)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.verticalLayout_3.addWidget(self.label_13)

        self.frame_8 = QFrame(self.frame_21)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_8)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(9)
        self.formLayout_2.setVerticalSpacing(6)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.labelVersion_47 = QLabel(self.frame_8)
        self.labelVersion_47.setObjectName(u"labelVersion_47")
        self.labelVersion_47.setLineWidth(1)
        self.labelVersion_47.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.labelVersion_47)

        self.proNomText = QLineEdit(self.frame_8)
        self.proNomText.setObjectName(u"proNomText")
        self.proNomText.setMinimumSize(QSize(0, 30))
        self.proNomText.setReadOnly(False)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.proNomText)

        self.labelVersion_50 = QLabel(self.frame_8)
        self.labelVersion_50.setObjectName(u"labelVersion_50")
        self.labelVersion_50.setLineWidth(1)
        self.labelVersion_50.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.labelVersion_50)

        self.proCatCombo = QLineEdit(self.frame_8)
        self.proCatCombo.setObjectName(u"proCatCombo")
        self.proCatCombo.setMinimumSize(QSize(0, 30))
        self.proCatCombo.setReadOnly(False)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.proCatCombo)

        self.labelVersion_48 = QLabel(self.frame_8)
        self.labelVersion_48.setObjectName(u"labelVersion_48")
        self.labelVersion_48.setLineWidth(1)
        self.labelVersion_48.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.labelVersion_48)

        self.proDesText = QLineEdit(self.frame_8)
        self.proDesText.setObjectName(u"proDesText")
        self.proDesText.setMinimumSize(QSize(0, 30))

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.proDesText)

        self.labelVersion_49 = QLabel(self.frame_8)
        self.labelVersion_49.setObjectName(u"labelVersion_49")
        self.labelVersion_49.setLineWidth(1)
        self.labelVersion_49.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.labelVersion_49)

        self.frame_3 = QFrame(self.frame_8)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.proFotLabel = QLabel(self.frame_3)
        self.proFotLabel.setObjectName(u"proFotLabel")
        self.proFotLabel.setMinimumSize(QSize(150, 150))
        self.proFotLabel.setMaximumSize(QSize(150, 150))
        self.proFotLabel.setStyleSheet(u"/*---- QLabel  ----*/\n"
"QLabel {\n"
"    border-radius: 5px;\n"
"    border: 2px solid #6AAB6D;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    border: 2px solid #3C6B4A;\n"
"}\n"
"\n"
"QLabel:focus {\n"
"    border: 2px solid #FFF59D;\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    border: 2px solid #808080;\n"
"}")
        self.proFotLabel.setScaledContents(True)

        self.horizontalLayout.addWidget(self.proFotLabel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.frame_3)


        self.verticalLayout_3.addWidget(self.frame_8)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_8)


        self.horizontalLayout_12.addWidget(self.frame_21)


        self.verticalLayout.addWidget(self.frame_22)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(inventario)

        QMetaObject.connectSlotsByName(inventario)
    # setupUi

    def retranslateUi(self, inventario):
        inventario.setWindowTitle(QCoreApplication.translate("inventario", u"Form", None))
        self.label.setText(QCoreApplication.translate("inventario", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Inventario</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("inventario", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Lista de Productos</span></p></body></html>", None))
        ___qtablewidgetitem = self.proTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("inventario", u"0", None));
        ___qtablewidgetitem1 = self.proTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("inventario", u"1", None));
        ___qtablewidgetitem2 = self.proTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("inventario", u"2", None));
        ___qtablewidgetitem3 = self.proTable.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("inventario", u"New Row", None));
        ___qtablewidgetitem4 = self.proTable.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("inventario", u"New Row", None));
        ___qtablewidgetitem5 = self.proTable.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("inventario", u"New Row", None));
        ___qtablewidgetitem6 = self.proTable.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("inventario", u"New Row", None));
        ___qtablewidgetitem7 = self.proTable.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("inventario", u"New Row", None));
        ___qtablewidgetitem8 = self.proTable.verticalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("inventario", u"New Row", None));
        ___qtablewidgetitem9 = self.proTable.verticalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("inventario", u"New Row", None));
        ___qtablewidgetitem10 = self.proTable.verticalHeaderItem(7)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("inventario", u"New Row", None));
        ___qtablewidgetitem11 = self.proTable.verticalHeaderItem(8)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("inventario", u"New Row", None));
        ___qtablewidgetitem12 = self.proTable.verticalHeaderItem(9)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("inventario", u"New Row", None));
        ___qtablewidgetitem13 = self.proTable.verticalHeaderItem(10)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("inventario", u"New Row", None));

        __sortingEnabled = self.proTable.isSortingEnabled()
        self.proTable.setSortingEnabled(False)
        ___qtablewidgetitem14 = self.proTable.item(0, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("inventario", u"Producto", None));
        ___qtablewidgetitem15 = self.proTable.item(0, 1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("inventario", u"Cantidad", None));
        ___qtablewidgetitem16 = self.proTable.item(0, 2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("inventario", u"Costo Compra", None));
        self.proTable.setSortingEnabled(__sortingEnabled)

        self.label_13.setText(QCoreApplication.translate("inventario", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Producto Seleccionado</span></p></body></html>", None))
        self.labelVersion_47.setText(QCoreApplication.translate("inventario", u"Nombre Producto", None))
        self.proNomText.setText("")
        self.labelVersion_50.setText(QCoreApplication.translate("inventario", u"Categor\u00eda", None))
        self.proCatCombo.setText("")
        self.labelVersion_48.setText(QCoreApplication.translate("inventario", u"Descripci\u00f3n", None))
        self.proDesText.setText("")
        self.labelVersion_49.setText(QCoreApplication.translate("inventario", u"Foto", None))
    # retranslateUi

