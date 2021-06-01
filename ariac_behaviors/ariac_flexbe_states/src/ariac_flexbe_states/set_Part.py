#!/usr/bin/env python
import copy
import rospy
from std_msgs.msg import String
from flexbe_core import EventState, Logger

class setPart(EventState):
	'''
	State for know witch bin is empty

	># binPartType 		string[] 	array for all content in bins 
	#> bin 			string		name of empty bin
	#> bin_frame 		string		name frame of empty bin

	'''

	def __init__(self):
		super(setPart,self).__init__(input_keys = ['part_Type','gasket','piston','gear'],outcomes = ['continue', 'failed'], output_keys = ['part'])


	def execute(self, userdata):
		if self._part_Type == 'gasket_part':
			userdata.part=copy.deepcopy(userdata.gasket)
		elif self._part_Type == 'piston_rod_part':
			userdata.part=copy.deepcopy(userdata.piston)
		elif self._part_Type == 'gear_part':
			userdata.part=copy.deepcopy(userdata.gear)
		else :
			Logger.logwarn("part_Type didn't match")
			return 'failed'
		return 'continue'

	def on_enter(self, userdata):
		self._part_Type= userdata.part_Type
		pass

	def on_exit(self, userdata):
		pass

	def on_start(self):
		pass


	def on_stop(self):
		pass
