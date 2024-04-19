from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice

class Arduino():
    def __init__(self):
        self.serial = QSerialPort()
        self.serial.setBaudRate(9600)

        self.serial.setPortName('COM3')
        self.serial.open(QIODevice.ReadWrite)

    def serialSend(self, data):
        txs = ""
        for val in data:
            txs += str(val)
            txs += ','
        txs = txs[:-1]
        txs += ';'
        self.serial.write(txs.encode())

    def Light_Kor_On(self):
        self.serialSend([2,1])

    def Ligh_Kor_Off(self):
        self.serialSend([3, 1])

    def Ligh_Gar_On(self):
        self.serialSend([1, 1])
    
    def Ligh_Gar_Off(self):
        self.serialSend([6, 1])
        
    def Ligh_Gost_On(self):
        self.serialSend([4, 1])

    def Ligh_Gost_Off(self):
        self.serialSend([5, 1])

    def Open_Door(self):
        self.serialSend([7, 1])
        
    def Close_Door(self):
        self.serialSend([8, 1])

    def Open_Shlag(self):
        self.serialSend([9, 1])
    
    def Close_Shlag(self):
        self.serialSend([10, 1])

    def Open_Garage(self):
        self.serialSend([11, 1])

    def Close_Garage(self):
        self.serialSend([12, 1])
