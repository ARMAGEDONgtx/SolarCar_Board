# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controller.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import mywidgets.mycalendar
import sql_functions as sql


class controller(QtWidgets.QWidget):


    def setupUi(self, measure , id_obiektu):
        self.controled_measure = measure
        self.controled_thread = None
        ## WHOLE SHIT FROM QTDESIGNER AND PYUIC5##############################

        self.Form = QtWidgets.QWidget()
        self.Form.setObjectName("Form")
        self.Form.resize(354, 403)
        self.gridLayout = QtWidgets.QGridLayout(self.Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        #self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName("verticalLayout")


        # label live
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_live = QtWidgets.QLabel(self.Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_live.setFont(font)
        self.label_live.setObjectName("label_live")
        self.horizontalLayout_2.addWidget(self.label_live)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # init button
        self.pushButton_init = QtWidgets.QPushButton(self.Form)
        self.pushButton_init.setText("")
        self.pushButton_init.setIcon(QtGui.QIcon("other/init.png"))
        self.pushButton_init.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_init.setFlat(True)
        self.pushButton_init.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_init.setObjectName("pushButton_init")
        self.horizontalLayout_2.addWidget(self.pushButton_init)

        # label select + combobox
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_select = QtWidgets.QLabel(self.Form)
        self.label_select.setObjectName("label_select")
        self.horizontalLayout.addWidget(self.label_select)
        self.comboBox = QtWidgets.QComboBox(self.Form)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.comboBox.setSizeAdjustPolicy(3)


        #play button
        self.pushButton_play = QtWidgets.QPushButton(self.Form)
        self.pushButton_play.setText("")
        self.pushButton_play.setIcon(QtGui.QIcon("other/play.png"))
        self.pushButton_play.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_play.setFlat(True)
        self.pushButton_play.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_play.setObjectName("pushButton_play")
        self.horizontalLayout_3.addWidget(self.pushButton_play)

        #Pause Button
        self.pushButton_pause = QtWidgets.QPushButton(self.Form)
        self.pushButton_pause.setText("")
        self.pushButton_pause.setIcon(QtGui.QIcon("other/pause.png"))
        self.pushButton_pause.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_pause.setFlat(True)
        self.pushButton_pause.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_pause.setObjectName("pushButton_pause")
        self.horizontalLayout_3.addWidget(self.pushButton_pause)

        #Stop button
        self.pushButton_stop = QtWidgets.QPushButton(self.Form)
        self.pushButton_stop.setText("")
        self.pushButton_stop.setIcon(QtGui.QIcon("other/stop.png"))
        self.pushButton_stop.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_stop.setFlat(True)
        self.pushButton_stop.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.horizontalLayout_3.addWidget(self.pushButton_stop)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        #back button
        self.pushButton_back = QtWidgets.QPushButton(self.Form)
        self.pushButton_back.setText("")
        self.pushButton_back.setIcon(QtGui.QIcon("other/back.png"))
        self.pushButton_back.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_back.setFlat(True)
        self.pushButton_back.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_back.setObjectName("pushButton_back")
        self.horizontalLayout_4.addWidget(self.pushButton_back)

        # callendar button
        self.pushButton_cal = QtWidgets.QPushButton(self.Form)
        self.pushButton_cal.setText("")
        self.pushButton_cal.setIcon(QtGui.QIcon("other/callendar.png"))
        self.pushButton_cal.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_cal.setFlat(True)
        self.pushButton_cal.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_cal.setObjectName("pushButton_cal")
        self.horizontalLayout_4.addWidget(self.pushButton_cal)


        #next button
        self.pushButton_next = QtWidgets.QPushButton(self.Form)
        self.pushButton_next.setText("")
        self.pushButton_next.setIcon(QtGui.QIcon("other/next.png"))
        self.pushButton_next.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_next.setFlat(True)
        self.pushButton_next.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_next.setObjectName("pushButton_next")
        self.horizontalLayout_4.addWidget(self.pushButton_next)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        #label last value
        self.label_last_value = QtWidgets.QLabel(self.Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_last_value.setFont(font)
        self.label_last_value.setObjectName("label_last_value")
        self.horizontalLayout_5.addWidget(self.label_last_value)

        #lcd last value
        self.lcd_lastvalue = QtWidgets.QLCDNumber(self.Form)
        self.lcd_lastvalue.setFrameShape(QtWidgets.QFrame.Box)
        self.lcd_lastvalue.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcd_lastvalue.setLineWidth(2)
        self.lcd_lastvalue.setObjectName("lcd_lastvalue")
        self.horizontalLayout_5.addWidget(self.lcd_lastvalue)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        #lavel average
        self.label_average = QtWidgets.QLabel(self.Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_average.setFont(font)
        self.label_average.setObjectName("label_average")
        self.horizontalLayout_6.addWidget(self.label_average)

        #lcd avreage
        self.lcd_average = QtWidgets.QLCDNumber(self.Form)
        self.lcd_average.setFrameShape(QtWidgets.QFrame.Box)
        self.lcd_average.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcd_average.setLineWidth(2)
        self.lcd_average.setObjectName("lcd_average")
        self.horizontalLayout_6.addWidget(self.lcd_average)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        #label minimum
        self.label_min = QtWidgets.QLabel(self.Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_min.setFont(font)
        self.label_min.setObjectName("label_min")
        self.horizontalLayout_7.addWidget(self.label_min)

        #lcd minimum
        self.lcd_minimum = QtWidgets.QLCDNumber(self.Form)
        self.lcd_minimum.setFrameShape(QtWidgets.QFrame.Box)
        self.lcd_minimum.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcd_minimum.setLineWidth(2)
        self.lcd_minimum.setObjectName("lcd_minimum")
        self.horizontalLayout_7.addWidget(self.lcd_minimum)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")

        #label maximum
        self.label_max = QtWidgets.QLabel(self.Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_max.setFont(font)
        self.label_max.setObjectName("label_max")
        self.horizontalLayout_8.addWidget(self.label_max)

        #lcd maximum
        self.lcd_maximum = QtWidgets.QLCDNumber(self.Form)
        self.lcd_maximum.setFrameShape(QtWidgets.QFrame.Box)
        self.lcd_maximum.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcd_maximum.setLineWidth(2)
        self.lcd_maximum.setObjectName("lcd_maximum")
        self.horizontalLayout_8.addWidget(self.lcd_maximum)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        # generate data button
        self.pushButton_generate = QtWidgets.QPushButton(self.Form)
        self.pushButton_generate.setText("Generate Data")
        self.pushButton_generate.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_generate.setObjectName("pushButton_generate")
        self.verticalLayout.addWidget(self.pushButton_generate)

        #slider
        self.slider_time = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_time.setObjectName("slider_time")
        self.slider_time.setMinimum(1)
        self.slider_time.setMaximum(20)
        self.verticalLayout.addWidget(self.slider_time)
        self.slider_time.setValue(self.controled_measure.frequency)


        ##### CALENDAR SETUP ######################################################
        self.cal = mywidgets.mycalendar.calendar()
        self.cal.setupUi()

        ##########################################################################
        #add objects to combobox
        self.comboBox.addItem("")
        if id_obiektu is not None:
            conn = sql.connect_to_sql()
            list = sql.avaiable_measurments(conn, id_obiektu)
            for x in list:
                self.comboBox.addItem(x[1])
            conn.close()


        self.retranslateUi()
        self.setLayout(self.gridLayout)

        ####### SIGNALS AND SLOTS ###############################################3
        self.pushButton_play.clicked.connect(self.handle_play)
        self.pushButton_pause.clicked.connect(self.handle_pause)
        self.pushButton_stop.clicked.connect(self.handle_stop)
        self.pushButton_cal.clicked.connect(self.show_calendar)
        self.pushButton_generate.clicked.connect(self.handle_generate)
        self.comboBox.currentIndexChanged.connect(self.handle_combobox)
        self.slider_time.valueChanged.connect(self.handle_slider)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Form.setWindowTitle(_translate("Form", "Form"))
        self.label_select.setText(_translate("Form", "Select variable:"))
        self.label_live.setText(_translate("Form", "Live"))
        self.label_last_value.setText(_translate("Form", "Last value: "))
        self.label_average.setText(_translate("Form", "Average:     "))
        self.label_min.setText(_translate("Form", "Minimum:   "))
        self.label_max.setText(_translate("Form", "Maximum:  "))

    #bind thread on which buttons actions will take affects
    def bind_thread(self, thread_tb_bind):
        self.controled_thread = thread_tb_bind

    #function called when play button is clicked
    def handle_play(self):
        try:
            self.controled_measure.thread1.unpause()
            if self.controled_thread is not None:
                self.controled_thread.unpause()
            self.live_status()
        except Exception as e:
            print(str(e))

    # function called when pause button is clicked
    def handle_pause(self):
        try:
            self.controled_measure.thread1.pause()
            if self.controled_thread is not None:
                self.controled_thread.pause()
            self.live_status()
        except Exception as e:
            print(str(e))

    # function called when stop button is clicked
    def handle_stop(self):
        try:
            self.controled_measure.thread1.stop()
            if self.controled_thread is not None:
                self.controled_thread.stop()
            self.live_status()
        except Exception as e:
            print(str(e))

    # show callendar widget
    def show_calendar(self):
        self.cal.show()

    # update lcd display
    def display_parameters(self,average, min, max, last):
        self.lcd_average.display(average)
        self.lcd_minimum.display(min)
        self.lcd_maximum.display(max)
        self.lcd_lastvalue.display(last)

    #combobox changed
    def handle_combobox(self):
        conn = sql.connect_to_sql()
        self.controled_measure.measurment_id = sql.nazwa_pomiaru_to_id(conn, self.comboBox.currentText())
        #print(self.controled_measure.measurment_id)
        conn.close()

    # generate button clicked
    def handle_generate(self):
        try:
            if self.controled_measure.measurment_id is not None:
                self.controled_measure.thread1.start()
        except Exception as e:
            print(str(e))

    #slider value cahnged
    def handle_slider(self):
        self.controled_measure.frequency = self.slider_time.value()

    #manage live status
    def live_status(self):
        if self.controled_thread.stopped() is True:
            self.setStyleSheet('QLabel#label_live {color: red;}')
        elif self.controled_thread.paused() is True:
            self.setStyleSheet('QLabel#label_live {color: yellow;}')
        elif self.controled_thread.started() is True:
            self.setStyleSheet('QLabel#label_live {color: green;}')
        else:
            self.setStyleSheet('QLabel#label_live {color: white;}')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    con = controller()
    con.setupUi(1)
    con.show()
    sys.exit(app.exec_())