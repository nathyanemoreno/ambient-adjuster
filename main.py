import os
import sys
import simulateTemp
from interface import App
from classes import Room, Agent
from PyQt5.QtWidgets import *
# from multiprocessing import Pool, Queue
from time import perf_counter, sleep

if __name__ == '__main__':
	begin = perf_counter()
	
	room = Room()
	# agent = Agent()
	# room.powerBtn()
	# room.addSensor([2,3])
	# room.actDevices('sen')
	# room.checkStatus()
	app = QApplication(sys.argv)
	ambient = App(room)
	sys.exit(app.exec_())
	end = perf_counter()    
	timeExec = end - begin
	print(f"Tempo de execução: {timeExec}")

################################################################################333	
# print(room, agent)
# print(room.agent)
# room.setAgent(agent)
# print(room.agent)
# print(agent.room)
# room.checkStatus() 
# room.checkStatus() #Desactivated
# room.addSensor([2,3])
# room.checkStatus()
# print('Sensores ativados: %r' %(room.sensors[0].status))
# room.actDevices('sen')
# print('Sensores ativados: %r' %(room.sensors[0].status))

# Interface gráfica #############
