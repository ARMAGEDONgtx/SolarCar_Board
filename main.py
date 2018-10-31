import sys
import matplotlib

matplotlib.use("Qt5Agg", warn = False, force = True)

from home import HomeView
from lights import LightsView
from inverters import InvertersView
from battery import BatteryView
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'SolarCar'
        self.left = 0
        self.top = 0
        self.width = 800
        self.height = 1280
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.mainWidget = TabView(self)
        self.setCentralWidget(self.mainWidget)

        self.setStyleSheet("""
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
        """)

        #self.showFullScreen()
        self.show()

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
        self.tabs.addTab(self.homeTab, 'Home')
        self.tabs.addTab(self.lightsTab, 'Lights')
        self.tabs.addTab(self.invertersTab, 'Inverter')
        self.tabs.addTab(self.batteryTab, 'Battery')

        #Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())