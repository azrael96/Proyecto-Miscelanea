# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reportesjlYqvh.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_reportes(object):
    def setupUi(self, reportes):
        if not reportes.objectName():
            reportes.setObjectName(u"reportes")
        reportes.resize(1182, 608)
        reportes.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(reportes)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(reportes)
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
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.label_4)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(reportes)

        QMetaObject.connectSlotsByName(reportes)
    # setupUi

    def retranslateUi(self, reportes):
        reportes.setWindowTitle(QCoreApplication.translate("reportes", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("reportes", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Reportes</span></p></body></html>", None))
    # retranslateUi

