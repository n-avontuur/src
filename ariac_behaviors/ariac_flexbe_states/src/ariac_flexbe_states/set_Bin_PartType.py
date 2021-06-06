#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from flexbe_core import EventState, Logger


class setBinPartType(EventState):
	'''
	this state sets the new pose for the part

	># bin string name of bin
	># part string name of part
	#> binPartType string[] list of the content of bins

	'''

	def __init__(self):
		super(setBinPartType,self).__init__(input_keys = ["bin","part_Type","bin_Content" ],outcomes = ['continue'], output_keys = ['bin_Content'])


	def execute(self, userdata):
		if userdata.bin == "bin1" and userdata.bin_Content[0][0]=="empty":
			userdata.bin_Content[0][0]='used'
			userdata.bin_Content[0][1]=self._part
		elif userdata.bin == "bin2" and userdata.bin_Content[1][0]=="empty":
			userdata.bin_Content[1][0]='used'
			userdata.bin_Content[1][1]=self._part
		elif userdata.bin == "bin3" and userdata.bin_Content[2][0]=="empty":
			userdata.bin_Content[2][0]='used'
			userdata.bin_Content[2][1]=self._part
		elif userdata.bin == "bin4" and userdata.bin_Content[3][0]=="empty":
			userdata.bin_Content[3][0]='used'
			userdata.bin_Content[3][1]=self._part
		elif userdata.bin == "bin5" and userdata.bin_Content[4][0]=="empty":
			userdata.bin_Content[4][0]='used'
			userdata.bin_Content[4][1]=self._part
		elif userdata.bin == "bin6" and userdata.bin_Content[5][0]=="empty":
			userdata.bin_Content[5][0]='used'
			userdata.bin_Content[5][1]=self._part
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
