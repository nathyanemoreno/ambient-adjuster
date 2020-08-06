import threading
from time import sleep
import simulateTemp


class Room:
    def __init__(self, r_size=[], nArc=1, time_check=5, timeWorking=0,
                 sensors=[], actuators=[], agent=None, status=False, externTemp=None):
        self.sensors, self.actuators, self.agent = sensors, actuators, agent
        self.time_check = time_check
        self.r_size = r_size
        self.nArc = nArc
        self.status = status
        self.timeWorking = timeWorking
        self.externTemp = externTemp

    def setAgent(self, agent):
        self.agent = agent
        agent.setRoom(self)

    def setConAR(self, conAR):
        self.conAR = conAR

    def addDevice(self, pos=[], Type=None):
        if Type == 'sen':
            sensor = Sensor(Type, pos)
            self.sensors.append(sensor)
        elif Type == 'act':
            actuator = Actuator(Type, pos)
            self.actuators.append(actuator)

    def powerBtn(self):  # botão para ativar os sensores e atuadores
        self.status = not self.status
        self.externTemp = simulateTemp.readTemp()


        '''if self.status == True:
			 self.checkTemp()
		 else:
			 pass'''

    def actDevices(self, param):
        if param == 'sen':
            for sensor in self.sensors:
                sensor.powerDevice()
        elif param == 'act':
            for actuator in self.actuators:
                actuator.powerDevice()

    def checkStatus(self):
        # retorna lista com desativados
        tempSen = list(filter(lambda x: x.status == False, self.sensors))
        tempAct = list(filter(lambda x: x.status == False, self.actuators))
        # verifica e printa o estado dos dispositivos e do sistema
        if self.status == True and len(tempSen) != 0 or len(tempAct) != 0:
            return f'System : Activated\n\tSensores ativos: {len(tempSen)} \n\tAtuadores ativos {len(tempAct)}'
        else:
            # print('System : Desactivated')
            # print(f'Status dos dispositivos: \n\tSensores ativos: {len(tempSen)} \n\tAtuadores ativos {len(tempAct)}')
            return f'System : Desactivated  \n\tSensores ativos: {len(tempSen)} \n\tAtuadores ativos {len(tempAct)}'

    def checkTemp(self):
        # print(self.timeWorking)
        if self.status == True:
            # t1 = threading.Thread(target=self.checkTemp)
            # self.timeWorking += self.time_check
            # sleep(self.time_check)
            # t1.start()
            self.externTemp = simulateTemp.readTemp()
            return self.externTemp['temperatura']['temp']
        else:
            pass


class CondicionadorAr():
    def __init__(self, caType, btu, inverter):
        self.caType = caType
        self.btu = btu
        self.inverter = True


class Agent():
    def __init__(self, agent=None, room=None):
        self.agent = agent
        self.room = room

    def setRoom(self, room):
        self.room = room


class Device():
    def __init__(self, pos, status=False):
        self.pos = pos
        self.status = status

    def powerDevice(self):
        self.status = not self.status


class Actuator (Device):
    def __init__(self, pos, status=False):
        super().__init__(pos, status)


class Sensor(Device):
    def __init__(self, pos, status):
        super().__init__(pos, status)
