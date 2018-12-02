from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QHBoxLayout

from PyQt5 import QtCore, QtGui, QtWidgets
from mywidgets.mytab import Tab

class InvertersView(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.counter = 1
        self.layout = QVBoxLayout(self)
        self.upperlay = QHBoxLayout(self)

        # Add button
        self.add_button = QtWidgets.QPushButton(self)
        self.add_button.setText("")
        self.add_button.setIcon(QtGui.QIcon("other/add.png"))
        self.add_button.setIconSize(QtCore.QSize(30, 20))
        self.add_button.setFlat(True)
        self.add_button.setFocusPolicy(QtCore.Qt.NoFocus)

        self.spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.upperlay.addWidget(self.add_button)
        self.upperlay.addItem(self.spacer)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.homeTab = Tab(self,2)
        self.tabs.setTabsClosable(True)

        # Add tabs
        self.tabs.addTab(self.homeTab, '1')

        # Add tabs to widget
        self.layout.addLayout(self.upperlay)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        # Signals
        self.tabs.tabCloseRequested.connect(self.closeMyTab)
        self.add_button.clicked.connect(self.addMyTab)
        QtCore.QMetaObject.connectSlotsByName(self)


        # fucntion called to delete tab

    def closeMyTab(self, tab):
        self.tabs.currentWidget().handleClose()
        self.tabs.removeTab(tab)
        self.counter = self.counter - 1

        # fucntion called to add new tab

    def addMyTab(self):
        NewTab = Tab(self,2)
        self.counter = self.counter + 1
        self.tabs.addTab(NewTab, str(self.counter))

        # function called when app is about to close, threads closing

    def exitHandler(self):
        for x in range(self.tabs.count()):
            try:
                self.tabs.widget(x).handleClose()
            except Exception as e:
                print(str(e))