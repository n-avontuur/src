#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from flexbe_core import EventState, Logger

class setFirstTimePart(EventState):
	'''


	'''

	def __init__(self):
		super(setFirstTimePart,self).__init__(outcomes = ['continue', 'failed'], output_keys = ['gasket','piston','gear'])


	def execute(self, userdata):
		userdata.gasket=[(0,0,0),(0.15,0.10,0.035),(0),(4,3)]
		userdata.piston=[(0,0,0),(0.11,0.11,0.020),(0),(3,3)]
		userdata.gear=[(0,0,0),(0.13,0.10,0.025),(0),(3,2)]
		Logger.loginfo(userdata.gasket)
		Logger.loginfo(userdata.piston)
		Logger.loginfo(userdata.gear)
		return 'continue'

	def on_enter(self, userdata):
		pass

	def on_exit(self, userdata):
		pass

	def on_start(self):
		pass


	def on_stop(self):
		pass
