# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pedidojrtlyG.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_pedidos(object):
    def setupUi(self, pedidos):
        if not pedidos.objectName():
            pedidos.setObjectName(u"pedidos")
        pedidos.resize(1182, 608)
        self.verticalLayout = QVBoxLayout(pedidos)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(pedidos)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_5.setFont(font)

        self.verticalLayout_2.addWidget(self.label_5)

        self.frame_18 = QFrame(self.frame)
        self.frame_18.setObjectName(u"frame_18")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush1 = QBrush(QColor(0, 120, 215, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush2 = QBrush(QColor(240, 240, 240, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush2)
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush1)
        self.frame_18.setPalette(palette)
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_18)
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
        self.horizontalLayout_10 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.frame_16)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_15)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_5)

        self.frame_2 = QFrame(self.frame_15)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_21.addWidget(self.frame_2)

        self.label_9 = QLabel(self.frame_15)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout_21.addWidget(self.label_9)

        self.frame_13 = QFrame(self.frame_15)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.formLayout_5 = QFormLayout(self.frame_13)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.labelVersion_29 = QLabel(self.frame_13)
        self.labelVersion_29.setObjectName(u"labelVersion_29")
        self.labelVersion_29.setLineWidth(1)
        self.labelVersion_29.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.labelVersion_29)

        self.nomProFilText = QLineEdit(self.frame_13)
        self.nomProFilText.setObjectName(u"nomProFilText")
        self.nomProFilText.setMinimumSize(QSize(0, 30))

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.nomProFilText)

        self.labelVersion_28 = QLabel(self.frame_13)
        self.labelVersion_28.setObjectName(u"labelVersion_28")
        self.labelVersion_28.setLineWidth(1)
        self.labelVersion_28.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.labelVersion_28)

        self.catProFilCombo = QComboBox(self.frame_13)
        self.catProFilCombo.addItem("")
        self.catProFilCombo.addItem("")
        self.catProFilCombo.addItem("")
        self.catProFilCombo.setObjectName(u"catProFilCombo")
        self.catProFilCombo.setFont(font)
        self.catProFilCombo.setAutoFillBackground(False)
        self.catProFilCombo.setIconSize(QSize(16, 16))
        self.catProFilCombo.setFrame(True)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.catProFilCombo)


        self.verticalLayout_21.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_15)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pedBusButton = QPushButton(self.frame_14)
        self.pedBusButton.setObjectName(u"pedBusButton")
        self.pedBusButton.setMinimumSize(QSize(120, 30))
        self.pedBusButton.setFont(font)
        self.pedBusButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-find-in-page.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pedBusButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.pedBusButton)


        self.verticalLayout_21.addWidget(self.frame_14)

        self.frame_5 = QFrame(self.frame_15)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pedResButton = QPushButton(self.frame_5)
        self.pedResButton.setObjectName(u"pedResButton")
        self.pedResButton.setMinimumSize(QSize(120, 30))
        self.pedResButton.setFont(font)
        self.pedResButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-magnifying-glass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pedResButton.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.pedResButton)

        self.pedEscButton = QPushButton(self.frame_5)
        self.pedEscButton.setObjectName(u"pedEscButton")
        self.pedEscButton.setMinimumSize(QSize(120, 30))
        self.pedEscButton.setFont(font)
        self.pedEscButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pedEscButton.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.pedEscButton)


        self.verticalLayout_21.addWidget(self.frame_5)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_7)


        self.horizontalLayout_10.addWidget(self.frame_15)

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

        self.horizontalLayout_10.addWidget(self.proTable)


        self.verticalLayout_22.addWidget(self.frame_16)

        self.label_8 = QLabel(self.frame_17)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout_22.addWidget(self.label_8)

        self.frame_12 = QFrame(self.frame_17)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 0))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.formLayout_4 = QFormLayout(self.frame_12)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.labelVersion_33 = QLabel(self.frame_12)
        self.labelVersion_33.setObjectName(u"labelVersion_33")
        self.labelVersion_33.setLineWidth(1)
        self.labelVersion_33.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.labelVersion_33)

        self.nomProSelText = QLineEdit(self.frame_12)
        self.nomProSelText.setObjectName(u"nomProSelText")
        self.nomProSelText.setMinimumSize(QSize(0, 30))

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.nomProSelText)

        self.labelVersion_34 = QLabel(self.frame_12)
        self.labelVersion_34.setObjectName(u"labelVersion_34")
        self.labelVersion_34.setLineWidth(1)
        self.labelVersion_34.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.labelVersion_34)

        self.desProSelText = QLineEdit(self.frame_12)
        self.desProSelText.setObjectName(u"desProSelText")
        self.desProSelText.setMinimumSize(QSize(0, 30))

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.desProSelText)

        self.labelVersion_32 = QLabel(self.frame_12)
        self.labelVersion_32.setObjectName(u"labelVersion_32")
        self.labelVersion_32.setLineWidth(1)
        self.labelVersion_32.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.labelVersion_32)

        self.catProSelText = QLineEdit(self.frame_12)
        self.catProSelText.setObjectName(u"catProSelText")
        self.catProSelText.setMinimumSize(QSize(0, 30))

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.catProSelText)

        self.labelVersion_31 = QLabel(self.frame_12)
        self.labelVersion_31.setObjectName(u"labelVersion_31")
        self.labelVersion_31.setLineWidth(1)
        self.labelVersion_31.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.labelVersion_31)

        self.frame_3 = QFrame(self.frame_12)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.proFotLabel = QLabel(self.frame_3)
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

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.labelVersion_30 = QLabel(self.frame_4)
        self.labelVersion_30.setObjectName(u"labelVersion_30")
        self.labelVersion_30.setLineWidth(1)
        self.labelVersion_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.labelVersion_30)

        self.canProSelText = QLineEdit(self.frame_4)
        self.canProSelText.setObjectName(u"canProSelText")
        self.canProSelText.setMinimumSize(QSize(0, 30))

        self.verticalLayout_5.addWidget(self.canProSelText)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_4)


        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.frame_3)


        self.verticalLayout_22.addWidget(self.frame_12)


        self.horizontalLayout_11.addWidget(self.frame_17)

        self.frame_6 = QFrame(self.frame_18)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.verticalLayout_19.addWidget(self.label_10)

        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_11)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.formLayout_3 = QFormLayout(self.frame_10)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.labelVersion_36 = QLabel(self.frame_10)
        self.labelVersion_36.setObjectName(u"labelVersion_36")
        self.labelVersion_36.setLineWidth(1)
        self.labelVersion_36.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.labelVersion_36)

        self.pedCosText = QLineEdit(self.frame_10)
        self.pedCosText.setObjectName(u"pedCosText")
        self.pedCosText.setMinimumSize(QSize(0, 30))

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.pedCosText)

        self.labelVersion_42 = QLabel(self.frame_10)
        self.labelVersion_42.setObjectName(u"labelVersion_42")
        self.labelVersion_42.setLineWidth(1)
        self.labelVersion_42.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.labelVersion_42)

        self.pedCanText = QLineEdit(self.frame_10)
        self.pedCanText.setObjectName(u"pedCanText")
        self.pedCanText.setMinimumSize(QSize(0, 30))

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.pedCanText)


        self.horizontalLayout_9.addWidget(self.frame_10)

        self.pedAddButton = QPushButton(self.frame_11)
        self.pedAddButton.setObjectName(u"pedAddButton")
        self.pedAddButton.setMinimumSize(QSize(150, 30))
        self.pedAddButton.setFont(font)
        self.pedAddButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/cil-arrow-circle-bottom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pedAddButton.setIcon(icon2)

        self.horizontalLayout_9.addWidget(self.pedAddButton)


        self.verticalLayout_19.addWidget(self.frame_11)

        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.verticalLayout_19.addWidget(self.label_11)

        self.pedTable = QTableWidget(self.frame_6)
        if (self.pedTable.columnCount() < 4):
            self.pedTable.setColumnCount(4)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.pedTable.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.pedTable.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.pedTable.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.pedTable.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        if (self.pedTable.rowCount() < 10):
            self.pedTable.setRowCount(10)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font1);
        self.pedTable.setVerticalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.pedTable.setVerticalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.pedTable.setVerticalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.pedTable.setVerticalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.pedTable.setVerticalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.pedTable.setVerticalHeaderItem(5, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.pedTable.setVerticalHeaderItem(6, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.pedTable.setVerticalHeaderItem(7, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.pedTable.setVerticalHeaderItem(8, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.pedTable.setVerticalHeaderItem(9, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.pedTable.setItem(0, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.pedTable.setItem(0, 1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.pedTable.setItem(0, 2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.pedTable.setItem(0, 3, __qtablewidgetitem29)
        self.pedTable.setObjectName(u"pedTable")
        sizePolicy.setHeightForWidth(self.pedTable.sizePolicy().hasHeightForWidth())
        self.pedTable.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        brush4 = QBrush(QColor(51, 51, 51, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        brush5 = QBrush(QColor(0, 0, 0, 0))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        brush8 = QBrush(QColor(0, 0, 0, 255))
        brush8.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.pedTable.setPalette(palette1)
        self.pedTable.setFrameShape(QFrame.NoFrame)
        self.pedTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.pedTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.pedTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.pedTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.pedTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.pedTable.setShowGrid(True)
        self.pedTable.setGridStyle(Qt.SolidLine)
        self.pedTable.setSortingEnabled(False)
        self.pedTable.horizontalHeader().setVisible(True)
        self.pedTable.horizontalHeader().setCascadingSectionResizes(True)
        self.pedTable.horizontalHeader().setDefaultSectionSize(150)
        self.pedTable.horizontalHeader().setStretchLastSection(True)
        self.pedTable.verticalHeader().setVisible(False)
        self.pedTable.verticalHeader().setCascadingSectionResizes(False)
        self.pedTable.verticalHeader().setHighlightSections(False)
        self.pedTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_19.addWidget(self.pedTable)

        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.verticalLayout_19.addWidget(self.label_12)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_9)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_8)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.labelVersion_47 = QLabel(self.frame_8)
        self.labelVersion_47.setObjectName(u"labelVersion_47")
        self.labelVersion_47.setLineWidth(1)
        self.labelVersion_47.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.labelVersion_47)

        self.pedNomText = QLineEdit(self.frame_8)
        self.pedNomText.setObjectName(u"pedNomText")
        self.pedNomText.setMinimumSize(QSize(0, 30))

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.pedNomText)

        self.labelVersion_48 = QLabel(self.frame_8)
        self.labelVersion_48.setObjectName(u"labelVersion_48")
        self.labelVersion_48.setLineWidth(1)
        self.labelVersion_48.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.labelVersion_48)

        self.pedEstText = QLineEdit(self.frame_8)
        self.pedEstText.setObjectName(u"pedEstText")
        self.pedEstText.setMinimumSize(QSize(0, 30))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.pedEstText)


        self.horizontalLayout_8.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.frame_9)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_7)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.pedRecButton = QPushButton(self.frame_7)
        self.pedRecButton.setObjectName(u"pedRecButton")
        self.pedRecButton.setMinimumSize(QSize(150, 30))
        self.pedRecButton.setFont(font)
        self.pedRecButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-check-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pedRecButton.setIcon(icon3)

        self.verticalLayout_18.addWidget(self.pedRecButton)

        self.pedCanButton = QPushButton(self.frame_7)
        self.pedCanButton.setObjectName(u"pedCanButton")
        self.pedCanButton.setMinimumSize(QSize(150, 30))
        self.pedCanButton.setFont(font)
        self.pedCanButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pedCanButton.setIcon(icon4)

        self.verticalLayout_18.addWidget(self.pedCanButton)


        self.horizontalLayout_8.addWidget(self.frame_7)


        self.verticalLayout_19.addWidget(self.frame_9)


        self.horizontalLayout_11.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.frame_18)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(pedidos)

        self.catProFilCombo.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(pedidos)
    # setupUi

    def retranslateUi(self, pedidos):
        pedidos.setWindowTitle(QCoreApplication.translate("pedidos", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("pedidos", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Pedidos</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("pedidos", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Filtrar Producto</span></p></body></html>", None))
        self.labelVersion_29.setText(QCoreApplication.translate("pedidos", u"Nombre", None))
        self.nomProFilText.setText("")
        self.nomProFilText.setPlaceholderText(QCoreApplication.translate("pedidos", u"Ingrese el nombre del producto", None))
        self.labelVersion_28.setText(QCoreApplication.translate("pedidos", u"Categor\u00eda", None))
        self.catProFilCombo.setItemText(0, QCoreApplication.translate("pedidos", u"Fotocopiado", None))
        self.catProFilCombo.setItemText(1, QCoreApplication.translate("pedidos", u"Impresi\u00f3n", None))
        self.catProFilCombo.setItemText(2, QCoreApplication.translate("pedidos", u"Laminado", None))

        self.catProFilCombo.setPlaceholderText(QCoreApplication.translate("pedidos", u"Seleccione una opci\u00f3n", None))
        self.pedBusButton.setText(QCoreApplication.translate("pedidos", u"Filtar", None))
        self.pedResButton.setText(QCoreApplication.translate("pedidos", u"Mostrar Todos", None))
        self.pedEscButton.setText(QCoreApplication.translate("pedidos", u"En Escasez", None))
        ___qtablewidgetitem = self.proTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("pedidos", u"0", None));
        ___qtablewidgetitem1 = self.proTable.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("pedidos", u"New Row", None));
        ___qtablewidgetitem2 = self.proTable.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("pedidos", u"New Row", None));
        ___qtablewidgetitem3 = self.proTable.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("pedidos", u"New Row", None));
        ___qtablewidgetitem4 = self.proTable.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("pedidos", u"New Row", None));
        ___qtablewidgetitem5 = self.proTable.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("pedidos", u"New Row", None));
        ___qtablewidgetitem6 = self.proTable.verticalHeaderItem(5)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("pedidos", u"New Row", None));
        ___qtablewidgetitem7 = self.proTable.verticalHeaderItem(6)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("pedidos", u"New Row", None));
        ___qtablewidgetitem8 = self.proTable.verticalHeaderItem(7)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("pedidos", u"New Row", None));
        ___qtablewidgetitem9 = self.proTable.verticalHeaderItem(8)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("pedidos", u"New Row", None));
        ___qtablewidgetitem10 = self.proTable.verticalHeaderItem(9)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("pedidos", u"New Row", None));

        __sortingEnabled = self.proTable.isSortingEnabled()
        self.proTable.setSortingEnabled(False)
        ___qtablewidgetitem11 = self.proTable.item(0, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("pedidos", u"Producto", None));
        self.proTable.setSortingEnabled(__sortingEnabled)

        self.label_8.setText(QCoreApplication.translate("pedidos", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Producto Seleccionado</span></p></body></html>", None))
        self.labelVersion_33.setText(QCoreApplication.translate("pedidos", u"Nombre Producto", None))
        self.nomProSelText.setText("")
        self.nomProSelText.setPlaceholderText("")
        self.labelVersion_34.setText(QCoreApplication.translate("pedidos", u"Descripci\u00f3n", None))
        self.desProSelText.setText("")
        self.desProSelText.setPlaceholderText("")
        self.labelVersion_32.setText(QCoreApplication.translate("pedidos", u"Categor\u00eda", None))
        self.catProSelText.setText("")
        self.catProSelText.setPlaceholderText("")
        self.labelVersion_31.setText(QCoreApplication.translate("pedidos", u"Foto", None))
        self.labelVersion_30.setText(QCoreApplication.translate("pedidos", u"Cantidad Disponible", None))
        self.canProSelText.setText("")
        self.canProSelText.setPlaceholderText("")
        self.label_10.setText(QCoreApplication.translate("pedidos", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Generar un Pedido</span></p></body></html>", None))
        self.labelVersion_36.setText(QCoreApplication.translate("pedidos", u"Costo Unitario", None))
        self.pedCosText.setText("")
        self.pedCosText.setPlaceholderText(QCoreApplication.translate("pedidos", u"Ingrese el costo unitario del producto", None))
        self.labelVersion_42.setText(QCoreApplication.translate("pedidos", u"Cantidad Pedida", None))
        self.pedCanText.setText("")
        self.pedCanText.setPlaceholderText(QCoreApplication.translate("pedidos", u"Ingrese la cantidad de producto pedido", None))
        self.pedAddButton.setText(QCoreApplication.translate("pedidos", u"Agregar", None))
        self.label_11.setText(QCoreApplication.translate("pedidos", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Lista de Pedidos</span></p></body></html>", None))
        ___qtablewidgetitem12 = self.pedTable.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("pedidos", u"0", None));
        ___qtablewidgetitem13 = self.pedTable.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("pedidos", u"1", None));
        ___qtablewidgetitem14 = self.pedTable.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("pedidos", u"2", None));
        ___qtablewidgetitem15 = self.pedTable.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("pedidos", u"3", None));
        ___qtablewidgetitem16 = self.pedTable.verticalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("pedidos", u"New Row", None));
        ___qtablewidgetitem17 = self.pedTable.verticalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("pedidos", u"New Row", None));
        ___qtablewidgetitem18 = self.pedTable.verticalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("pedidos", u"New Row", None));
        ___qtablewidgetitem19 = self.pedTable.verticalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("pedidos", u"New Row", None));
        ___qtablewidgetitem20 = self.pedTable.verticalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("pedidos", u"New Row", None));
        ___qtablewidgetitem21 = self.pedTable.verticalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("pedidos", u"New Row", None));
        ___qtablewidgetitem22 = self.pedTable.verticalHeaderItem(6)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("pedidos", u"New Row", None));
        ___qtablewidgetitem23 = self.pedTable.verticalHeaderItem(7)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("pedidos", u"New Row", None));
        ___qtablewidgetitem24 = self.pedTable.verticalHeaderItem(8)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("pedidos", u"New Row", None));
        ___qtablewidgetitem25 = self.pedTable.verticalHeaderItem(9)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("pedidos", u"New Row", None));

        __sortingEnabled1 = self.pedTable.isSortingEnabled()
        self.pedTable.setSortingEnabled(False)
        ___qtablewidgetitem26 = self.pedTable.item(0, 0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("pedidos", u"Producto", None));
        ___qtablewidgetitem27 = self.pedTable.item(0, 1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("pedidos", u"Cantidad", None));
        ___qtablewidgetitem28 = self.pedTable.item(0, 2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("pedidos", u"Estado", None));
        ___qtablewidgetitem29 = self.pedTable.item(0, 3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("pedidos", u"Costo", None));
        self.pedTable.setSortingEnabled(__sortingEnabled1)

        self.label_12.setText(QCoreApplication.translate("pedidos", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Pedido Seleccionado</span></p></body></html>", None))
        self.labelVersion_47.setText(QCoreApplication.translate("pedidos", u"Producto", None))
        self.pedNomText.setText("")
        self.pedNomText.setPlaceholderText("")
        self.labelVersion_48.setText(QCoreApplication.translate("pedidos", u"Estado Actual", None))
        self.pedEstText.setText("")
        self.pedEstText.setPlaceholderText("")
        self.pedRecButton.setText(QCoreApplication.translate("pedidos", u"Marcar Recibido", None))
        self.pedCanButton.setText(QCoreApplication.translate("pedidos", u"Marcar Cancelado", None))
    # retranslateUi

