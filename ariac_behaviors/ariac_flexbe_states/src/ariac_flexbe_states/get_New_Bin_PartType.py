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
		super(getNewBinPartType,self).__init__(input_keys = ['bin',"part_Type","bin_Content" ],outcomes = ['continue', "findEmptyBin"], output_keys = ['bin','bin_frame'])


	def execute(self, userdata):
		if userdata.bin == 'bin1':
			i = 1
		elif userdata.bin == 'bin2':
			i = 2
		elif userdata.bin == 'bin3':
			i = 3
		elif userdata.bin == 'bin4':
			i = 4
		elif userdata.bin == 'bin5':
			i = 5
		elif userdata.bin == 'bin6':
			Logger.loginfo('look for empty bin')
			return "findEmptyBin"

		while i < 6:
			self._binUsed=userdata.bin_Content[i]
			if self._binUsed[0]=="used" and self._binUsed[1]==self._part:
				i = i + 1
				userdata.bin = ('bin'+ str(i))
				userdata.bin_frame = ('bin'+ str(i) + '_frame')
				Logger.loginfo('New Bin selected')
				return 'continue'
			else :
				i= i+1
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
