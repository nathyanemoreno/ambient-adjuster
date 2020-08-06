import sys
from classes import *
import simulateTemp
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class App(QWidget):
    def __init__(self, room=None):
        super().__init__()
        self.title = 'Ambient Adjuster'
        self.left = 10
        self.top = 10
        self.width = 1000
        self.height = 500
        self.room = room
        self.initUI()

    def showTemp(self, value):
        if self.room.status == True and self.room.timeWorking > value:
            tempboxValue = self.tempbox.text()
            self.tempbox.setText('%d' % self.room.timeWorking)

    def addButton(self, name, tip, resize, move):
        self.newBtn = QPushButton(name, self)
        self.newBtn.setToolTip(tip)
        self.newBtn.resize(resize[0], resize[1])
        self.newBtn.move(move[0], move[1])
        return self.newBtn

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.tempbox = QLineEdit(self)
        self.tempbox.move(100, 100)
        self.tempbox.resize(700, 50)

        btnPower = self.addButton(
            'Power', 'Click to power off or on', [120, 30], [20, 20])
        btnActSensors = self.addButton(
            'Activate Sensors', 'Click to power activate the sensors and actuators', [120, 30], [120+30, 20])
        btnActActuators = self.addButton(
            'Activate Actuators', 'Click to power activate the sensors and actuators', [120, 30], [2*120+40, 20])
        btnAddSensors = self.addButton(
            'Add Sensor', 'Click to power activate the sensors and actuators', [120, 30], [3*120+60, 20])
        btnAddSensors = self.addButton(
            'Add Actuator', 'Click to power activate the sensors and actuators', [120, 30], [4*120+80, 20])
        btnCheckStatus = self.addButton(
            'Check status', 'Click to power activate the sensors and actuators', [120, 30], [5*120+100, 20])

        btnPower.clicked.connect(self.on_click)
        btnActSensors.clicked.connect(self.on_actSensors)
        btnActActuators.clicked.connect(self.on_actActuators)
        btnAddSensors.clicked.connect(self.add_Sensor)
        btnAddSensors.clicked.connect(self.add_Actuator)
        btnCheckStatus.clicked.connect(self.checkStatus)
        self.show()

    @pyqtSlot()
    def on_click(self):
        self.room.powerBtn()
        self.room.checkStatus()
        self.showTemp(self.room.timeWorking)

    @pyqtSlot()
    def on_actSensors(self):
        self.room.actDevices('sen')

    @pyqtSlot()
    def on_actActuators(self):
        self.room.actDevices('act')

    @pyqtSlot()
    def add_Sensor(self):
        self.room.addDevice([2, 3], 'sen')

    @pyqtSlot()
    def add_Actuator(self):
        self.room.addDevice([4, 6], 'act')

    @pyqtSlot()
    def checkStatus(self):
        self.room.checkStatus()
        status = f'{self.room.checkStatus()} \n\t Temperatura: {self.room.checkTemp()}'
        self.tempbox.setText(status)
