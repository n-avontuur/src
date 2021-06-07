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
		if userdata.bin == "bin1":
			self._content[0]=['used',self._part]
		if userdata.bin == "bin2" :
			self._content[1]=['used',self._part]
		if userdata.bin == "bin3":
			self._content[2]=['used',self._part]
		if userdata.bin == "bin4":
			self._content[3]=['used',self._part]
		if userdata.bin == "bin5":
			self._content[4]=['used',self._part]
		elif userdata.bin == "bin6":
			self._content[5]=['used',self._part]
		liststr = ' '.join([str(elem) for elem in self._content])
		Logger.loginfo('set List content bin: '+liststr)
		return 'continue'

	def on_enter(self, userdata):
		self._part = userdata.part_Type
		self._content = userdata.bin_Content
		pass

	def on_exit(self, userdata):
		userdata.bin_Content = self._content
		pass

	def on_start(self):
		pass


	def on_stop(self):
		pass
