import urllib.request
import re
import PyQt5
import datetime
import time
import mythread
import sql_functions as sql

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
        self.thread1 = mythread.StoppableThread(target=self.generate_random_data)
        # signal

    #change parmameters of measeurment
    def change_param(self, probe=1, limit=100):
        self.frequency = probe
        self.max_probes = limit
        print(self.frequency)

    #http get request to xmc controler
    def get_data(self):
        req = urllib.request.urlopen("http://192.168.0.10").read()
        result = re.findall(r'\d+', req.decode("utf-8"))
        self.new_data.emit(int(result[0]))

    #generate random data and put it into mysql database
    def generate_random_data(self):
        conn = None
        try:
            conn = sql.connect_to_sql()
            while True:
                if self.thread1.stopped() == True:
                    break
                if self.thread1.paused() == False:
                    sql.put_random_data_SQL(conn)
                    time.sleep(self.frequency)
        except Exception as e:
            print(e)
        finally:
            if conn is not None:
                conn.close()