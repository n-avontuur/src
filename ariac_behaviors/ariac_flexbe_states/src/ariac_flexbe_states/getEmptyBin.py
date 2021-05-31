#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from flexbe_core import EventState, Logger

class getEmptyBin(EventState):
	'''
	State for know witch bin is empty

	># binPartType 		string[] 	array for all content in bins 
	#> bin 			string		name of empty bin
	#> bin_frame 		string		name frame of empty bin

	'''

	def __init__(self):
		super(getEmptyBin,self).__init__(input_keys = ['binPartType'],outcomes = ['continue', 'failed'], output_keys = ['bin','bin_frame','robot_name'])


	def execute(self, userdata):
		try :
			for i in range(len(userdata.binPartType)):
				if userdata.binPartType[i] == 'empty' or  userdata.binPartType[i] == 'Empty':
					i = i + 1
					userdata.bin = 'bin'+ str(i)
					userdata.bin_frame = 'bin'+ str(i) + '_frame'
					if i > 1 and i < 3:
						userdata.robot_name='R1'
					if i > 3 and i < 6:
						userdata.robot_name='R2'
					Logger.loginfo('Empty bin :'+ userdata.bin)
					return 'continue'
		except :
			Logger.logwarn("An exception occurred")
			return 'failed'

	def on_enter(self, userdata):
		self._binPartType = ['','']
		self._binPartType = userdata.binPartType
		pass

	def on_exit(self, userdata):
		pass

	def on_start(self):
		pass


	def on_stop(self):
		pass
