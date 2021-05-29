#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from flexbe_core import EventState, Logger


class setBinPartType(EventState):
	'''
	this state sets the new pose for the part

	'''

	def __init__(self):
		super(setBinPartType,self).__init__(input_keys = ["bin","part" ],outcomes = ['continue', 'failed'], output_keys = ['bin1PartType','bin2PartType','bin3PartType','bin4PartType','bin5PartType','bin6PartType'])


	def execute(self, userdata):
		if userdata.bin == "bin1":
            userdata.bin1PartType=userdata.part
		else if userdata.bin == "bin2":
            userdata.bin2PartType=userdata.part
        else if userdata.bin == "bin3":
            userdata.bin3PartType=userdata.part
        else if userdata.bin == "bin4":
            userdata.bin4PartType=userdata.part
        else if userdata.bin == "bin5":
            userdata.bin5PartType=userdata.part
        else if userdata.bin == "bin6":
            userdata.bin6PartType=userdata.part

        return 'continue'

	def on_enter(self, userdata):
		pass

	def on_exit(self, userdata):
		pass

	def on_start(self):
		pass


	def on_stop(self):
		pass
