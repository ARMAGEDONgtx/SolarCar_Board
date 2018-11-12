# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_calendar.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import PyQt5
import time

class calendar(QtWidgets.QWidget):

    plot_on_close = PyQt5.QtCore.pyqtSignal(object, object)

    def setupUi(self):
        self.Form = QtWidgets.QWidget()
        self.Form.setObjectName("Form")
        self.Form.resize(476, 440)
        self.gridLayout2 = QtWidgets.QGridLayout(self.Form)
        self.gridLayout2.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.Form)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.timeEdit = QtWidgets.QTimeEdit(self.Form)
        self.timeEdit.setObjectName("timeEdit")
        self.horizontalLayout_2.addWidget(self.timeEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.Form)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.Form)
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.horizontalLayout.addWidget(self.timeEdit_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(self.Form)
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.verticalLayout.addWidget(self.calendarWidget_2)
        self.gridLayout2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.button_ok = QtWidgets.QPushButton()
        self.button_ok.setObjectName("button_ok")
        self.button_ok.setText("Ok")
        self.button_cancel = QtWidgets.QPushButton()
        self.button_cancel.setObjectName("button_cancel")
        self.button_cancel.setText("Cancel")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_3.addWidget(self.button_ok)
        self.horizontalLayout_3.addWidget(self.button_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.button_ok.clicked.connect(self.ok_clicked)
        self.button_cancel.clicked.connect(self.cancel_clicked)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.retranslateUi(self.Form)
        QtCore.QMetaObject.connectSlotsByName(self.Form)
        self.setLayout(self.gridLayout2)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Start point"))
        self.timeEdit.setDisplayFormat(_translate("Form", "HH:mm:ss"))
        self.label_2.setText(_translate("Form", "End point"))
        self.timeEdit_2.setDisplayFormat(_translate("Form", "HH:mm:ss"))

    def start_date(self):
        return self.calendarWidget.selectedDate()

    def start_time(self):
        return self.timeEdit.time()


    def end_date(self):
        return self.calendarWidget_2.selectedDate()

    def end_time(self):
        return self.timeEdit_2.time()


    def ok_clicked(self):
        try:
            start_dt = QtCore.QDateTime(self.start_date(), self.start_time()).toPyDateTime()
            end_dt = QtCore.QDateTime(self.end_date(),self.end_time()).toPyDateTime()
            self.plot_on_close.emit(start_dt,end_dt)
            self.close()
        except Exception as e:
            print(str(e))

    def cancel_clicked(self):
        self.close()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    cal = calendar()
    cal.setupUi()
    cal.show()
    sys.exit(app.exec_())