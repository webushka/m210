# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created: Wed Aug 25 00:25:56 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(544, 275)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setCheckable(True)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.comboBoxMode = QtGui.QComboBox(self.groupBox)
        self.comboBoxMode.setObjectName("comboBoxMode")
        self.comboBoxMode.addItem("")
        self.comboBoxMode.addItem("")
        self.gridLayout.addWidget(self.comboBoxMode, 3, 1, 1, 1)
        self.pushButtonErase = QtGui.QPushButton(self.groupBox)
        self.pushButtonErase.setEnabled(False)
        self.pushButtonErase.setObjectName("pushButtonErase")
        self.gridLayout.addWidget(self.pushButtonErase, 5, 0, 1, 1)
        self.pushButtonDownload = QtGui.QPushButton(self.groupBox)
        self.pushButtonDownload.setEnabled(False)
        self.pushButtonDownload.setObjectName("pushButtonDownload")
        self.gridLayout.addWidget(self.pushButtonDownload, 5, 1, 1, 1)
        self.spinBoxUsedMemory = QtGui.QSpinBox(self.groupBox)
        self.spinBoxUsedMemory.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinBoxUsedMemory.setReadOnly(True)
        self.spinBoxUsedMemory.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBoxUsedMemory.setPrefix("")
        self.spinBoxUsedMemory.setMaximum(999999999)
        self.spinBoxUsedMemory.setObjectName("spinBoxUsedMemory")
        self.gridLayout.addWidget(self.spinBoxUsedMemory, 4, 1, 1, 1)
        self.spinBoxPadVersion = QtGui.QSpinBox(self.groupBox)
        self.spinBoxPadVersion.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinBoxPadVersion.setReadOnly(True)
        self.spinBoxPadVersion.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBoxPadVersion.setMaximum(65535)
        self.spinBoxPadVersion.setObjectName("spinBoxPadVersion")
        self.gridLayout.addWidget(self.spinBoxPadVersion, 2, 1, 1, 1)
        self.spinBoxAnalogVersion = QtGui.QSpinBox(self.groupBox)
        self.spinBoxAnalogVersion.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinBoxAnalogVersion.setReadOnly(True)
        self.spinBoxAnalogVersion.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBoxAnalogVersion.setMaximum(65535)
        self.spinBoxAnalogVersion.setObjectName("spinBoxAnalogVersion")
        self.gridLayout.addWidget(self.spinBoxAnalogVersion, 1, 1, 1, 1)
        self.spinBoxFirmwareVersion = QtGui.QSpinBox(self.groupBox)
        self.spinBoxFirmwareVersion.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinBoxFirmwareVersion.setReadOnly(True)
        self.spinBoxFirmwareVersion.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.spinBoxFirmwareVersion.setMaximum(65535)
        self.spinBoxFirmwareVersion.setObjectName("spinBoxFirmwareVersion")
        self.gridLayout.addWidget(self.spinBoxFirmwareVersion, 0, 1, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 544, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "M210", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Connected", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Used memory:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Analog version:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Mode:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Firmware version:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Pad version:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxMode.setItemText(0, QtGui.QApplication.translate("MainWindow", "MOUSE", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxMode.setItemText(1, QtGui.QApplication.translate("MainWindow", "TABLE", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonErase.setText(QtGui.QApplication.translate("MainWindow", "Erase", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDownload.setText(QtGui.QApplication.translate("MainWindow", "Download...", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBoxUsedMemory.setSuffix(QtGui.QApplication.translate("MainWindow", "B", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))

