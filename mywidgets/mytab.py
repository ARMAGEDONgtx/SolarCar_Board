from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QHBoxLayout
from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from mywidgets.plotter import PlotCanvas
import mywidgets.plot_controller
from PyQt5 import QtCore, QtGui, QtWidgets
from xmc import pomiar


class Tab(QWidget):
    def __init__(self, parent, mes_id):
        self.own_measure = pomiar()

        super(QWidget, self).__init__(parent)
        self.setObjectName("LightView")
        self.layoutmain = QHBoxLayout(self)
        self.layoutmain.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.layout = QVBoxLayout(self)
        self.graph = PlotCanvas(self.own_measure, self , width=8, height=6)
        self.layout.addWidget(self.graph)
        self.toolbar = NavigationToolbar(self.graph, parent)
        self.layout.addWidget(self.toolbar)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        ################################   BUTTONS ETC.     ##################################################


        ##### CONTROLER SETUP #####################################################
        self.controler = mywidgets.plot_controller.controller()
        self.controler.setupUi(self.own_measure,mes_id)
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
        self.controler.pushButton_init.clicked.connect(self.start_live)
        self.controler.controled_measure.new_data.connect(self.handle_new_data)
        self.controler.pushButton_stop.clicked.connect(self.graph.stop_thread)
        self.controler.cal.plot_on_close.connect(self.graph.data_btwn_dates)
        QtCore.QMetaObject.connectSlotsByName(self)

    # function called when new data appears
    def handle_new_data(self, value):
        try:
            self.controler.controled_measure.last_value = value
            self.controler.controled_measure.update()
            self.controler.display_parameters(self.controler.controled_measure.average, self.controler.controled_measure.minimum, self.controler.controled_measure.maximum , self.controler.controled_measure.last_value)
        except Exception as e:
            print(e)

    #function called when tabs is about to close
    def handleClose(self):
        self.controler.handle_stop()

    def start_live(self):
        self.graph.start_thread()
        self.controler.live_status()




