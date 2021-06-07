#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from flexbe_core import EventState, Logger


class getNewBinPartType(EventState):
	'''
	this state sets the new pose for the part

	># bin string name of bin
	># part string name of part
	#> binPartType string[] list of the content of bins

	'''

	def __init__(self):
		super(getNewBinPartType,self).__init__(input_keys = ['bin',"part_Type","bin_Content" ],outcomes = ['continue', "findEmptyBin",'system_Full'], output_keys = ['bin','bin_frame'])


	def execute(self, userdata):
		x=0
		i=0
		while i < 6:
			if userdata.bin_Content[i] == ["used",self._part]:
				i = i+ 1
				userdata.bin = ('bin'+ str(i))
				userdata.bin_frame = ('bin'+ str(i) + '_frame')
				Logger.loginfo("new bin found :" + userdata.bin)
				return 'continue'
			if userdata.bin_Content[i] == ["full",self._part]:
				x +=1
				Logger.loginfo('fulbin bin :'+ str(i))
				if x == 6:
					return 'system_Full'
				i = i+ 1
			else :
				i = i+ 1
		return 'findEmptyBin'
	def on_enter(self, userdata):
		self._part = userdata.part_Type
		pass

	def on_exit(self, userdata):

		pass

	def on_start(self):
		pass


	def on_stop(self):
		pass
