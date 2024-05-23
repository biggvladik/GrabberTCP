import datetime

from PyQt5.QtCore import *
from TCP_receiver import *
import traceback





# Поток для работы с бегущем временем
class Thread_1(QThread):
    signal_status = pyqtSignal(bool)


    def __init__(self,mainwindow,parent = None):
        super().__init__()
        self.mainwindow = mainwindow


    def run(self):
        # Подключаемся к БД


        # Подключаемся к серверу, откуда будем принимать
        try:
            receiver = TCP_receiver()
            receiver.connect(self.mainwindow.ui.lineEdit_2.text(),int(self.mainwindow.ui.lineEdit.text()))
            self.signal_status.emit(True)

            status = True
        except:
            status = False
            self.signal_status.emit(False)
            print(traceback.format_exc())
            return

        while True:
            try:
                now = datetime.datetime.now()
                data = receiver.receive_data()
                receiver.write_logs(str(now) + ' --- ' + str(data),'byte_logs')
                receiver.write_logs(str(now) + ' --- ' + data.decode('ascii','replace'), 'byte_ascii')
                self.signal_status.emit(True)
            except:
                self.signal_status.emit(False)
                print(traceback.format_exc())