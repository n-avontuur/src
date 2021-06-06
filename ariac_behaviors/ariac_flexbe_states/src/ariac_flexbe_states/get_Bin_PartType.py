#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from flexbe_core import EventState, Logger


class getBinPartType(EventState):
	'''
	this state sets the new pose for the part

	># bin string name of bin
	># part string name of part
	#> binPartType string[] list of the content of bins

	'''

	def __init__(self):
		super(getBinPartType,self).__init__(input_keys = ["part_Type","bin_Content" ],outcomes = ['continue', 'useEmptyBin'], output_keys = ['bin'])


	def execute(self, userdata):
		for i in userdata.bin_Content:
			bin=userdata.bin_Content[i]
			status =bin[0]
			part_Type = bin[1]
			if part_Type == userdata.part_Type:
				userdata.bin = ('bin'+ str(i))
		return 'continue'

	def on_enter(self, userdata):
		self._part = userdata.part_Type
		pass

	def on_exit(self, userdata):
		pass

	def on_start(self):
		pass


	def on_stop(self):
		pass
