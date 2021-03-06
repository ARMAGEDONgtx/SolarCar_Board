import urllib.request
import re
import PyQt5
import datetime
import time
import mythread
import sql_functions as sql

# class for managing data from xmc controlers and plots


class pomiar(PyQt5.QtCore.QObject):


    new_data = PyQt5.QtCore.pyqtSignal(int)

    def __init__(self, probe=5, limit=100):
        PyQt5.QtCore.QObject.__init__(self)
        self.frequency = probe
        self.max_probes = limit
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        self.last_update = timestamp
        self.xs = []
        self.ys = []
        self.average = 0
        self.av = []
        self.minimum = 0
        self.maximum = 0
        self.last_value = 0
        self.measurment_id = None
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
                    if self.measurment_id is not None:
                        sql.put_random_json_SQL(conn,self.measurment_id)
                        print(self.measurment_id)
                    time.sleep(self.frequency)
        except Exception as e:
            print(e)
        finally:
            if conn is not None:
                conn.close()


    #update parameters
    def update(self):
        self.average = sum(self.xs)/len(self.xs)
        self.minimum = min(self.xs)
        self.maximum = max(self.xs)

if __name__ == "__main__":
    print("XD")
