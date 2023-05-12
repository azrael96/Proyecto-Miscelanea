# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'productosJUbMzx.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_productos(object):
    def setupUi(self, productos):
        if not productos.objectName():
            productos.setObjectName(u"productos")
        productos.resize(1182, 608)
        self.verticalLayout_4 = QVBoxLayout(productos)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(productos)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_6.setFont(font)

        self.verticalLayout.addWidget(self.label_6)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout_3.addWidget(self.label_9)

        self.proTable = QTableWidget(self.frame_2)
        if (self.proTable.columnCount() < 1):
            self.proTable.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.proTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.proTable.rowCount() < 11):
            self.proTable.setRowCount(11)
        __qtablewidgetitem1 = QTableWidgetItem()
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
        self.proTable.setVerticalHeaderItem(10, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.proTable.setItem(0, 0, __qtablewidgetitem12)
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
        self.proTable.horizontalHeader().setDefaultSectionSize(120)
        self.proTable.horizontalHeader().setStretchLastSection(True)
        self.proTable.verticalHeader().setVisible(False)
        self.proTable.verticalHeader().setCascadingSectionResizes(False)
        self.proTable.verticalHeader().setHighlightSections(False)
        self.proTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_3.addWidget(self.proTable)


        self.horizontalLayout_8.addWidget(self.frame_2)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.proAddButton = QPushButton(self.frame_6)
        self.proAddButton.setObjectName(u"proAddButton")
        self.proAddButton.setMinimumSize(QSize(120, 30))
        self.proAddButton.setFont(font)
        self.proAddButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-check-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.proAddButton.setIcon(icon)

        self.verticalLayout_2.addWidget(self.proAddButton)

        self.proEditButton = QPushButton(self.frame_6)
        self.proEditButton.setObjectName(u"proEditButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.proEditButton.sizePolicy().hasHeightForWidth())
        self.proEditButton.setSizePolicy(sizePolicy1)
        self.proEditButton.setMinimumSize(QSize(120, 30))
        self.proEditButton.setFont(font)
        self.proEditButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.proEditButton.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.proEditButton)

        self.proDelButton = QPushButton(self.frame_6)
        self.proDelButton.setObjectName(u"proDelButton")
        self.proDelButton.setMinimumSize(QSize(120, 30))
        self.proDelButton.setFont(font)
        self.proDelButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.proDelButton.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.proDelButton)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)


        self.horizontalLayout_8.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_7)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_7)

        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout_17.addWidget(self.label_8)

        self.frame_8 = QFrame(self.frame_7)
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

        self.proCatCombo = QComboBox(self.frame_8)
        self.proCatCombo.setObjectName(u"proCatCombo")
        self.proCatCombo.setFont(font)
        self.proCatCombo.setAutoFillBackground(False)
        self.proCatCombo.setIconSize(QSize(16, 16))
        self.proCatCombo.setFrame(True)

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

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.proAddIMGButton = QPushButton(self.frame_4)
        self.proAddIMGButton.setObjectName(u"proAddIMGButton")
        self.proAddIMGButton.setMinimumSize(QSize(120, 30))
        self.proAddIMGButton.setFont(font)
        self.proAddIMGButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.proAddIMGButton.setIcon(icon)

        self.verticalLayout_5.addWidget(self.proAddIMGButton)

        self.proDelIMGButton = QPushButton(self.frame_4)
        self.proDelIMGButton.setObjectName(u"proDelIMGButton")
        self.proDelIMGButton.setMinimumSize(QSize(120, 30))
        self.proDelIMGButton.setFont(font)
        self.proDelIMGButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.proDelIMGButton.setIcon(icon2)

        self.verticalLayout_5.addWidget(self.proDelIMGButton)


        self.horizontalLayout.addWidget(self.frame_4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.frame_3)


        self.verticalLayout_17.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.proSaveButton = QPushButton(self.frame_9)
        self.proSaveButton.setObjectName(u"proSaveButton")
        self.proSaveButton.setMinimumSize(QSize(120, 30))
        self.proSaveButton.setFont(font)
        self.proSaveButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.proSaveButton.setIcon(icon)

        self.horizontalLayout_9.addWidget(self.proSaveButton)

        self.proCancelButton = QPushButton(self.frame_9)
        self.proCancelButton.setObjectName(u"proCancelButton")
        self.proCancelButton.setMinimumSize(QSize(120, 30))
        self.proCancelButton.setFont(font)
        self.proCancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.proCancelButton.setIcon(icon2)

        self.horizontalLayout_9.addWidget(self.proCancelButton)

        self.proClearButton = QPushButton(self.frame_9)
        self.proClearButton.setObjectName(u"proClearButton")
        self.proClearButton.setMinimumSize(QSize(120, 30))
        self.proClearButton.setFont(font)
        self.proClearButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-reload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.proClearButton.setIcon(icon3)

        self.horizontalLayout_9.addWidget(self.proClearButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)


        self.verticalLayout_17.addWidget(self.frame_9)

        self.verticalSpacer_8 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_8)


        self.horizontalLayout_8.addWidget(self.frame_7)


        self.verticalLayout.addWidget(self.frame_5)


        self.verticalLayout_4.addWidget(self.frame)


        self.retranslateUi(productos)

        self.proCatCombo.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(productos)
    # setupUi

    def retranslateUi(self, productos):
        productos.setWindowTitle(QCoreApplication.translate("productos", u"Form", None))
        self.label_6.setText(QCoreApplication.translate("productos", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Productos</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("productos", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Lista de Productos</span></p></body></html>", None))
        ___qtablewidgetitem = self.proTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("productos", u"0", None));
        ___qtablewidgetitem1 = self.proTable.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("productos", u"New Row", None));
        ___qtablewidgetitem2 = self.proTable.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("productos", u"New Row", None));
        ___qtablewidgetitem3 = self.proTable.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("productos", u"New Row", None));
        ___qtablewidgetitem4 = self.proTable.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("productos", u"New Row", None));
        ___qtablewidgetitem5 = self.proTable.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("productos", u"New Row", None));
        ___qtablewidgetitem6 = self.proTable.verticalHeaderItem(5)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("productos", u"New Row", None));
        ___qtablewidgetitem7 = self.proTable.verticalHeaderItem(6)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("productos", u"New Row", None));
        ___qtablewidgetitem8 = self.proTable.verticalHeaderItem(7)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("productos", u"New Row", None));
        ___qtablewidgetitem9 = self.proTable.verticalHeaderItem(8)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("productos", u"New Row", None));
        ___qtablewidgetitem10 = self.proTable.verticalHeaderItem(9)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("productos", u"New Row", None));
        ___qtablewidgetitem11 = self.proTable.verticalHeaderItem(10)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("productos", u"New Row", None));

        __sortingEnabled = self.proTable.isSortingEnabled()
        self.proTable.setSortingEnabled(False)
        ___qtablewidgetitem12 = self.proTable.item(0, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("productos", u"Nombre ", None));
        self.proTable.setSortingEnabled(__sortingEnabled)

        self.proAddButton.setText(QCoreApplication.translate("productos", u"Agregar", None))
        self.proEditButton.setText(QCoreApplication.translate("productos", u"Editar", None))
        self.proDelButton.setText(QCoreApplication.translate("productos", u"Eliminar", None))
        self.label_8.setText(QCoreApplication.translate("productos", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Producto Seleccionado</span></p></body></html>", None))
        self.labelVersion_47.setText(QCoreApplication.translate("productos", u"Nombre Producto", None))
        self.proNomText.setText("")
        self.proNomText.setPlaceholderText(QCoreApplication.translate("productos", u"Ingrese el nombre del producto", None))
        self.labelVersion_50.setText(QCoreApplication.translate("productos", u"Categor\u00eda", None))
        self.proCatCombo.setPlaceholderText(QCoreApplication.translate("productos", u"Seleccione una opci\u00f3n", None))
        self.labelVersion_48.setText(QCoreApplication.translate("productos", u"Descripci\u00f3n", None))
        self.proDesText.setText("")
        self.proDesText.setPlaceholderText(QCoreApplication.translate("productos", u"Ingrese la descripci\u00f3n del producto", None))
        self.labelVersion_49.setText(QCoreApplication.translate("productos", u"Foto", None))
        self.proAddIMGButton.setText(QCoreApplication.translate("productos", u"Agregar", None))
        self.proDelIMGButton.setText(QCoreApplication.translate("productos", u"Eliminar", None))
        self.proSaveButton.setText(QCoreApplication.translate("productos", u"Confirmar", None))
        self.proCancelButton.setText(QCoreApplication.translate("productos", u"Cancelar", None))
        self.proClearButton.setText(QCoreApplication.translate("productos", u"Limpiar", None))
    # retranslateUi

