import sys
import matplotlib


matplotlib.use("Qt5Agg", warn = False, force = True)

from home import HomeView
from lights import LightsView
from inverters import InvertersView
from battery import BatteryView
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import qdarkstyle

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'SolarCar'
        self.left = 0
        self.top = 0
        #self.width = 1000
        #self.height = 1280
        self.setWindowTitle(self.title)
        #self.setGeometry(self.left, self.top, self.width, self.height)

        self.mainWidget = TabView(self)
        self.setCentralWidget(self.mainWidget)



        self.tmp = """
            QTabBar::tab {
                background: lightgray;
                color: black;
                border: 0;
                width: 60px;
                height: 50px;
                padding: 5px;
            }

            QTabBar::tab:selected {
                background: gray;
                color: white;
            }
        """

        #self.showFullScreen()
        self.show()

    def closeEvent(self, QCloseEvent):
        self.mainWidget.lightsTab.exitHandler()
        super(QMainWindow,self).closeEvent(QCloseEvent)



class TabView(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        #Initialize tab screen
        self.tabs = QTabWidget()
        self.homeTab = HomeView(self)
        self.lightsTab = LightsView(self)
        self.invertersTab = InvertersView(self)
        self.batteryTab = BatteryView(self)

        #Add tabs
        self.tabs.addTab(self.homeTab,  QtGui.QIcon("other/home.png"), '')
        self.tabs.addTab(self.lightsTab, QtGui.QIcon("other/light.png"),'')
        self.tabs.addTab(self.invertersTab,QtGui.QIcon("other/engine.png"), '')
        self.tabs.addTab(self.batteryTab, QtGui.QIcon("other/battery.png"),'')

        self.tabs.setIconSize(QtCore.QSize(40,40))


        #Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    sys.exit(app.exec_())