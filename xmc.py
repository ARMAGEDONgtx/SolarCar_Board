import urllib.request

import re

import PyQt5

import datetime

import time



# helpful class for managing data from xmc controlers and plots


class pomiar(PyQt5.QtCore.QObject):


    new_data = PyQt5.QtCore.pyqtSignal(int)

    def __init__(self, probe=1, limit=100):
        PyQt5.QtCore.QObject.__init__(self)
        self.frequency = probe
        self.max_probes = limit
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        self.last_update = timestamp
        self.xs = []
        self.ys = []
        # signal


    def change_param(self, probe=1, limit=100):
        self.frequency = probe
        self.max_probes = limit


    def get_data(self):
        req = urllib.request.urlopen("http://192.168.0.10").read()
        result = re.findall(r'\d+', req.decode("utf-8"))
        self.new_data.emit(int(result[0]))
