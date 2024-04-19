import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice


class New(QMainWindow):
    def __init__(self):
        super(New, self).__init__()

        loadUi("design.ui", self)
        self.setWindowTitle('New')

        self.openB.clicked.connect(self.onOpen)
        self.closeB.clicked.connect(self.onClose)
        self.led13on.clicked.connect(self.led13_on)
        self.led13off.clicked.connect(self.led13_off)
        self.val = 0
        self.val_gost = 0
        self.Sh_on.stateChanged.connect(self.readPort)
        self.val_sht = 0

        self.serial = QSerialPort()
        self.serial.setBaudRate(9600)
        
        portList = []
        ports = QSerialPortInfo().availablePorts()
        for port in ports:
            portList.append(port.portName())
        print(portList)
        self.comL.addItems(portList)

    def onOpen(self):
        print('on')
        self.serial.setPortName(self.comL.currentText())
        self.serial.open(QIODevice.ReadWrite)
    
    def serialSend(self, data): # список int
        txs = ""
        for val in data:
            txs += str(val)
            txs += ','
        txs = txs[:-1]
        txs += ';'
        self.serial.write(txs.encode())

    def readPort(self):
        self.rx = self.serial.readAll()
        rxs = str(self.rx)
        res = [int(i) for i in rxs.split() if i.isdigit()]
        rxs.encode().strip()
        print(rxs)

    def onClose(self):
        print('close')
        self.serial.close()

    def led13_on(self):
        val = 1
        self.serialSend([0, val])

    def led13_off(self):
        val = 0
        self.serialSend([0, val])

    def closeEvent(self, e):
        super().closeEvent(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = New()
    window.show()
    sys.exit(app.exec_())