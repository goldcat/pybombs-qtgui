# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/gui_pybombs.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(652, 464)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(634, 353))
        self.tableWidget.setBaseSize(QtCore.QSize(640, 480))
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.verticalLayout.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 652, 28))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuActions = QtWidgets.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        self.toolBar.setStyleSheet("")
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_About_GNU_Radio = QtWidgets.QAction(MainWindow)
        self.action_About_GNU_Radio.setObjectName("action_About_GNU_Radio")
        self.action_About_CGRAN = QtWidgets.QAction(MainWindow)
        self.action_About_CGRAN.setObjectName("action_About_CGRAN")
        self.action_Apply = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/noprefix/images/apply.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Apply.setIcon(icon)
        font = QtGui.QFont()
        self.action_Apply.setFont(font)
        self.action_Apply.setIconVisibleInMenu(False)
        self.action_Apply.setObjectName("action_Apply")
        self.action_Mark_All_Updates = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/noprefix/images/mark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Mark_All_Updates.setIcon(icon1)
        self.action_Mark_All_Updates.setIconVisibleInMenu(False)
        self.action_Mark_All_Updates.setObjectName("action_Mark_All_Updates")
        self.action_Refresh = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/noprefix/images/refresh_list.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Refresh.setIcon(icon2)
        self.action_Refresh.setIconVisibleInMenu(False)
        self.action_Refresh.setObjectName("action_Refresh")
        self.action_Properties = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/noprefix/images/dev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Properties.setIcon(icon3)
        self.action_Properties.setIconVisibleInMenu(False)
        self.action_Properties.setObjectName("action_Properties")
        self.action_Search = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/noprefix/images/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Search.setIcon(icon4)
        self.action_Search.setIconVisibleInMenu(False)
        self.action_Search.setObjectName("action_Search")
        self.actionConfig_Preferences = QtWidgets.QAction(MainWindow)
        self.actionConfig_Preferences.setObjectName("actionConfig_Preferences")
        self.action_Preferences = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/noprefix/images/prefs.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Preferences.setIcon(icon5)
        self.action_Preferences.setIconVisibleInMenu(False)
        self.action_Preferences.setObjectName("action_Preferences")
        self.action_RunningConfig = QtWidgets.QAction(MainWindow)
        self.action_RunningConfig.setObjectName("action_RunningConfig")
        self.action_About_PyBOMBS = QtWidgets.QAction(MainWindow)
        self.action_About_PyBOMBS.setObjectName("action_About_PyBOMBS")
        self.menuFile.addAction(self.action_Preferences)
        self.menuFile.addAction(self.action_RunningConfig)
        self.menuActions.addSeparator()
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.action_Apply)
        self.menuActions.addAction(self.action_Mark_All_Updates)
        self.menuActions.addAction(self.action_Refresh)
        self.menuActions.addSeparator()
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.action_Properties)
        self.menuActions.addSeparator()
        self.menuActions.addAction(self.action_Search)
        self.menuHelp.addAction(self.action_About_PyBOMBS)
        self.menuHelp.addAction(self.action_About_GNU_Radio)
        self.menuHelp.addSeparator()
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.action_About_CGRAN)
        self.menuHelp.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.action_Apply)
        self.toolBar.addAction(self.action_Mark_All_Updates)
        self.toolBar.addAction(self.action_Refresh)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Properties)
        self.toolBar.addAction(self.action_Preferences)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Search)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Category"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Description"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Repository"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Status"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuActions.setTitle(_translate("MainWindow", "Actions"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_About_GNU_Radio.setText(_translate("MainWindow", "&About GNU Radio"))
        self.action_About_CGRAN.setText(_translate("MainWindow", "&About CGRAN"))
        self.action_Apply.setText(_translate("MainWindow", "&Apply Changes"))
        self.action_Mark_All_Updates.setText(_translate("MainWindow", "&Mark All Updates"))
        self.action_Refresh.setText(_translate("MainWindow", "&Refresh List"))
        self.action_Properties.setText(_translate("MainWindow", "&Module Info"))
        self.action_Search.setText(_translate("MainWindow", "&Search"))
        self.action_Search.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionConfig_Preferences.setText(_translate("MainWindow", "&Config Preferences"))
        self.action_Preferences.setText(_translate("MainWindow", "&Preferences"))
        self.action_RunningConfig.setText(_translate("MainWindow", "&Running Config"))
        self.action_About_PyBOMBS.setText(_translate("MainWindow", "&About PyBOMBS"))

import myicons_rc
