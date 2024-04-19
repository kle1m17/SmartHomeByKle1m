import sys
import arduino
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QWidget
from PyQt5.uic import loadUi
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice, Qt
from PyQt5 import QtWidgets, QtGui
import time
import threading

from Ui_MainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):

    def Check_Pass(self, password):
        file = open('password.txt', 'r')
        passw = file.read()
        file.close()
        activ = open('activity.txt', 'a')
        if password == passw:
            self.password_state = 1
            activ.write(f'{time.ctime(time.time())} Entered Password!\n')
            self.ui.Security_Activity.addItem(f"{time.ctime(time.time())} Entered Pasword!")
            activ.close()
        else: 
            activ.write(f'{time.ctime(time.time())} Password was entered incorrectly!\n')            
            self.ui.Security_Activity.addItem(f'{time.ctime(time.time())} Password was entered incorrectly!\n')
            self.password_state = 0

    def Check_Password(self):
        if self.password_state == 1:
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.Vhod_Dveri)
        else: 
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.Nothing)

    def Set_Pass(self, password):
        file = open('password.txt', 'w')
        file.write(password)
        file.close()

    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ar = arduino.Arduino()
        self.password_state = 0
        self.main_win.setWindowTitle("SmartHome")
        self.main_win.setWindowIcon(QtGui.QIcon("ICONS/ios-navigate.svg"))

        self.Check_Password()

        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)
        self.ui.BTN_Home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Home))
        self.ui.BTN_Light.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Light))
        self.ui.BTN_Security.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Security))
        self.ui.BTN_Settings.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Settings))
        self.ui.BTN_About.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.About))
        
        #Управление Светом 1 часть
        self.ui.Kor_Light_On_4.clicked.connect(lambda: self.ui.Light_Kor1.setStyleSheet("border: 2px solid #fff;\n background-color: #cfff67;"))
        self.ui.Kor_Light_Off_4.clicked.connect(lambda: self.ui.Light_Kor1.setStyleSheet("border: 2px solid #fff;\n background-color: none"))
        self.ui.Gar_Light_On_3.clicked.connect(lambda: self.ui.Light_Gar1.setStyleSheet("border: 2px solid #fff;\n background-color: #cfff67;"))
        self.ui.Gar_Light_Off_3.clicked.connect(lambda: self.ui.Light_Gar1.setStyleSheet("border: 2px solid #fff;\n background-color: none"))
        self.ui.Gost_Light_On_4.clicked.connect(lambda: self.ui.Light_Gost1.setStyleSheet("border: 2px solid #fff;\n background-color: #cfff67;"))
        self.ui.Gost_Light_Off_4.clicked.connect(lambda: self.ui.Light_Gost1.setStyleSheet("border: 2px solid #fff;\n background-color: none"))
        #Управление светом 2 часть
        self.ui.Kor_Light_On_4.clicked.connect(lambda: self.ui.Light_Kor2.setStyleSheet("border: 2px solid #fff;\n background-color: #cfff67;"))
        self.ui.Kor_Light_Off_4.clicked.connect(lambda: self.ui.Light_Kor2.setStyleSheet("border: 2px solid #fff;\n background-color: none"))
        self.ui.Gar_Light_On_3.clicked.connect(lambda: self.ui.Light_Gar_2.setStyleSheet("border: 2px solid #fff;\n background-color: #cfff67;"))
        self.ui.Gar_Light_Off_3.clicked.connect(lambda: self.ui.Light_Gar_2.setStyleSheet("border: 2px solid #fff;\n background-color: none"))
        self.ui.Gost_Light_On_4.clicked.connect(lambda: self.ui.Light_Gost2.setStyleSheet("border: 2px solid #fff;\n background-color: #cfff67;"))
        self.ui.Gost_Light_Off_4.clicked.connect(lambda: self.ui.Light_Gost2.setStyleSheet("border: 2px solid #fff;\n background-color: none"))

        #Управление светом через Ардуино (import arduino)

        self.ui.Kor_Light_On_4.clicked.connect(lambda: self.ar.Light_Kor_On())
        self.ui.Kor_Light_Off_4.clicked.connect(lambda: self.ar.Ligh_Kor_Off())
        self.ui.Gar_Light_On_3.clicked.connect(lambda: self.ar.Ligh_Gar_On())
        self.ui.Gar_Light_Off_3.clicked.connect(lambda: self.ar.Ligh_Gar_Off())
        self.ui.Gost_Light_On_4.clicked.connect(lambda: self.ar.Ligh_Gost_On())
        self.ui.Gost_Light_Off_4.clicked.connect(lambda: self.ar.Ligh_Gost_Off())


        #Пароль управление
        self.ui.BTN_Enter_Pass.clicked.connect(lambda: self.Check_Pass(self.ui.Enter_Pass_Line.text()))
        self.ui.BTN_Enter_Pass.clicked.connect(lambda: self.Check_Password())

        self.ui.BTN_Set_Pass.clicked.connect(lambda: self.ui.Check_State_Pass.setStyleSheet("border: 1px solid rgb(35, 255, 71);\n color: white;\n border-radius: 10%;"))
        self.ui.BTN_Set_Pass.clicked.connect(lambda: self.ui.Check_State_Pass.setText('Пароль успешно установлен!'))
        self.file1 = open("activity.txt", 'a')
        self.ui.BTN_Set_Pass.clicked.connect(lambda: self.file1.write(f'{time.ctime(time.time())} User was changed password!\n'))
        self.ui.BTN_Set_Pass.clicked.connect(lambda: self.ui.Security_Activity.addItem(f'{time.ctime(time.time())} User was changed password!\n'))
        
        self.ui.BTN_Set_Pass.clicked.connect(lambda: self.Set_Pass(self.ui.Line_Set_Pass.text()))

        #Дверь, шлакбаум и ворота
        self.ui.Open_Vhod.clicked.connect(lambda: self.ar.Open_Door())
        self.ui.Close_Vhod.clicked.connect(lambda: self.ar.Close_Door())
        self.ui.Gar_Ope.clicked.connect(lambda: self.ar.Open_Garage())
        self.ui.Gar_Close.clicked.connect(lambda: self.ar.Close_Garage())
        self.ui.Shlak_Open.clicked.connect(lambda: self.ar.Open_Shlag())
        self.ui.Slack_Close.clicked.connect(lambda: self.ar.Close_Shlag())

        #Центр активности
        self.file = open("activity.txt", 'r')
        while True:
            self.line = self.file.readline()
            if not self.line:
                break
            self.ui.Security_Activity.addItem(self.line)
        
        self.file.close()
        



    def Message_Box(self, text: str):
        QtWidgets.QMessageBox.about(self, text)

    def Show(self):
        self.main_win.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.Show()
    sys.exit(app.exec_())
