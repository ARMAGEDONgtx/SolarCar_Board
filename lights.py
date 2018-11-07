from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QHBoxLayout
from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from plotter import PlotCanvas
import mycalendar
import PyQt5.QtWidgets as wgt
from PyQt5 import QtCore

class LightsView(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.setObjectName("LightView")
        self.layout = QVBoxLayout(self)
        #self.pushButton = QPushButton("Test")
        #self.layout.addWidget(self.pushButton)
        self.graph = PlotCanvas(self, width=5, height=4)
        self.layout.addWidget(self.graph)
        self.toolbar = NavigationToolbar(self.graph, parent)
        self.layout.addWidget(self.toolbar)
        ################################   BUTTONS ETC.     ##################################################
        self.button_start = wgt.QPushButton(self)
        self.button_start.setObjectName("button_start")
        self.button_start.setText("Start")
        self.button_stop = wgt.QPushButton(self)
        self.button_stop.setObjectName("button_stop")
        self.button_stop.setText( "Stop")
        self.button_cal = wgt.QPushButton(self)
        self.button_cal.setObjectName("button_cal")
        self.button_cal.setText("calendar")
        self.slider_time = wgt.QSlider(QtCore.Qt.Horizontal)
        self.slider_time.setObjectName("slider_time")
        self.slider_time.setMinimum(1)
        self.slider_time.setMaximum(20)
        self.layout2 = QHBoxLayout(self)
        self.layout2.addWidget(self.button_start)
        self.layout2.addWidget(self.slider_time)
        self.layout2.addWidget(self.button_stop)
        self.layout2.addWidget(self.button_cal)
        self.layout.addLayout(self.layout2)
        self.cal = mycalendar.calendar()
        self.cal.setupUi()
        ###################  SIGNALS AND SLOTS  #############################################################
        self.slider_time.setValue(self.graph.pomiar1.frequency)
        self.button_start.clicked.connect(self.graph.start_thread)
        self.graph.pomiar1.new_data.connect(self.handle_new_data)
        self.button_stop.clicked.connect(self.graph.pause_thread)
        self.slider_time.valueChanged.connect(self.handle_slider)
        self.button_cal.clicked.connect(self.show_calendar)
        self.cal.plot_on_close.connect(self.graph.data_btwn_dates)
        QtCore.QMetaObject.connectSlotsByName(self)


    def handle_new_data(self, time, val):
        pass
        try:
            self.graph.plot(time, val)
            self.graph.set_xlimits(self.pom1.first_update, self.pom1.last_update)
        except Exception as e:
            print(e)


    def handle_slider(self):
        self.graph.pomiar1.frequency = self.slider_time.value()

    def show_calendar(self):
        self.cal.show()
