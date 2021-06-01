#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from flexbe_core import EventState, Logger

class set_Robot_Parameters(EventState):
	'''
	State for know witch bin is empty

	># binPartType 		string[] 	array for all content in bins 
	#> bin 			string		name of empty bin
	#> bin_frame 		string		name frame of empty bin

	'''

	def __init__(self):
		super(set_Robot_Parameters,self).__init__(input_keys = ['robot_Name'],outcomes = ['continue', 'failed'], output_keys = ['move_group','action_topic_namespace','action_topic','robot_name','tool_link','gripper_service','gripper_status_topic','gripper_status_attached','gripper_status_enabled','PrePick_config'])


	def execute(self, userdata):
		if userdata.robot_Name == 'arm1':
			userdata.move_group = 'Manipulator'
			userdata.action_topic_namespace = '/ariac/arm1'
			userdata.action_topic = '/move_group'
			userdata.robot_name = 'arm1'
			userdata.tool_link = 'ee_link'
			userdata.gripper_service = '/ariac/arm1/gripper/control'
			userdata.gripper_status_topic = '/ariac/arm1/gripper/state'
			userdata.PrePick_config = 'homeR1'
		elif userdata.robot_Name == 'arm2':
			userdata.move_group = 'Manipulator'
			userdata.action_topic_namespace = '/ariac/arm2'
			userdata.action_topic = '/move_group'
			userdata.robot_name = 'arm2'
			userdata.tool_link = 'ee_link'
			userdata.gripper_service = '/ariac/arm2/gripper/control'
			userdata.gripper_status_topic = '/ariac/arm2/gripper/state'
			userdata.PrePick_config = 'homeR2'
		return 'continue'


	def on_enter(self, userdata):
		pass

	def on_exit(self, userdata):

		pass

	def on_start(self):
		pass


	def on_stop(self):
		pass
