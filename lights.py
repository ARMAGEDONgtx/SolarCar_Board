from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QHBoxLayout

from PyQt5 import QtCore, QtGui, QtWidgets
from mytab import Tab


class LightsView(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.layout = QVBoxLayout(self)
        self.upperlay = QHBoxLayout(self)
        self.add_button = QtWidgets.QPushButton(self)
        self.spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.upperlay.addWidget(self.add_button)
        self.upperlay.addItem(self.spacer)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.homeTab = Tab(self)
        self.tabs.setTabsClosable(True)



        # Add tabs
        self.tabs.addTab(self.homeTab, '1')


        # Add tabs to widget
        self.layout.addLayout(self.upperlay)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


        #Signals
        self.tabs.tabCloseRequested.connect(self.closeMyTab)
        self.add_button.clicked.connect(self.addMyTab)
        QtCore.QMetaObject.connectSlotsByName(self)

    def closeMyTab(self, tab):
        self.tabs.removeTab(tab)

    def addMyTab(self):
        NewTab = Tab(self)
        self.tabs.addTab(NewTab,'ok')
