#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from flexbe_core import EventState, Logger


class set_new_pose_part(EventState):
	'''
	this state sets the new pose for the part

	'''

	def __init__(self):
		super(set_new_pose_part,self).__init__(input_keys = ['piston_rod_part_redX', 'piston_rod_part_redY','gasket_part_blueX','gasket_part_blueY'  ],outcomes = ['continue', 'failed'], output_keys = [ 'piston_rod_part_redX', 'piston_rod_part_redY','gasket_part_blueX','gasket_part_blueY'])


	def execute(self, userdata):
		if userdata.arm1_status=='piston_rod_part_red' or userdata.arm2_status=='piston_rod_part_red':
			offset_X=userdata.piston_rod_part_redX
			offset_Y=userdata.piston_rod_part_redY
			if offset_Y==0 and offset_X==0:
				offset_Y-=0.3
				offset_X-=0.3
				pass
			if offset_X<0.3:
				offset_X+=0.15
				pass
			if offset_X==0.3:
				offset_Y+=0.15
			userdata.piston_rod_part_redX=offset_X
			userdata.piston_rod_part_redY=offset_Y
		elif userdata.arm2_status=='gasket_part_blue' or userdata.arm2_status=='gasket_part_blue':
			offset_X=userdata.gasket_part_blueX
			offset_Y=userdata.gasket_part_blueY
			if offset_Y==0 and offset_X==0:
				offset_Y-=0.3
				offset_X-=0.3
				pass
			if offset_X<0.3:
				offset_X+=0.15
				pass
			if offset_X==0.3:
				offset_Y+=0.15
			userdata.gasket_part_blueX=offset_X
			userdata.gasket_part_blueY=offset_Y
		return 'continue'

	def on_enter(self, userdata):
		pass

	def on_exit(self, userdata):
		pass

	def on_start(self):
		pass


	def on_stop(self):
		pass
