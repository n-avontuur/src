#!/usr/bin/env python
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
		super(setPart,self).__init__(input_keys = ['partType','gasket','piston','gear'],outcomes = ['continue', 'failed'], output_keys = ['part'])


	def execute(self, userdata):
            if userdata.partType == "gasket_part":
                userdata.part=userdata.gasket
            elif userdata.partType == "piston_part":
                userdata.part=userdata.piston
            elif userdata.partType == "gear_part":
                userdata.part=userdata.gear
            else :
                Logger.logwarn("partType didn't match")
                return 'failed'
            return 'continue'

	def on_enter(self, userdata):
		pass

	def on_exit(self, userdata):
		pass

	def on_start(self):
		pass


	def on_stop(self):
		pass
