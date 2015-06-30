#from multiprocessing import Pipe,Process
import time
import numpy as np
#import copy
#import Blocks
#import Links
import crappy as modules
modules.blocks.MasterBlock.instances=[] # Init masterblock instances
from crappy.technical import Ximea

class condition_cycle(modules.links.Condition):
	def __init__(self):
		self.cycle=0
		self.go=True
		
	def evaluate(self,value):
		if value[2]>=F_max and self.go==True:
			self.cycle+=1
			self.go=False
		if value[2]<=F_min and self.go==False:
			self.go=True
		return self.cycle

class condition_cycle_bool(modules.links.Condition):
	def __init__(self,n=1):
		self.cycle=0
		self.go=True
		self.n=n
		
	def evaluate(self,value):
		if value[2]>=F_max and self.go==True:
			self.cycle+=1
			self.go=False
			if self.cycle%self.n==0:
				return True
			else:
				return False
		elif value[2]<=F_min and self.go==False:
			self.go=True
			if self.cycle%self.n==0:
				return True
			else:
				return False
		else:
			return False


class condition_camera(modules.links.Condition):
	def __init__(self,n=1):
		self.cycle=0
		self.n=n
		
	def evaluate(self,value):
		if self.cycle%self.n==0:
			#print self.cycle
			self.cycle+=1
			return value 
		else:
			#print self.cycle
			self.cycle+=1
			return None
		#self.cycle+=1
		


#############################################################################



#class condition_cycle_old(object):
	#def __init__(self):
		#self.cycle=0
		#self.go=True
		
	#def evaluate(self,value):
		#if value[2]>=F_max and self.go==True:
			#self.cycle+=1
			#self.go=False
		#if value[2]<=F_min and self.go==False:
			#self.go=True
		#bool_condition=True
		#ret_value=self.cycle
		#return (bool_condition,ret_value)

#class condition_cycle_bool_old(object):
	#def __init__(self,n=1):
		#self.cycle=0
		#self.go=True
		#self.n=n
		
	#def evaluate(self,value):
		##print value
		#if value[2]>=F_max and self.go==True:
			#self.cycle+=1
			#self.go=False
			#if self.cycle%self.n==0:
				##print "frame!"
				#return (True,True)
			#else:
				#return (False,False)
		#elif value[2]<=F_min and self.go==False:
			#self.go=True
			#if self.cycle%self.n==0:
				#return (True,True)
			#else:
				#return (False,False)
		#else:
			#return (False, False)

F_max=3.1e-5
F_min=2.9e-5
t0=time.time()
try:
########################################### Creating objects
	
	#instronSensor=modules.sensor.ComediSensor(channels=[0,1,2])
	#cameraSensor=modules.technical.Ximea
	#agilentSensor=modules.sensor.Agilent34420ASensor()

########################################### Creating blocks
	
	stream=modules.blocks.PathGenerator(t0,send_freq=1000,actuator=None,waveform="triangle",freq=1,cycles=None,amplitude=1,offset=0,phase=0,init=0)
	#camera=modules.blocks.StreamerCamera(Ximea,freq=None,save=False,save_directory="./images_fissuration/")
	#resistance=modules.blocks.MeasureAgilent34420A(t0,agilentSensor)
	compacter=modules.blocks.Compacter(500)
	#compacter_resistance=modules.blocks.Compacter(10)
	#save=modules.blocks.Saver("/home/corentin/Bureau/t_F_dep_cycle.txt")
	save=modules.blocks.Saver("/home/corentin/Bureau/t_path.txt")
	graph=modules.blocks.Grapher("static",(0,1))
	#graph2=modules.blocks.Grapher("static",(0,1),(0,2),(0,3))
	#graph_resistance=modules.blocks.Grapher("dynamic",(0,1))
	#cameraDisplay=modules.blocks.CameraDisplayer()
	
########################################### Creating links
	
	link1=modules.links.Link()
	link2=modules.links.Link()
	link3=modules.links.Link()
	#link4=modules.links.Link(condition=condition_cycle_bool())
	#link5=modules.links.Link(condition=condition_cycle_bool(n=5))
	#link6=modules.links.Link()
	#link7=modules.links.Link()
	#link8=modules.links.Link()
	#link9=modules.links.Link(condition=condition_cycle())
	#link10=modules.links.Link(condition=condition_cycle())
	
########################################### Linking objects
	stream.add_output(link1)
	#stream.add_output(link3)
	#stream.add_output(link5)
	#stream.add_output(link9)
	#stream.add_output(link10)
	
	#camera.add_output(link1)
	#resistance.add_input(link4)
	#resistance.add_output(link6)
	compacter.add_input(link1)
	#compacter.add_input(link3)
	compacter.add_output(link2)
	compacter.add_output(link3)
	#compacter.add_output(link7)
	
	#cameraDisplay.add_input(link1)
	
	#compacter_resistance.add_input(link10)
	#compacter_resistance.add_input(link6)
	#compacter_resistance.add_output(link7)
	#compacter_resistance.add_output(link8)
	
	save.add_input(link3)
	#save_resistance.add_input(link8)
	graph.add_input(link2)
	#graph2.add_input(link6)
	#graph_resistance.add_input(link7)
	
########################################### Starting objects

	for instance in modules.blocks.MasterBlock.instances:
		instance.start()

########################################### Waiting for execution
	time.sleep(1)
	time.sleep(100)

########################################### Stopping objects

	for instance in modules.blocks.MasterBlock.instances:
		instance.stop()

except KeyboardInterrupt:
	for instance in modules.blocks.MasterBlock.instances:
		instance.stop()