# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/module_info.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ModuleInfoDialog(object):
    def setupUi(self, ModuleInfoDialog):
        ModuleInfoDialog.setObjectName("ModuleInfoDialog")
        ModuleInfoDialog.resize(445, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ModuleInfoDialog.sizePolicy().hasHeightForWidth())
        ModuleInfoDialog.setSizePolicy(sizePolicy)
        ModuleInfoDialog.setFocusPolicy(QtCore.Qt.NoFocus)
        self.verticalLayout = QtWidgets.QVBoxLayout(ModuleInfoDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(ModuleInfoDialog)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QTabBar::tab{\n"
"  min-width: 10ex;\n"
"  padding: 2px;\n"
"  margin-right: 20px;\n"
"  margin-left: 10px;\n"
"  padding-right: 20px;\n"
"  padding-left: 20px;\n"
"  padding-top: -4px;\n"
"  focus{border:none;}\n"
"}\n"
"QTabBar::tab:selected {\n"
"  border-bottom : 2.3px solid;\n"
"  border-bottom-color: rgb(69, 140, 214);\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"  border-bottom: 2.3px solid; /* make non-selected tabs look smaller */\n"
"  border-bottom-color: rgb(135, 135, 134);   \n"
"}\n"
"\n"
"QTabBar:tab:focus {\n"
"  outline: none;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.textEdit.setStyleSheet("")
        self.textEdit.setTabChangesFocus(True)
        self.textEdit.setReadOnly(True)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.label = QtWidgets.QLabel(ModuleInfoDialog)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/noprefix/images/protip.png"))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(ModuleInfoDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ModuleInfoDialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(ModuleInfoDialog.accept)
        self.buttonBox.rejected.connect(ModuleInfoDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ModuleInfoDialog)

    def retranslateUi(self, ModuleInfoDialog):
        _translate = QtCore.QCoreApplication.translate
        ModuleInfoDialog.setWindowTitle(_translate("ModuleInfoDialog", "Module Info"))
        self.textEdit.setHtml(_translate("ModuleInfoDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ModuleInfoDialog", "Module Info"))

import myicons_rc