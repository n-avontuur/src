#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from flexbe_core import EventState, Logger

class selectRobot(EventState):
	'''
	State for know witch bin is empty

	># binPartType 		string[] 	array for all content in bins 
	#> bin 			string		name of empty bin
	#> bin_frame 		string		name frame of empty bin

	'''

	def __init__(self):
		super(selectRobot,self).__init__(input_keys = ['bin'],outcomes = ['continue', 'failed'], output_keys = ['robot_Name'])


	def execute(self, userdata):
		if userdata.bin == "bin6":
			userdata.robot_Name='arm1'
		elif userdata.bin == "bin5":
			userdata.robot_Name='arm1'
		elif userdata.bin == "bin4":
			userdata.robot_Name='arm1'
		elif userdata.bin == "bin3":
			userdata.robot_Name='arm2'
		elif userdata.bin == "bin2":
			userdata.robot_Name='arm2'
		elif userdata.bin == "bin1":
			userdata.robot_Name='arm2'
		return 'continue'

	def on_enter(self, userdata):
		pass

	def on_exit(self, userdata):
		pass

	def on_start(self):
		pass


	def on_stop(self):
		pass
