import sys
import traceback
from PyQt5.QtCore import *
from PyQt5.QtWidgets import  QMainWindow,QApplication
from window import Ui_MainWindow
from TCP_receiver import TCP_receiver
from Thread_1 import Thread_1
import configparser
class ImageDialog(QMainWindow):
    signal_server = pyqtSignal(TCP_receiver)


    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.settings = QSettings('GrabberBob', 'GrabberBob')
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.launch_thread1)
        try:
            self.set_old_values()
        except:
            print(traceback.format_exc())



    def launch_thread1(self):
        try:
            if self.mythread_1.isRunning():
                self.mythread_1.terminate()
                self.mythread_1 = Thread_1(mainwindow=self)
                self.mythread_1.signal_status.connect(self.change_status_tcp)
                self.mythread_1.start()
            else:
                self.mythread_1 = Thread_1(mainwindow=self)
                self.mythread_1.signal_status.connect(self.change_status_tcp)
                self.mythread_1.start()
        except:
            self.mythread_1 = Thread_1(mainwindow=self)
            self.mythread_1.signal_status.connect(self.change_status_tcp)
            self.mythread_1.start()







    def closeEvent(self, event):
        self.settings.setValue('host1', self.ui.lineEdit_2.text())
        self.settings.setValue('port1', self.ui.lineEdit.text())








    def set_old_values(self):
        try:
            self.ui.lineEdit.setText(self.settings.value('port1'))
            self.ui.lineEdit_2.setText(self.settings.value('host1'))
        except:
            print(traceback.format_exc())


    def change_status_tcp(self,item:bool):
        if item:
            self.ui.label_3.setStyleSheet('color: rgb(0, 100, 0); font: bold 14px;')
        else:
            self.ui.label_3.setStyleSheet('color: rgb(255, 0, 0); font: bold 14px;')

app = QApplication(sys.argv)
window = ImageDialog()
window.show()

sys.exit(app.exec())