# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1073, 614)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 45);\n"
"border-radius: 20%;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 191, 621))
        self.widget.setStyleSheet("background-color: rgb(115, 101, 114);\n"
"border-radius: 0%;")
        self.widget.setObjectName("widget")
        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 171, 561))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.BTN_Home = QtWidgets.QPushButton(self.layoutWidget)
        self.BTN_Home.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"background-color: rgb(74, 171, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ICONS/ios-home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_Home.setIcon(icon)
        self.BTN_Home.setObjectName("BTN_Home")
        self.verticalLayout_2.addWidget(self.BTN_Home)
        self.BTN_Light = QtWidgets.QPushButton(self.layoutWidget)
        self.BTN_Light.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"background-color: rgb(74, 171, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ICONS/ios-bulb.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_Light.setIcon(icon1)
        self.BTN_Light.setObjectName("BTN_Light")
        self.verticalLayout_2.addWidget(self.BTN_Light)
        self.BTN_Security = QtWidgets.QPushButton(self.layoutWidget)
        self.BTN_Security.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"background-color: rgb(74, 171, 255);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ICONS/md-camera.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_Security.setIcon(icon2)
        self.BTN_Security.setObjectName("BTN_Security")
        self.verticalLayout_2.addWidget(self.BTN_Security)
        spacerItem = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.BTN_Settings = QtWidgets.QPushButton(self.layoutWidget)
        self.BTN_Settings.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"background-color: rgb(74, 171, 255);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ICONS/ios-cog.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_Settings.setIcon(icon3)
        self.BTN_Settings.setObjectName("BTN_Settings")
        self.verticalLayout_2.addWidget(self.BTN_Settings)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.BTN_About = QtWidgets.QPushButton(self.layoutWidget)
        self.BTN_About.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"background-color: rgb(74, 171, 255);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ICONS/info-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_About.setIcon(icon4)
        self.BTN_About.setObjectName("BTN_About")
        self.verticalLayout_3.addWidget(self.BTN_About)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(190, -10, 431, 641))
        self.stackedWidget.setStyleSheet("background-color: rgb(54, 54, 54)")
        self.stackedWidget.setObjectName("stackedWidget")
        self.Home = QtWidgets.QWidget()
        self.Home.setObjectName("Home")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.Home)
        self.stackedWidget_2.setGeometry(QtCore.QRect(0, 10, 531, 121))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.Vhod_Dveri = QtWidgets.QWidget()
        self.Vhod_Dveri.setObjectName("Vhod_Dveri")
        self.layoutWidget1 = QtWidgets.QWidget(self.Vhod_Dveri)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 30, 391, 75))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"background-color: rgb(74, 171, 255);")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Open_Vhod = QtWidgets.QPushButton(self.layoutWidget1)
        self.Open_Vhod.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"background-color: rgb(74, 171, 255);")
        self.Open_Vhod.setObjectName("Open_Vhod")
        self.horizontalLayout_3.addWidget(self.Open_Vhod)
        self.Close_Vhod = QtWidgets.QPushButton(self.layoutWidget1)
        self.Close_Vhod.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"background-color: rgb(74, 171, 255);")
        self.Close_Vhod.setObjectName("Close_Vhod")
        self.horizontalLayout_3.addWidget(self.Close_Vhod)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.stackedWidget_2.addWidget(self.Vhod_Dveri)
        self.Nothing = QtWidgets.QWidget()
        self.Nothing.setObjectName("Nothing")
        self.stackedWidget_2.addWidget(self.Nothing)
        self.layoutWidget_5 = QtWidgets.QWidget(self.Home)
        self.layoutWidget_5.setGeometry(QtCore.QRect(20, 250, 391, 75))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAccessibleDescription("")
        self.label_9.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"background-color: rgb(74, 171, 255);")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_9.addWidget(self.label_9)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Gar_Ope = QtWidgets.QPushButton(self.layoutWidget_5)
        self.Gar_Ope.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"background-color: rgb(74, 171, 255);")
        self.Gar_Ope.setObjectName("Gar_Ope")
        self.horizontalLayout_5.addWidget(self.Gar_Ope)
        self.Gar_Close = QtWidgets.QPushButton(self.layoutWidget_5)
        self.Gar_Close.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"background-color: rgb(74, 171, 255);")
        self.Gar_Close.setObjectName("Gar_Close")
        self.horizontalLayout_5.addWidget(self.Gar_Close)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.layoutWidget2 = QtWidgets.QWidget(self.Home)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 150, 391, 75))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAccessibleDescription("")
        self.label_8.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"background-color: rgb(74, 171, 255);")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Shlak_Open = QtWidgets.QPushButton(self.layoutWidget2)
        self.Shlak_Open.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"background-color: rgb(74, 171, 255);")
        self.Shlak_Open.setObjectName("Shlak_Open")
        self.horizontalLayout_4.addWidget(self.Shlak_Open)
        self.Slack_Close = QtWidgets.QPushButton(self.layoutWidget2)
        self.Slack_Close.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"background-color: rgb(74, 171, 255);")
        self.Slack_Close.setObjectName("Slack_Close")
        self.horizontalLayout_4.addWidget(self.Slack_Close)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.stackedWidget.addWidget(self.Home)
        self.Light = QtWidgets.QWidget()
        self.Light.setObjectName("Light")
        self.label_2 = QtWidgets.QLabel(self.Light)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"background-color: rgb(74, 171, 255);\n"
"text-align: center;")
        self.label_2.setObjectName("label_2")
        self.layoutWidget3 = QtWidgets.QWidget(self.Light)
        self.layoutWidget3.setGeometry(QtCore.QRect(30, 120, 371, 381))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"text-align: center;")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_30.addWidget(self.label_17)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.Kor_Light_On_4 = QtWidgets.QPushButton(self.layoutWidget3)
        self.Kor_Light_On_4.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"text-align: center;")
        self.Kor_Light_On_4.setObjectName("Kor_Light_On_4")
        self.horizontalLayout_23.addWidget(self.Kor_Light_On_4)
        self.Kor_Light_Off_4 = QtWidgets.QPushButton(self.layoutWidget3)
        self.Kor_Light_Off_4.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"text-align: center;")
        self.Kor_Light_Off_4.setObjectName("Kor_Light_Off_4")
        self.horizontalLayout_23.addWidget(self.Kor_Light_Off_4)
        self.verticalLayout_30.addLayout(self.horizontalLayout_23)
        self.verticalLayout_33.addLayout(self.verticalLayout_30)
        self.verticalLayout_31 = QtWidgets.QVBoxLayout()
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"text-align: center;")
        self.label_18.setObjectName("label_18")
        self.verticalLayout_31.addWidget(self.label_18)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.Gost_Light_On_4 = QtWidgets.QPushButton(self.layoutWidget3)
        self.Gost_Light_On_4.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"text-align: center;")
        self.Gost_Light_On_4.setObjectName("Gost_Light_On_4")
        self.horizontalLayout_24.addWidget(self.Gost_Light_On_4)
        self.Gost_Light_Off_4 = QtWidgets.QPushButton(self.layoutWidget3)
        self.Gost_Light_Off_4.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"text-align: center;")
        self.Gost_Light_Off_4.setObjectName("Gost_Light_Off_4")
        self.horizontalLayout_24.addWidget(self.Gost_Light_Off_4)
        self.verticalLayout_31.addLayout(self.horizontalLayout_24)
        self.verticalLayout_33.addLayout(self.verticalLayout_31)
        self.verticalLayout_32 = QtWidgets.QVBoxLayout()
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.label_19 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"text-align: center;")
        self.label_19.setObjectName("label_19")
        self.verticalLayout_32.addWidget(self.label_19)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.Gar_Light_On_3 = QtWidgets.QPushButton(self.layoutWidget3)
        self.Gar_Light_On_3.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"text-align: center;")
        self.Gar_Light_On_3.setObjectName("Gar_Light_On_3")
        self.horizontalLayout_25.addWidget(self.Gar_Light_On_3)
        self.Gar_Light_Off_3 = QtWidgets.QPushButton(self.layoutWidget3)
        self.Gar_Light_Off_3.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"text-align: center;")
        self.Gar_Light_Off_3.setObjectName("Gar_Light_Off_3")
        self.horizontalLayout_25.addWidget(self.Gar_Light_Off_3)
        self.verticalLayout_32.addLayout(self.horizontalLayout_25)
        self.verticalLayout_33.addLayout(self.verticalLayout_32)
        self.stackedWidget.addWidget(self.Light)
        self.Security = QtWidgets.QWidget()
        self.Security.setObjectName("Security")
        self.layoutWidget4 = QtWidgets.QWidget(self.Security)
        self.layoutWidget4.setGeometry(QtCore.QRect(30, 40, 371, 91))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"background-color: rgb(74, 171, 255);\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Enter_Pass_Line = QtWidgets.QLineEdit(self.layoutWidget4)
        self.Enter_Pass_Line.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"\n"
"")
        self.Enter_Pass_Line.setObjectName("Enter_Pass_Line")
        self.horizontalLayout.addWidget(self.Enter_Pass_Line)
        self.BTN_Enter_Pass = QtWidgets.QPushButton(self.layoutWidget4)
        self.BTN_Enter_Pass.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"background-color: rgb(74, 171, 255);\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("ICONS/ios-cloud-upload.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_Enter_Pass.setIcon(icon5)
        self.BTN_Enter_Pass.setObjectName("BTN_Enter_Pass")
        self.horizontalLayout.addWidget(self.BTN_Enter_Pass)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.layoutWidget5 = QtWidgets.QWidget(self.Security)
        self.layoutWidget5.setGeometry(QtCore.QRect(10, 160, 411, 451))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"background-color: rgb(74, 171, 255);\n"
"")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.Security_Activity = QtWidgets.QListWidget(self.layoutWidget5)
        self.Security_Activity.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;")
        self.Security_Activity.setObjectName("Security_Activity")
        self.verticalLayout_4.addWidget(self.Security_Activity)
        self.stackedWidget.addWidget(self.Security)
        self.Settings = QtWidgets.QWidget()
        self.Settings.setObjectName("Settings")
        self.layoutWidget6 = QtWidgets.QWidget(self.Settings)
        self.layoutWidget6.setGeometry(QtCore.QRect(21, 41, 391, 101))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"background-color: rgb(74, 171, 255);")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_10.addWidget(self.label_10)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Line_Set_Pass = QtWidgets.QLineEdit(self.layoutWidget6)
        self.Line_Set_Pass.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"background-color: rgb(74, 171, 255);")
        self.Line_Set_Pass.setObjectName("Line_Set_Pass")
        self.horizontalLayout_6.addWidget(self.Line_Set_Pass)
        self.BTN_Set_Pass = QtWidgets.QPushButton(self.layoutWidget6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.BTN_Set_Pass.setFont(font)
        self.BTN_Set_Pass.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"background-color: rgb(74, 171, 255);")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("ICONS/ios-add-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_Set_Pass.setIcon(icon6)
        self.BTN_Set_Pass.setObjectName("BTN_Set_Pass")
        self.horizontalLayout_6.addWidget(self.BTN_Set_Pass)
        self.verticalLayout_10.addLayout(self.horizontalLayout_6)
        self.Check_State_Pass = QtWidgets.QLabel(self.layoutWidget6)
        self.Check_State_Pass.setStyleSheet("")
        self.Check_State_Pass.setText("")
        self.Check_State_Pass.setObjectName("Check_State_Pass")
        self.verticalLayout_10.addWidget(self.Check_State_Pass)
        self.stackedWidget.addWidget(self.Settings)
        self.About = QtWidgets.QWidget()
        self.About.setObjectName("About")
        self.label_4 = QtWidgets.QLabel(self.About)
        self.label_4.setGeometry(QtCore.QRect(40, 40, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border: 2px solid rgb(123, 111, 255);\n"
"color: white;\n"
"border-radius: 10%;\n"
"height: 30px;\n"
"background-color: rgb(74, 171, 255);")
        self.label_4.setObjectName("label_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.About)
        self.textBrowser.setGeometry(QtCore.QRect(40, 120, 351, 451))
        self.textBrowser.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.stackedWidget.addWidget(self.About)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(620, 0, 451, 631))
        self.groupBox_3.setStyleSheet("alternate-background-color: rgb(42, 42, 42);")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.line = QtWidgets.QFrame(self.groupBox_3)
        self.line.setGeometry(QtCore.QRect(20, 20, 16, 561))
        self.line.setStyleSheet("border: 2px solid #fff;\n"
"")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.groupBox_3)
        self.line_2.setGeometry(QtCore.QRect(20, 570, 286, 16))
        self.line_2.setStyleSheet("border: 2px solid #fff;\n"
"")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.groupBox_3)
        self.line_3.setGeometry(QtCore.QRect(20, 400, 371, 16))
        self.line_3.setStyleSheet("border: 2px solid #fff;\n"
"")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.groupBox_3)
        self.line_4.setGeometry(QtCore.QRect(20, 190, 371, 16))
        self.line_4.setStyleSheet("border: 2px solid #fff;\n"
"")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.groupBox_3)
        self.line_5.setGeometry(QtCore.QRect(20, 20, 286, 16))
        self.line_5.setStyleSheet("border: 2px solid #fff;\n"
"")
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.groupBox_3)
        self.line_6.setGeometry(QtCore.QRect(290, 20, 16, 566))
        self.line_6.setStyleSheet("border: 2px solid #fff;\n"
"")
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.groupBox_3)
        self.line_7.setGeometry(QtCore.QRect(375, 190, 16, 226))
        self.line_7.setStyleSheet("border: 2px solid #fff;\n"
"")
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.Light_Kor2 = QtWidgets.QFrame(self.groupBox_3)
        self.Light_Kor2.setGeometry(QtCore.QRect(50, 415, 21, 21))
        self.Light_Kor2.setStyleSheet("border: 2px solid #fff;\n"
"")
        self.Light_Kor2.setFrameShape(QtWidgets.QFrame.VLine)
        self.Light_Kor2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Light_Kor2.setObjectName("Light_Kor2")
        self.Light_Kor1 = QtWidgets.QFrame(self.groupBox_3)
        self.Light_Kor1.setGeometry(QtCore.QRect(250, 415, 21, 21))
        self.Light_Kor1.setStyleSheet("border: 2px solid #fff;\n"
"")
        self.Light_Kor1.setFrameShape(QtWidgets.QFrame.VLine)
        self.Light_Kor1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Light_Kor1.setObjectName("Light_Kor1")
        self.Light_Gost1 = QtWidgets.QFrame(self.groupBox_3)
        self.Light_Gost1.setGeometry(QtCore.QRect(250, 205, 21, 21))
        self.Light_Gost1.setStyleSheet("border: 2px solid #fff;\n"
"")
        self.Light_Gost1.setFrameShape(QtWidgets.QFrame.VLine)
        self.Light_Gost1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Light_Gost1.setObjectName("Light_Gost1")
        self.Light_Gost2 = QtWidgets.QFrame(self.groupBox_3)
        self.Light_Gost2.setGeometry(QtCore.QRect(50, 205, 21, 21))
        self.Light_Gost2.setStyleSheet("border: 2px solid #fff;\n"
"")
        self.Light_Gost2.setFrameShape(QtWidgets.QFrame.VLine)
        self.Light_Gost2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Light_Gost2.setObjectName("Light_Gost2")
        self.Light_Gar1 = QtWidgets.QFrame(self.groupBox_3)
        self.Light_Gar1.setGeometry(QtCore.QRect(320, 204, 21, 21))
        self.Light_Gar1.setStyleSheet("border: 2px solid #fff;\n"
"")
        self.Light_Gar1.setFrameShape(QtWidgets.QFrame.VLine)
        self.Light_Gar1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Light_Gar1.setObjectName("Light_Gar1")
        self.Light_Gar_2 = QtWidgets.QFrame(self.groupBox_3)
        self.Light_Gar_2.setGeometry(QtCore.QRect(320, 381, 21, 21))
        self.Light_Gar_2.setStyleSheet("border: 2px solid #fff;\n"
"")
        self.Light_Gar_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.Light_Gar_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Light_Gar_2.setObjectName("Light_Gar_2")
        self.Color = QtWidgets.QGroupBox(self.groupBox_3)
        self.Color.setGeometry(QtCore.QRect(20, 20, 281, 571))
        self.Color.setStyleSheet("border-radius: 0px;")
        self.Color.setTitle("")
        self.Color.setObjectName("Color")
        self.Color.raise_()
        self.line_6.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.line_5.raise_()
        self.line_7.raise_()
        self.Light_Kor2.raise_()
        self.Light_Gost1.raise_()
        self.Light_Gost2.raise_()
        self.Light_Gar1.raise_()
        self.Light_Gar_2.raise_()
        self.Light_Kor1.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BTN_Home.setText(_translate("MainWindow", "Home"))
        self.BTN_Light.setText(_translate("MainWindow", "Light"))
        self.BTN_Security.setText(_translate("MainWindow", "Security"))
        self.BTN_Settings.setText(_translate("MainWindow", "Settings"))
        self.BTN_About.setText(_translate("MainWindow", "About"))
        self.label_7.setText(_translate("MainWindow", "Входная дверь"))
        self.Open_Vhod.setText(_translate("MainWindow", "Открыть"))
        self.Close_Vhod.setText(_translate("MainWindow", "Закрыть"))
        self.label_9.setText(_translate("MainWindow", "Ворота"))
        self.Gar_Ope.setText(_translate("MainWindow", "Открыть"))
        self.Gar_Close.setText(_translate("MainWindow", "Закрыть"))
        self.label_8.setText(_translate("MainWindow", "Шлагбаум"))
        self.Shlak_Open.setText(_translate("MainWindow", "Открыть"))
        self.Slack_Close.setText(_translate("MainWindow", "Закрыть"))
        self.label_2.setText(_translate("MainWindow", "             Управление светом"))
        self.label_17.setText(_translate("MainWindow", "                      Свет в коридоре"))
        self.Kor_Light_On_4.setText(_translate("MainWindow", "Включить"))
        self.Kor_Light_Off_4.setText(_translate("MainWindow", "Выключить"))
        self.label_18.setText(_translate("MainWindow", "                      Свет в гостинной"))
        self.Gost_Light_On_4.setText(_translate("MainWindow", "Включить"))
        self.Gost_Light_Off_4.setText(_translate("MainWindow", "Выключить"))
        self.label_19.setText(_translate("MainWindow", "                      Свет в гараже"))
        self.Gar_Light_On_3.setText(_translate("MainWindow", "Включить"))
        self.Gar_Light_Off_3.setText(_translate("MainWindow", "Выключить"))
        self.label.setText(_translate("MainWindow", "Пароль для открытия двери"))
        self.BTN_Enter_Pass.setText(_translate("MainWindow", "Отправить"))
        self.label_3.setText(_translate("MainWindow", "Просмотр активности"))
        self.label_10.setText(_translate("MainWindow", "Задать пароль"))
        self.BTN_Set_Pass.setText(_translate("MainWindow", "Задать"))
        self.label_4.setText(_translate("MainWindow", "О приложении \"Smart Home\""))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">Данное приложения является аппаратной частью проекта &quot;Smart Home&quot;. Приложение написанно на языке программирования </span><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Python</span><span style=\" font-size:12pt; color:#ffffff;\">, для графического интерфейса была использованна библиотека </span><span style=\" font-size:12pt; font-weight:600; font-style:italic; text-decoration: underline; color:#ffffff;\">PyQt5</span><span style=\" font-size:12pt; color:#ffffff;\">. В аппаратной части лежит система из датчиков и моторов на базе </span><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Arduino Uno. </span><span style=\" font-size:12pt; color:#ffffff;\">Для общения между компьютером и платой </span><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Arduino</span><span style=\" font-size:12pt; color:#ffffff;\"> используется всё та же библиотека </span><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">PyQt5</span><span style=\" font-size:12pt; color:#ffffff;\">. Для редактирования графической части приложения использовался бесплатный редактор QtDesigner.</span></p></body></html>"))
