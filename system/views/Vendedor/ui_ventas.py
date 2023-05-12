# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventasDvlbrO.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_ventas(object):
    def setupUi(self, ventas):
        if not ventas.objectName():
            ventas.setObjectName(u"ventas")
        ventas.resize(1182, 608)
        ventas.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(ventas)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(ventas)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_5.setFont(font)

        self.verticalLayout_3.addWidget(self.label_5)

        self.frame_14 = QFrame(self.frame)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_14)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_17 = QFrame(self.frame_10)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_17)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_17)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_18)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_5)

        self.frame_2 = QFrame(self.frame_18)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_21.addWidget(self.frame_2)

        self.label_9 = QLabel(self.frame_18)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout_21.addWidget(self.label_9)

        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.formLayout_5 = QFormLayout(self.frame_19)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.labelVersion_29 = QLabel(self.frame_19)
        self.labelVersion_29.setObjectName(u"labelVersion_29")
        self.labelVersion_29.setLineWidth(1)
        self.labelVersion_29.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.labelVersion_29)

        self.nomProFilText = QLineEdit(self.frame_19)
        self.nomProFilText.setObjectName(u"nomProFilText")
        self.nomProFilText.setMinimumSize(QSize(0, 30))

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.nomProFilText)

        self.labelVersion_28 = QLabel(self.frame_19)
        self.labelVersion_28.setObjectName(u"labelVersion_28")
        self.labelVersion_28.setLineWidth(1)
        self.labelVersion_28.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.labelVersion_28)

        self.catProFilCombo = QComboBox(self.frame_19)
        self.catProFilCombo.addItem("")
        self.catProFilCombo.addItem("")
        self.catProFilCombo.addItem("")
        self.catProFilCombo.setObjectName(u"catProFilCombo")
        self.catProFilCombo.setFont(font)
        self.catProFilCombo.setAutoFillBackground(False)
        self.catProFilCombo.setIconSize(QSize(16, 16))
        self.catProFilCombo.setFrame(True)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.catProFilCombo)


        self.verticalLayout_21.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pedResButton = QPushButton(self.frame_20)
        self.pedResButton.setObjectName(u"pedResButton")
        self.pedResButton.setMinimumSize(QSize(120, 30))
        self.pedResButton.setFont(font)
        self.pedResButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-magnifying-glass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pedResButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.pedResButton)

        self.pedBusButton = QPushButton(self.frame_20)
        self.pedBusButton.setObjectName(u"pedBusButton")
        self.pedBusButton.setMinimumSize(QSize(120, 30))
        self.pedBusButton.setFont(font)
        self.pedBusButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-find-in-page.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pedBusButton.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.pedBusButton)


        self.verticalLayout_21.addWidget(self.frame_20)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_7)


        self.horizontalLayout_11.addWidget(self.frame_18)

        self.proTable = QTableWidget(self.frame_16)
        if (self.proTable.columnCount() < 1):
            self.proTable.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.proTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.proTable.rowCount() < 10):
            self.proTable.setRowCount(10)
        font1 = QFont()
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.proTable.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(4, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(5, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(6, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(7, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(8, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(9, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.proTable.setItem(0, 0, __qtablewidgetitem11)
        self.proTable.setObjectName(u"proTable")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proTable.sizePolicy().hasHeightForWidth())
        self.proTable.setSizePolicy(sizePolicy)
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

        self.horizontalLayout_11.addWidget(self.proTable)


        self.verticalLayout_22.addWidget(self.frame_16)

        self.label_8 = QLabel(self.frame_17)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout_22.addWidget(self.label_8)

        self.frame_21 = QFrame(self.frame_17)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 0))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.formLayout_6 = QFormLayout(self.frame_21)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.labelVersion_33 = QLabel(self.frame_21)
        self.labelVersion_33.setObjectName(u"labelVersion_33")
        self.labelVersion_33.setLineWidth(1)
        self.labelVersion_33.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.labelVersion_33)

        self.nomProSelText = QLineEdit(self.frame_21)
        self.nomProSelText.setObjectName(u"nomProSelText")
        self.nomProSelText.setMinimumSize(QSize(0, 30))

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.nomProSelText)

        self.labelVersion_34 = QLabel(self.frame_21)
        self.labelVersion_34.setObjectName(u"labelVersion_34")
        self.labelVersion_34.setLineWidth(1)
        self.labelVersion_34.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.labelVersion_34)

        self.desProSelText = QLineEdit(self.frame_21)
        self.desProSelText.setObjectName(u"desProSelText")
        self.desProSelText.setMinimumSize(QSize(0, 30))

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.desProSelText)

        self.labelVersion_32 = QLabel(self.frame_21)
        self.labelVersion_32.setObjectName(u"labelVersion_32")
        self.labelVersion_32.setLineWidth(1)
        self.labelVersion_32.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.labelVersion_32)

        self.catProSelText = QLineEdit(self.frame_21)
        self.catProSelText.setObjectName(u"catProSelText")
        self.catProSelText.setMinimumSize(QSize(0, 30))

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.catProSelText)

        self.labelVersion_31 = QLabel(self.frame_21)
        self.labelVersion_31.setObjectName(u"labelVersion_31")
        self.labelVersion_31.setLineWidth(1)
        self.labelVersion_31.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_6.setWidget(3, QFormLayout.LabelRole, self.labelVersion_31)

        self.frame_6 = QFrame(self.frame_21)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.proFotLabel = QLabel(self.frame_6)
        self.proFotLabel.setObjectName(u"proFotLabel")
        self.proFotLabel.setMinimumSize(QSize(120, 120))
        self.proFotLabel.setMaximumSize(QSize(120, 120))
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

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_7)


        self.formLayout_6.setWidget(3, QFormLayout.FieldRole, self.frame_6)


        self.verticalLayout_22.addWidget(self.frame_21)


        self.verticalLayout_4.addWidget(self.frame_17)


        self.horizontalLayout_10.addWidget(self.frame_10)

        self.frame_13 = QFrame(self.frame_14)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_13)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_11 = QLabel(self.frame_13)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.verticalLayout_19.addWidget(self.label_11)

        self.frame_4 = QFrame(self.frame_13)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.labelVersion_37 = QLabel(self.frame_3)
        self.labelVersion_37.setObjectName(u"labelVersion_37")
        self.labelVersion_37.setLineWidth(1)
        self.labelVersion_37.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelVersion_37, 0, 0, 1, 1)

        self.labelVersion_30 = QLabel(self.frame_3)
        self.labelVersion_30.setObjectName(u"labelVersion_30")
        self.labelVersion_30.setLineWidth(1)
        self.labelVersion_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelVersion_30, 0, 1, 1, 1)

        self.labelVersion_36 = QLabel(self.frame_3)
        self.labelVersion_36.setObjectName(u"labelVersion_36")
        self.labelVersion_36.setLineWidth(1)
        self.labelVersion_36.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelVersion_36, 0, 2, 1, 1)

        self.labelVersion_38 = QLabel(self.frame_3)
        self.labelVersion_38.setObjectName(u"labelVersion_38")
        self.labelVersion_38.setLineWidth(1)
        self.labelVersion_38.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelVersion_38, 0, 3, 1, 1)

        self.canProSelText = QLineEdit(self.frame_3)
        self.canProSelText.setObjectName(u"canProSelText")
        self.canProSelText.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.canProSelText, 1, 0, 1, 1)

        self.textCantDis = QLineEdit(self.frame_3)
        self.textCantDis.setObjectName(u"textCantDis")
        self.textCantDis.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.textCantDis, 1, 1, 1, 1)

        self.textPrecioPro = QLineEdit(self.frame_3)
        self.textPrecioPro.setObjectName(u"textPrecioPro")
        self.textPrecioPro.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.textPrecioPro, 1, 2, 1, 1)

        self.textCantAdd = QLineEdit(self.frame_3)
        self.textCantAdd.setObjectName(u"textCantAdd")
        self.textCantAdd.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.textCantAdd, 1, 3, 1, 1)


        self.horizontalLayout_6.addWidget(self.frame_3)


        self.verticalLayout_19.addWidget(self.frame_4)

        self.label_12 = QLabel(self.frame_13)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.verticalLayout_19.addWidget(self.label_12)

        self.tableFactura = QTableWidget(self.frame_13)
        if (self.tableFactura.columnCount() < 4):
            self.tableFactura.setColumnCount(4)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableFactura.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableFactura.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableFactura.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableFactura.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        if (self.tableFactura.rowCount() < 10):
            self.tableFactura.setRowCount(10)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font1);
        self.tableFactura.setVerticalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableFactura.setVerticalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableFactura.setVerticalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableFactura.setVerticalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableFactura.setVerticalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableFactura.setVerticalHeaderItem(5, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableFactura.setVerticalHeaderItem(6, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableFactura.setVerticalHeaderItem(7, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableFactura.setVerticalHeaderItem(8, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableFactura.setVerticalHeaderItem(9, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableFactura.setItem(0, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableFactura.setItem(0, 1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableFactura.setItem(0, 2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableFactura.setItem(0, 3, __qtablewidgetitem29)
        self.tableFactura.setObjectName(u"tableFactura")
        sizePolicy.setHeightForWidth(self.tableFactura.sizePolicy().hasHeightForWidth())
        self.tableFactura.setSizePolicy(sizePolicy)
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
        self.tableFactura.setPalette(palette)
        self.tableFactura.setFrameShape(QFrame.NoFrame)
        self.tableFactura.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableFactura.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableFactura.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableFactura.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableFactura.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableFactura.setShowGrid(True)
        self.tableFactura.setGridStyle(Qt.SolidLine)
        self.tableFactura.setSortingEnabled(False)
        self.tableFactura.horizontalHeader().setVisible(True)
        self.tableFactura.horizontalHeader().setCascadingSectionResizes(True)
        self.tableFactura.horizontalHeader().setDefaultSectionSize(150)
        self.tableFactura.horizontalHeader().setStretchLastSection(True)
        self.tableFactura.verticalHeader().setVisible(False)
        self.tableFactura.verticalHeader().setCascadingSectionResizes(False)
        self.tableFactura.verticalHeader().setHighlightSections(False)
        self.tableFactura.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_19.addWidget(self.tableFactura)

        self.frame_11 = QFrame(self.frame_13)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.venButtonDel = QPushButton(self.frame_11)
        self.venButtonDel.setObjectName(u"venButtonDel")
        self.venButtonDel.setMinimumSize(QSize(150, 30))
        self.venButtonDel.setFont(font)
        self.venButtonDel.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.venButtonDel.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.venButtonDel)

        self.venButtonAdd = QPushButton(self.frame_11)
        self.venButtonAdd.setObjectName(u"venButtonAdd")
        self.venButtonAdd.setMinimumSize(QSize(150, 30))
        self.venButtonAdd.setFont(font)
        self.venButtonAdd.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-arrow-circle-bottom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.venButtonAdd.setIcon(icon3)

        self.horizontalLayout_4.addWidget(self.venButtonAdd)


        self.verticalLayout_19.addWidget(self.frame_11)

        self.label_15 = QLabel(self.frame_13)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.verticalLayout_19.addWidget(self.label_15)

        self.frame_12 = QFrame(self.frame_13)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_15 = QFrame(self.frame_12)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.formLayout_4 = QFormLayout(self.frame_15)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.labelVersion_75 = QLabel(self.frame_15)
        self.labelVersion_75.setObjectName(u"labelVersion_75")
        self.labelVersion_75.setLineWidth(1)
        self.labelVersion_75.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.labelVersion_75)

        self.comboBoxMetodo = QComboBox(self.frame_15)
        self.comboBoxMetodo.addItem("")
        self.comboBoxMetodo.addItem("")
        self.comboBoxMetodo.addItem("")
        self.comboBoxMetodo.setObjectName(u"comboBoxMetodo")
        self.comboBoxMetodo.setFont(font)
        self.comboBoxMetodo.setAutoFillBackground(False)
        self.comboBoxMetodo.setIconSize(QSize(16, 16))
        self.comboBoxMetodo.setFrame(True)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.comboBoxMetodo)

        self.labelVersion_35 = QLabel(self.frame_15)
        self.labelVersion_35.setObjectName(u"labelVersion_35")
        self.labelVersion_35.setLineWidth(1)
        self.labelVersion_35.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.labelVersion_35)

        self.TextTotal = QLineEdit(self.frame_15)
        self.TextTotal.setObjectName(u"TextTotal")
        self.TextTotal.setMinimumSize(QSize(0, 30))

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.TextTotal)


        self.horizontalLayout_3.addWidget(self.frame_15)

        self.frame_5 = QFrame(self.frame_12)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.venButtonFac = QPushButton(self.frame_5)
        self.venButtonFac.setObjectName(u"venButtonFac")
        self.venButtonFac.setMinimumSize(QSize(150, 30))
        self.venButtonFac.setFont(font)
        self.venButtonFac.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-input.png", QSize(), QIcon.Normal, QIcon.Off)
        self.venButtonFac.setIcon(icon4)

        self.verticalLayout_6.addWidget(self.venButtonFac)

        self.venButtonRei = QPushButton(self.frame_5)
        self.venButtonRei.setObjectName(u"venButtonRei")
        self.venButtonRei.setMinimumSize(QSize(150, 30))
        self.venButtonRei.setFont(font)
        self.venButtonRei.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-history.png", QSize(), QIcon.Normal, QIcon.Off)
        self.venButtonRei.setIcon(icon5)

        self.verticalLayout_6.addWidget(self.venButtonRei)


        self.horizontalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_19.addWidget(self.frame_12)


        self.horizontalLayout_10.addWidget(self.frame_13)


        self.verticalLayout_3.addWidget(self.frame_14)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(ventas)

        self.catProFilCombo.setCurrentIndex(-1)
        self.comboBoxMetodo.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(ventas)
    # setupUi

    def retranslateUi(self, ventas):
        ventas.setWindowTitle(QCoreApplication.translate("ventas", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("ventas", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Ventas</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("ventas", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Filtrar Producto</span></p></body></html>", None))
        self.labelVersion_29.setText(QCoreApplication.translate("ventas", u"Nombre", None))
        self.nomProFilText.setText("")
        self.nomProFilText.setPlaceholderText(QCoreApplication.translate("ventas", u"Ingrese el nombre", None))
        self.labelVersion_28.setText(QCoreApplication.translate("ventas", u"Categor\u00eda", None))
        self.catProFilCombo.setItemText(0, QCoreApplication.translate("ventas", u"Fotocopiado", None))
        self.catProFilCombo.setItemText(1, QCoreApplication.translate("ventas", u"Impresi\u00f3n", None))
        self.catProFilCombo.setItemText(2, QCoreApplication.translate("ventas", u"Laminado", None))

        self.catProFilCombo.setPlaceholderText(QCoreApplication.translate("ventas", u"Seleccione una opci\u00f3n", None))
        self.pedResButton.setText(QCoreApplication.translate("ventas", u"Mostrar Todos", None))
        self.pedBusButton.setText(QCoreApplication.translate("ventas", u"Filtar", None))
        ___qtablewidgetitem = self.proTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ventas", u"0", None));
        ___qtablewidgetitem1 = self.proTable.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ventas", u"New Row", None));
        ___qtablewidgetitem2 = self.proTable.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ventas", u"New Row", None));
        ___qtablewidgetitem3 = self.proTable.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ventas", u"New Row", None));
        ___qtablewidgetitem4 = self.proTable.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ventas", u"New Row", None));
        ___qtablewidgetitem5 = self.proTable.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ventas", u"New Row", None));
        ___qtablewidgetitem6 = self.proTable.verticalHeaderItem(5)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("ventas", u"New Row", None));
        ___qtablewidgetitem7 = self.proTable.verticalHeaderItem(6)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("ventas", u"New Row", None));
        ___qtablewidgetitem8 = self.proTable.verticalHeaderItem(7)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("ventas", u"New Row", None));
        ___qtablewidgetitem9 = self.proTable.verticalHeaderItem(8)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("ventas", u"New Row", None));
        ___qtablewidgetitem10 = self.proTable.verticalHeaderItem(9)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("ventas", u"New Row", None));

        __sortingEnabled = self.proTable.isSortingEnabled()
        self.proTable.setSortingEnabled(False)
        ___qtablewidgetitem11 = self.proTable.item(0, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("ventas", u"Producto", None));
        self.proTable.setSortingEnabled(__sortingEnabled)

        self.label_8.setText(QCoreApplication.translate("ventas", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Producto Seleccionado</span></p></body></html>", None))
        self.labelVersion_33.setText(QCoreApplication.translate("ventas", u"Nombre Producto", None))
        self.nomProSelText.setText("")
        self.labelVersion_34.setText(QCoreApplication.translate("ventas", u"Descripci\u00f3n", None))
        self.desProSelText.setText("")
        self.labelVersion_32.setText(QCoreApplication.translate("ventas", u"Categor\u00eda", None))
        self.catProSelText.setText("")
        self.labelVersion_31.setText(QCoreApplication.translate("ventas", u"Foto", None))
        self.label_11.setText(QCoreApplication.translate("ventas", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Agregar Producto Seleccionado</span></p></body></html>", None))
        self.labelVersion_37.setText(QCoreApplication.translate("ventas", u"Cantidad en Inventario", None))
        self.labelVersion_30.setText(QCoreApplication.translate("ventas", u"Cantidad Stock", None))
        self.labelVersion_36.setText(QCoreApplication.translate("ventas", u"Precio", None))
        self.labelVersion_38.setText(QCoreApplication.translate("ventas", u"Cantidad Agregar", None))
        self.canProSelText.setText("")
        self.textCantDis.setText("")
        self.textPrecioPro.setText("")
        self.textCantAdd.setText("")
        self.textCantAdd.setPlaceholderText(QCoreApplication.translate("ventas", u"Ingrese la cantidad", None))
        self.label_12.setText(QCoreApplication.translate("ventas", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Productos en Factura</span></p></body></html>", None))
        ___qtablewidgetitem12 = self.tableFactura.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("ventas", u"0", None));
        ___qtablewidgetitem13 = self.tableFactura.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("ventas", u"1", None));
        ___qtablewidgetitem14 = self.tableFactura.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("ventas", u"2", None));
        ___qtablewidgetitem15 = self.tableFactura.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("ventas", u"3", None));
        ___qtablewidgetitem16 = self.tableFactura.verticalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("ventas", u"New Row", None));
        ___qtablewidgetitem17 = self.tableFactura.verticalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("ventas", u"New Row", None));
        ___qtablewidgetitem18 = self.tableFactura.verticalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("ventas", u"New Row", None));
        ___qtablewidgetitem19 = self.tableFactura.verticalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("ventas", u"New Row", None));
        ___qtablewidgetitem20 = self.tableFactura.verticalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("ventas", u"New Row", None));
        ___qtablewidgetitem21 = self.tableFactura.verticalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("ventas", u"New Row", None));
        ___qtablewidgetitem22 = self.tableFactura.verticalHeaderItem(6)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("ventas", u"New Row", None));
        ___qtablewidgetitem23 = self.tableFactura.verticalHeaderItem(7)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("ventas", u"New Row", None));
        ___qtablewidgetitem24 = self.tableFactura.verticalHeaderItem(8)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("ventas", u"New Row", None));
        ___qtablewidgetitem25 = self.tableFactura.verticalHeaderItem(9)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("ventas", u"New Row", None));

        __sortingEnabled1 = self.tableFactura.isSortingEnabled()
        self.tableFactura.setSortingEnabled(False)
        ___qtablewidgetitem26 = self.tableFactura.item(0, 0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("ventas", u"Producto", None));
        ___qtablewidgetitem27 = self.tableFactura.item(0, 1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("ventas", u"Cantidad", None));
        ___qtablewidgetitem28 = self.tableFactura.item(0, 2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("ventas", u"Valor Unitario", None));
        ___qtablewidgetitem29 = self.tableFactura.item(0, 3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("ventas", u"Total Producto", None));
        self.tableFactura.setSortingEnabled(__sortingEnabled1)

        self.venButtonDel.setText(QCoreApplication.translate("ventas", u"Eliminar", None))
        self.venButtonAdd.setText(QCoreApplication.translate("ventas", u"Agregar", None))
        self.label_15.setText(QCoreApplication.translate("ventas", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Generar Factura</span></p></body></html>", None))
        self.labelVersion_75.setText(QCoreApplication.translate("ventas", u"Metodo de Pago:", None))
        self.comboBoxMetodo.setItemText(0, QCoreApplication.translate("ventas", u"Fotocopiado", None))
        self.comboBoxMetodo.setItemText(1, QCoreApplication.translate("ventas", u"Impresi\u00f3n", None))
        self.comboBoxMetodo.setItemText(2, QCoreApplication.translate("ventas", u"Laminado", None))

        self.comboBoxMetodo.setPlaceholderText(QCoreApplication.translate("ventas", u"Seleccione una opci\u00f3n", None))
        self.labelVersion_35.setText(QCoreApplication.translate("ventas", u"Valor Total", None))
        self.TextTotal.setText("")
        self.venButtonFac.setText(QCoreApplication.translate("ventas", u"Generar Factura", None))
        self.venButtonRei.setText(QCoreApplication.translate("ventas", u"Reiniciar", None))
    # retranslateUi

