from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QHBoxLayout
from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from plotter import PlotCanvas

import PyQt5.QtWidgets as wgt
import threading as th
from xmc import pomiar
from PyQt5 import QtCore
import sql_functions as sql
import time

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
        self.slider_time = wgt.QSlider(QtCore.Qt.Horizontal)
        self.slider_time.setObjectName("slider_time")
        self.slider_time.setMinimum(1)
        self.slider_time.setMaximum(20)
        self.layout2 = QHBoxLayout(self)
        self.layout2.addWidget(self.button_start)
        self.layout2.addWidget(self.slider_time)
        self.layout2.addWidget(self.button_stop)
        self.layout.addLayout(self.layout2)
        ###################   THREAD FOR GENERATING DATA #####################################################
        self.my_thread = th.Thread(target=self.cyclic_data)
        self.my_thread.daemon = True
        self.pause = False
        self.my_thread2 = th.Thread(target=self.live_data)
        ###################  SIGNALS AND SLOTS  #############################################################
        self.pom1 = pomiar(5)
        self.slider_time.setValue(self.pom1.frequency)
        self.button_start.clicked.connect(self.start_thread)
        self.pom1.new_data.connect(self.handle_new_data)
        self.button_stop.clicked.connect(self.pause_thread)
        QtCore.QMetaObject.connectSlotsByName(self)


    def handle_new_data(self, time, val):
        #self.text_pomiary.appendPlainText(str(val))
        try:
            self.graph.plot(time, val)
            self.graph.set_xlimits(self.pom1.first_update, self.pom1.last_update)
        except Exception as e:
            print(e)


    def cyclic_data(self):
        #self.text_pomiary.appendPlainText("wystartowalem watek")
        conn = None
        try:
            conn = sql.connect_to_sql()
            while True:
                if self.pause == False:
                    sql.put_random_data_SQL(conn)
                    time.sleep(self.pom1.frequency)
        except Exception as e:
            print(e)
        finally:
            if conn is not None:
                conn.close()


    def live_data(self):
        conn = None
        try:
            while True:
                if self.pause == False :
                    conn = sql.connect_to_sql()
                    last_row = sql.check_last_row(conn, self.pom1.last_update)
                    print(last_row)
                    if last_row[0] == False:
                        self.pom1.xs.append(last_row[1])
                        self.pom1.ys.append(last_row[2])
                        self.graph.anim( self.pom1.ys, self.pom1.xs )
                        #self.handle_new_data(last_row[2],last_row[1])
                        self.pom1.last_update = last_row[2]
                    conn.close()
                    time.sleep(1)

        except Exception as e:
            print(e)
        finally:
            if conn is not None:
                conn.close()


    def data_btwn_dates(self):
        conn = None
        try:
            start_dt = QtCore.QDateTime(self.m_calendar.start_date(),self.m_calendar.start_time()).toPyDateTime()
            end_dt = QtCore.QDateTime(self.m_calendar.end_date(),self.m_calendar.end_time()).toPyDateTime()
            #print(type(start_dt))
            #print(type(end_dt))
            conn = sql.connect_to_sql()
            dat = sql.logs_btwn_dates(conn,start_dt,end_dt)
            self.graph.ax.clear()
            self.graph.setup()
            self.graph.set_xlimits(start_dt, end_dt)
            th.Thread(target=self.plot_thread, args=(dat,)).start()
            conn.close()
        except Exception as e:
            print(e)
        finally:
            if conn is not None:
                conn.close()


    def plot_thread(self,dat):
        tmp = False
        if dat is not None:
            for x in dat:
                self.graph.plot(x[0], x[1])
                if tmp is False:
                    self.graph.draw_legend()
                    tmp = True


    def start_thread(self):
        self.pause = False
        try:
            self.my_thread.start()
            self.my_thread2.start()
        except Exception as e:
            self.text_pomiary.appendPlainText(str(e))

    def pause_thread(self):
        self.pause = True


    def handle_slider(self):
        self.pom1.frequency = self.slider_time.value()