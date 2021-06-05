#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from flexbe_core import EventState, Logger

class getBinFrame(EventState):
	'''


	'''

	def __init__(self):
		super(getBinFrame,self).__init__(input_keys=['bin'],outcomes = ['continue'], output_keys = ['bin_frame'])


	def execute(self, userdata):
		userdata.bin_frame = userdata.bin + '_frame'
		return 'continue'

	def on_enter(self, userdata):
		pass

	def on_exit(self, userdata):
		pass

	def on_start(self):
		pass


	def on_stop(self):
		pass


