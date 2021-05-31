#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from flexbe_core import EventState, Logger


class set_new_pose_part(EventState):
	'''
	this state sets the new pose for the part

	'''

	def __init__(self):
		super(set_new_pose_part,self).__init__(input_keys = ['part_offset','offsetSizeX','offsetSizeY','offsetSizeZ','NumOfParts'],outcomes = ['continue', 'failed'], output_keys = ['part_offset'])


	def execute(self, userdata):
		
		if self._offset_Y==0 and self._offset_X==0:
			self._offset_Y-=self._offsetSize_x
			self._offset_X-=self._offsetSize_y
			pass
		if self._offset_X<0.3:
			self._offset_X+=self._offsetSize_x
			pass
		if self._offset_X==0.3:
			self._offset_Y+=self._offsetSize_y
		return 'continue'
		

	def on_enter(self, userdata):
		self._offset_X=userdata.part_offset(0)
		self._offset_Y=userdata.part_offset(1)
		self._offsetSize_x=userdata.offsetSizeX
		self._offsetSize_y=userdata.offsetSizeY
		self._offsetSize_z=userdata.offsetSizeZ
		pass

	def on_exit(self, userdata):
		userdata.part_offset(0)=self._offset_X
		userdata.part_offset(1)=self._offset_Y
		userdata.part_offset(2)=self._offsetSize_x
		userdata.part_offset(3)=self._offsetSize_y
		userdata.part_offset(4)=self._offsetSize_z
		pass

	def on_start(self):
		pass


	def on_stop(self):
		pass

# if userdata.arm1_status=='piston_rod_part_red' or userdata.arm2_status=='piston_rod_part_red':	

# elif userdata.arm2_status=='gasket_part_blue' or userdata.arm2_status=='gasket_part_blue':
# 			offset_X=userdata.gasket_part_blueX
# 			offset_Y=userdata.gasket_part_blueY
# 			if offset_Y==0 and offset_X==0:
# 				offset_Y-=0.3
# 				offset_X-=0.3
# 				pass
# 			if offset_X<0.3:
# 				offset_X+=0.15
# 				pass
# 			if offset_X==0.3:
# 				offset_Y+=0.15
# 			userdata.gasket_part_blueX=offset_X
# 			userdata.gasket_part_blueY=offset_Y