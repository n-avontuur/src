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
		super(getEmptyBin,self).__init__(input_keys = ['bin_Content'],outcomes = ['continue', 'failed','system_Full'], output_keys = ['bin','bin_frame'])


	def execute(self, userdata):
		liststr = ' '.join([str(elem) for elem in userdata.bin_Content])
		Logger.loginfo('bin Content: '+liststr)
		try :
			for i in range(len(userdata.bin_Content)):
				bin_content = userdata.bin_Content[i]
				if bin_content[0] == 'empty' or  bin_content[0] == 'Empty':
					i = i + 1
					userdata.bin = 'bin'+ str(i)
					userdata.bin_frame = 'bin'+ str(i) + '_frame'
					Logger.loginfo('Empty bin :'+ userdata.bin)
					return 'continue'
		except :
			Logger.logwarn("An exception occurred")
			return 'failed'

	def on_enter(self, userdata):
		pass

	def on_exit(self, userdata):
		pass

	def on_start(self):
		pass


	def on_stop(self):
		pass
