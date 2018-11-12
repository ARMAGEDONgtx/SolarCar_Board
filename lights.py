from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QHBoxLayout
from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from plotter import PlotCanvas
import mycalendar
import plot_controller
import PyQt5.QtWidgets as wgt
from PyQt5 import QtCore, QtGui, QtWidgets



class LightsView(QWidget):
    def __init__(self, parent):

        super(QWidget, self).__init__(parent)
        self.setObjectName("LightView")
        self.layoutmain = QHBoxLayout(self)
        self.layoutmain.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.layout = QVBoxLayout(self)
        self.graph = PlotCanvas(self, width=8, height=6)
        self.layout.addWidget(self.graph)
        self.toolbar = NavigationToolbar(self.graph, parent)
        self.layout.addWidget(self.toolbar)


        ################################   BUTTONS ETC.     ##################################################


        ##### CONTROLER SETUP #####################################################
        self.controler = plot_controller.controller()
        self.controler.setupUi()
        self.controler.bind_thread(self.graph.thread1)


        ##### LAYOUT MANAGMENT   ##################################################
        self.layoutmain.addLayout(self.layout)
        self.layout_controler = QVBoxLayout(self)
        self.layout_controler.addWidget(self.controler)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.layout_controler.addItem(spacerItem)
        self.layoutmain.addLayout(self.layout_controler)
        self.setLayout(self.layoutmain)


        ###################  SIGNALS AND SLOTS  #############################################################
        self.controler.pushButton_init.clicked.connect(self.graph.start_thread)
        self.graph.pomiar1.new_data.connect(self.handle_new_data)
        self.controler.pushButton_stop.clicked.connect(self.graph.stop_thread)
        self.controler.cal.plot_on_close.connect(self.graph.data_btwn_dates)
        QtCore.QMetaObject.connectSlotsByName(self)

    # function called when new data appears
    def handle_new_data(self, value):
        try:
            self.graph.pomiar1.last_value = value
            self.graph.pomiar1.update()
            self.controler.display_parameters(self.graph.pomiar1.average, self.graph.pomiar1.minimum, self.graph.pomiar1.maximum , self.graph.pomiar1.last_value)
        except Exception as e:
            print(e)




