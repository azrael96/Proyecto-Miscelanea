# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stockyxSeFY.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_stock(object):
    def setupUi(self, stock):
        if not stock.objectName():
            stock.setObjectName(u"stock")
        stock.resize(1182, 608)
        stock.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(stock)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(stock)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_3.setFont(font)

        self.verticalLayout_2.addWidget(self.label_3)

        self.frame_32 = QFrame(self.frame)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.frame_32)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMaximumSize(QSize(800, 16777215))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_31)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, -1, 0)
        self.frame_16 = QFrame(self.frame_31)
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
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

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


        self.verticalLayout_3.addWidget(self.frame_16)

        self.label_8 = QLabel(self.frame_31)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout_3.addWidget(self.label_8)

        self.frame_21 = QFrame(self.frame_31)
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
        self.labelVersion_39 = QLabel(self.frame_7)
        self.labelVersion_39.setObjectName(u"labelVersion_39")
        self.labelVersion_39.setLineWidth(1)
        self.labelVersion_39.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.labelVersion_39)

        self.canProSelText = QLineEdit(self.frame_7)
        self.canProSelText.setObjectName(u"canProSelText")
        self.canProSelText.setMinimumSize(QSize(0, 30))

        self.verticalLayout_5.addWidget(self.canProSelText)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_7)


        self.formLayout_6.setWidget(3, QFormLayout.FieldRole, self.frame_6)


        self.verticalLayout_3.addWidget(self.frame_21)


        self.horizontalLayout_16.addWidget(self.frame_31)

        self.frame_27 = QFrame(self.frame_32)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_27)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, 0, 0)
        self.label_22 = QLabel(self.frame_27)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)

        self.verticalLayout_4.addWidget(self.label_22)

        self.invTable = QTableWidget(self.frame_27)
        if (self.invTable.columnCount() < 2):
            self.invTable.setColumnCount(2)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.invTable.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.invTable.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        if (self.invTable.rowCount() < 12):
            self.invTable.setRowCount(12)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font1);
        self.invTable.setVerticalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.invTable.setVerticalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.invTable.setVerticalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.invTable.setVerticalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.invTable.setVerticalHeaderItem(4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.invTable.setVerticalHeaderItem(5, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.invTable.setVerticalHeaderItem(6, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.invTable.setVerticalHeaderItem(7, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.invTable.setVerticalHeaderItem(8, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.invTable.setVerticalHeaderItem(9, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.invTable.setVerticalHeaderItem(10, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.invTable.setVerticalHeaderItem(11, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.invTable.setItem(0, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.invTable.setItem(0, 1, __qtablewidgetitem27)
        self.invTable.setObjectName(u"invTable")
        sizePolicy.setHeightForWidth(self.invTable.sizePolicy().hasHeightForWidth())
        self.invTable.setSizePolicy(sizePolicy)
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
        self.invTable.setPalette(palette)
        self.invTable.setFrameShape(QFrame.NoFrame)
        self.invTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.invTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.invTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.invTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.invTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.invTable.setShowGrid(True)
        self.invTable.setGridStyle(Qt.SolidLine)
        self.invTable.setSortingEnabled(False)
        self.invTable.horizontalHeader().setVisible(True)
        self.invTable.horizontalHeader().setCascadingSectionResizes(True)
        self.invTable.horizontalHeader().setDefaultSectionSize(200)
        self.invTable.horizontalHeader().setStretchLastSection(True)
        self.invTable.verticalHeader().setVisible(False)
        self.invTable.verticalHeader().setCascadingSectionResizes(False)
        self.invTable.verticalHeader().setHighlightSections(False)
        self.invTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_4.addWidget(self.invTable)

        self.frame_24 = QFrame(self.frame_27)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_24)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textCanStock = QLineEdit(self.frame_24)
        self.textCanStock.setObjectName(u"textCanStock")
        self.textCanStock.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.textCanStock, 1, 1, 1, 1)

        self.textCanLote = QLineEdit(self.frame_24)
        self.textCanLote.setObjectName(u"textCanLote")
        self.textCanLote.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.textCanLote, 1, 0, 1, 1)

        self.labelVersion_17 = QLabel(self.frame_24)
        self.labelVersion_17.setObjectName(u"labelVersion_17")
        self.labelVersion_17.setLineWidth(1)
        self.labelVersion_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_17, 0, 0, 1, 1)

        self.labelVersion_16 = QLabel(self.frame_24)
        self.labelVersion_16.setObjectName(u"labelVersion_16")
        self.labelVersion_16.setLineWidth(1)
        self.labelVersion_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_16, 0, 1, 1, 1)

        self.labelVersion_38 = QLabel(self.frame_24)
        self.labelVersion_38.setObjectName(u"labelVersion_38")
        self.labelVersion_38.setLineWidth(1)
        self.labelVersion_38.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_38, 0, 2, 1, 1)

        self.textCosLote = QLineEdit(self.frame_24)
        self.textCosLote.setObjectName(u"textCosLote")
        self.textCosLote.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.textCosLote, 1, 2, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_24)

        self.label_20 = QLabel(self.frame_27)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.verticalLayout_4.addWidget(self.label_20)

        self.frame_25 = QFrame(self.frame_27)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.formLayout_8 = QFormLayout(self.frame_25)
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.labelVersion_18 = QLabel(self.frame_25)
        self.labelVersion_18.setObjectName(u"labelVersion_18")
        self.labelVersion_18.setLineWidth(1)
        self.labelVersion_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.labelVersion_18)

        self.labelVersion_37 = QLabel(self.frame_25)
        self.labelVersion_37.setObjectName(u"labelVersion_37")
        self.labelVersion_37.setLineWidth(1)
        self.labelVersion_37.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.labelVersion_37)

        self.textValVen = QLineEdit(self.frame_25)
        self.textValVen.setObjectName(u"textValVen")
        self.textValVen.setMinimumSize(QSize(0, 30))

        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.textValVen)

        self.textCanTrans = QLineEdit(self.frame_25)
        self.textCanTrans.setObjectName(u"textCanTrans")
        self.textCanTrans.setMinimumSize(QSize(0, 30))

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.textCanTrans)


        self.verticalLayout_4.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_27)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_7)

        self.ButtonTrans = QPushButton(self.frame_26)
        self.ButtonTrans.setObjectName(u"ButtonTrans")
        self.ButtonTrans.setMinimumSize(QSize(150, 30))
        self.ButtonTrans.setFont(font)
        self.ButtonTrans.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/cil-arrow-circle-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ButtonTrans.setIcon(icon2)

        self.horizontalLayout_14.addWidget(self.ButtonTrans)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_8)


        self.verticalLayout_4.addWidget(self.frame_26)


        self.horizontalLayout_16.addWidget(self.frame_27)


        self.verticalLayout_2.addWidget(self.frame_32)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(stock)

        self.catProFilCombo.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(stock)
    # setupUi

    def retranslateUi(self, stock):
        stock.setWindowTitle(QCoreApplication.translate("stock", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("stock", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Stock</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("stock", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Filtrar Producto</span></p></body></html>", None))
        self.labelVersion_29.setText(QCoreApplication.translate("stock", u"Nombre", None))
        self.nomProFilText.setText("")
        self.nomProFilText.setPlaceholderText(QCoreApplication.translate("stock", u"Ingrese el nombre del producto", None))
        self.labelVersion_28.setText(QCoreApplication.translate("stock", u"Categor\u00eda", None))
        self.catProFilCombo.setItemText(0, QCoreApplication.translate("stock", u"Fotocopiado", None))
        self.catProFilCombo.setItemText(1, QCoreApplication.translate("stock", u"Impresi\u00f3n", None))
        self.catProFilCombo.setItemText(2, QCoreApplication.translate("stock", u"Laminado", None))

        self.catProFilCombo.setPlaceholderText(QCoreApplication.translate("stock", u"Seleccione una opci\u00f3n", None))
        self.pedResButton.setText(QCoreApplication.translate("stock", u"Mostrar Todos", None))
        self.pedBusButton.setText(QCoreApplication.translate("stock", u"Filtar", None))
        ___qtablewidgetitem = self.proTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("stock", u"0", None));
        ___qtablewidgetitem1 = self.proTable.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("stock", u"New Row", None));
        ___qtablewidgetitem2 = self.proTable.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("stock", u"New Row", None));
        ___qtablewidgetitem3 = self.proTable.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("stock", u"New Row", None));
        ___qtablewidgetitem4 = self.proTable.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("stock", u"New Row", None));
        ___qtablewidgetitem5 = self.proTable.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("stock", u"New Row", None));
        ___qtablewidgetitem6 = self.proTable.verticalHeaderItem(5)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("stock", u"New Row", None));
        ___qtablewidgetitem7 = self.proTable.verticalHeaderItem(6)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("stock", u"New Row", None));
        ___qtablewidgetitem8 = self.proTable.verticalHeaderItem(7)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("stock", u"New Row", None));
        ___qtablewidgetitem9 = self.proTable.verticalHeaderItem(8)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("stock", u"New Row", None));
        ___qtablewidgetitem10 = self.proTable.verticalHeaderItem(9)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("stock", u"New Row", None));

        __sortingEnabled = self.proTable.isSortingEnabled()
        self.proTable.setSortingEnabled(False)
        ___qtablewidgetitem11 = self.proTable.item(0, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("stock", u"Producto", None));
        self.proTable.setSortingEnabled(__sortingEnabled)

        self.label_8.setText(QCoreApplication.translate("stock", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Producto Seleccionado</span></p></body></html>", None))
        self.labelVersion_33.setText(QCoreApplication.translate("stock", u"Nombre Producto", None))
        self.nomProSelText.setText("")
        self.labelVersion_34.setText(QCoreApplication.translate("stock", u"Descripci\u00f3n", None))
        self.desProSelText.setText("")
        self.labelVersion_32.setText(QCoreApplication.translate("stock", u"Categor\u00eda", None))
        self.catProSelText.setText("")
        self.labelVersion_31.setText(QCoreApplication.translate("stock", u"Foto", None))
        self.labelVersion_39.setText(QCoreApplication.translate("stock", u"Cantidad en Inventario", None))
        self.canProSelText.setText("")
        self.label_22.setText(QCoreApplication.translate("stock", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Lotes del Producto en Inventario</span></p></body></html>", None))
        ___qtablewidgetitem12 = self.invTable.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("stock", u"0", None));
        ___qtablewidgetitem13 = self.invTable.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("stock", u"1", None));
        ___qtablewidgetitem14 = self.invTable.verticalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("stock", u"New Row", None));
        ___qtablewidgetitem15 = self.invTable.verticalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("stock", u"Nueva fila", None));
        ___qtablewidgetitem16 = self.invTable.verticalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("stock", u"Nueva fila", None));
        ___qtablewidgetitem17 = self.invTable.verticalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("stock", u"New Row", None));
        ___qtablewidgetitem18 = self.invTable.verticalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("stock", u"New Row", None));
        ___qtablewidgetitem19 = self.invTable.verticalHeaderItem(5)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("stock", u"New Row", None));
        ___qtablewidgetitem20 = self.invTable.verticalHeaderItem(6)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("stock", u"New Row", None));
        ___qtablewidgetitem21 = self.invTable.verticalHeaderItem(7)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("stock", u"New Row", None));
        ___qtablewidgetitem22 = self.invTable.verticalHeaderItem(8)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("stock", u"New Row", None));
        ___qtablewidgetitem23 = self.invTable.verticalHeaderItem(9)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("stock", u"New Row", None));
        ___qtablewidgetitem24 = self.invTable.verticalHeaderItem(10)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("stock", u"New Row", None));
        ___qtablewidgetitem25 = self.invTable.verticalHeaderItem(11)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("stock", u"New Row", None));

        __sortingEnabled1 = self.invTable.isSortingEnabled()
        self.invTable.setSortingEnabled(False)
        ___qtablewidgetitem26 = self.invTable.item(0, 0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("stock", u"Producto", None));
        ___qtablewidgetitem27 = self.invTable.item(0, 1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("stock", u"Cantidad", None));
        self.invTable.setSortingEnabled(__sortingEnabled1)

        self.textCanStock.setText("")
        self.textCanLote.setText("")
        self.labelVersion_17.setText(QCoreApplication.translate("stock", u"Cantidad en Lote", None))
        self.labelVersion_16.setText(QCoreApplication.translate("stock", u"Cantidad en Stock", None))
        self.labelVersion_38.setText(QCoreApplication.translate("stock", u"Valor de venta actual", None))
        self.textCosLote.setText("")
        self.label_20.setText(QCoreApplication.translate("stock", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Transferir a Stock</span></p></body></html>", None))
        self.labelVersion_18.setText(QCoreApplication.translate("stock", u"Cantidad a Transferir", None))
        self.labelVersion_37.setText(QCoreApplication.translate("stock", u"Valor de Venta", None))
        self.textValVen.setText("")
        self.textValVen.setPlaceholderText(QCoreApplication.translate("stock", u"Ingrese el valor de venta", None))
        self.textCanTrans.setText("")
        self.textCanTrans.setPlaceholderText(QCoreApplication.translate("stock", u"Ingrese la cantidad a trasferir", None))
        self.ButtonTrans.setText(QCoreApplication.translate("stock", u"Transferir", None))
    # retranslateUi

