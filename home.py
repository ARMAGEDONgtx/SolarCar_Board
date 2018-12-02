#Start window

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QLabel, QGridLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore, QtGui

class HomeView(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QGridLayout(self)
        self.setObjectName("home_tab")
        pic = QLabel(self)
        pix = QtGui.QPixmap("other/put_logo.png")
        pic.setPixmap(pix.scaledToHeight(400))
        pic.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(pic)
        self.setLayout(self.layout)