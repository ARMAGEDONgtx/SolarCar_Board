from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from matplotlib.figure import Figure

import matplotlib.pyplot as plt

from PyQt5 import QtWidgets

import matplotlib

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
