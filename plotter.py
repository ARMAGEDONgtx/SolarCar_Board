from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
import matplotlib
import sql_functions as sql
import time
import mythread
import xmc
from PyQt5 import QtCore
import threading as th

matplotlib.use("Qt5Agg", warn = False, force = True)

class PlotCanvas(FigureCanvas):


    def __init__(self, parent=None, width=5, height=4, dpi=100):
        plt.xticks(rotation=90)
        plt.style.use('seaborn-pastel')
        plt.rcParams['font.family'] = 'serif'
        plt.rcParams['font.serif'] = 'Ubuntu'
        plt.rcParams['font.monospace'] = 'Ubuntu Mono'
        plt.rcParams['font.size'] = 14
        plt.rcParams['axes.labelsize'] = 12
        plt.rcParams['axes.labelweight'] = 'bold'
        plt.rcParams['axes.titlesize'] = 16
        plt.rcParams['xtick.labelsize'] = 8
        plt.rcParams['ytick.labelsize'] = 8
        plt.rcParams['legend.fontsize'] = 10
        plt.rcParams['figure.titlesize'] = 12
        # adjust plot to the whole ares #
        plt.rcParams['figure.autolayout'] = True
        # wybor ksztaltu punktu
        plt.rcParams['scatter.marker'] = 'v'
        # frame parameters #
        plt.rcParams['figure.edgecolor'] = 'b'
        plt.xlabel('time')
        plt.ylabel('value')
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.autofmt_xdate()
        # background color #
        fig.patch.set_facecolor('lightgray')
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.setup()
        # ADD LOGO TO THE PLOT #
        logo = plt.imread('/home/wroblem/projects/my_solar/solar_napis.png')
        self.ax.figure.figimage(logo, 80, 70, alpha=.1, zorder=1)
        ###################   THREAD FOR GENERATING DATA #####################################################
        self.thread1 = mythread.StoppableThread(target=self.live_data)
        ######################################################################################################
        self.pomiar1 = xmc.pomiar(5)

    #### setting up  some parameters of plots ###########
    def setup(self):
        # setting up axes
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title('Time over value', fontstyle='italic', loc='left', fontsize=20, color='orange')
        self.ax.set_title('PUT Solar Dynamics', loc='right', fontsize=12, color='grey', fontstyle='italic')
        self.ax.set_ylabel('Value[%]', fontstyle='italic')
        self.ax.set_xlabel('Time[date]', fontstyle='italic')
        self.ax.grid(color='black', linestyle='--', linewidth=0.5, alpha=0.5)
        # plot color
        self.ax.set_facecolor('xkcd:baby blue')
        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    #### scatter some date ###########################
    def plot(self, value_x, value_y):
        self.ax.scatter(value_x, value_y, label='wykres', alpha=0.6, edgecolors='black')
        self.draw()

    #### function for live ploting ####################
    def anim(self, xs, ys):
        # Limit x and y lists to 20 items
        xs = xs[-20:]
        ys = ys[-20:]
        # Draw x and y lists
        self.ax.clear()
        self.setup()
        self.ax.plot(xs, ys, label = 'wykres', c = 'orchid')
        self.draw_legend()
        self.ax.tick_params(axis='x', rotation=45)
        self.draw()
        # Format plot


    def draw_legend(self):
        self.ax.legend(numpoints=1, fancybox=True, shadow='True', borderpad=1)


    def set_xlimits(self,lower,upper):
        self.ax.set_xlim([lower,upper])


    #live plot from database based on time
    #we store time of the last probe and if we find
    #data with later timer we plot it on the graph
    def live_data(self):
        conn = None
        try:
            while True:
                if self.thread1.stopped() == True:
                    break
                if self.thread1.paused() == False :
                    conn = sql.connect_to_sql()
                    last_row = sql.check_last_row(conn, self.pomiar1.last_update)
                    print(last_row)
                    if last_row[0] == False:
                        self.pomiar1.xs.append(last_row[1])
                        self.pomiar1.ys.append(last_row[2])
                        self.anim(self.pomiar1.ys, self.pomiar1.xs)
                        #self.handle_new_data(last_row[2],last_row[1])
                        self.pomiar1.last_update = last_row[2]
                        self.pomiar1.new_data.emit(last_row[1])
                    conn.close()
                    time.sleep(1)
        except Exception as e:
            print(e)
        finally:
            if conn is not None:
                conn.close()

    #plot all data that is beetween selected dates
    def data_btwn_dates(self, start_dt, end_dt):
        conn = None
        try:
            #start_dt = QtCore.QDateTime(self.m_calendar.start_date(),self.m_calendar.start_time()).toPyDateTime()
            #end_dt = QtCore.QDateTime(self.m_calendar.end_date(),self.m_calendar.end_time()).toPyDateTime()
            #print(type(start_dt))
            #print(type(end_dt))
            conn = sql.connect_to_sql()
            dat = sql.logs_btwn_dates(conn,start_dt,end_dt)
            self.ax.clear()
            self.setup()
            self.set_xlimits(start_dt, end_dt)
            th.Thread(target=self.plot_in_thread, args=(dat,)).start()
            conn.close()
        except Exception as e:
            print(e)
        finally:
            if conn is not None:
                conn.close()

    #function used in thread to plot big amoant of data in another thread
    def plot_in_thread(self, dat):
        tmp = False
        if dat is not None:
            for x in dat:
                self.plot(x[0], x[1])
                if tmp is False:
                    self.draw_legend()
                    tmp = True


    def start_thread(self):
        try:
            self.thread1.start()
            self.pomiar1.thread1.start()
        except Exception as e:
            print(str(e))

    def pause_thread(self):
        try:
            if self.thread1.paused() == True and self.pomiar1.thread1.paused() == True:
                self.thread1.unpause()
                self.pomiar1.thread1.unpause()
            else:
                self.thread1.pause()
                self.pomiar1.thread1.pause()
        except Exception as e:
            print(str(e))

    def stop_thread(self):
        try:
            self.thread1.stop()
            self.pomiar1.thread1.stop()
        except Exception as e:
            print(str(e))