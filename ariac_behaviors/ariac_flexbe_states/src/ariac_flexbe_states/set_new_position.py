#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from flexbe_core import EventState, Logger


class set_new_pose_part(EventState):
	'''
	this state sets the new pose for the part

	'''

	def __init__(self):
		super(set_new_pose_part,self).__init__(input_keys = ['part'],outcomes = ['continue', 'failed'], output_keys = ['part','pose'])


	def execute(self, userdata):
		matrix = [[self._maxNumberPartsX][self._maxNumberPartsX]]
		x,y = matrix(self._numberParts)
		Logger.loginfo('x: ' + x)
		Logger.loginfo('y: ' + y)
		if x==0 and y==0:
			self._offset_y-=self._offsetSize_x
			self._offset_x-=self._offsetSize_y
			pass
		if x<self._maxNumberPartsX:
			self._offset_x+=self._offsetSize_x
			pass
		if x==self._maxNumberPartsX:
			self._offset_y+=self._offsetSize_y
		return 'continue'
		

	def on_enter(self, userdata):
		self._offset_x=userdata.part[0][0]
		self._offset_y=userdata.part[0][1]
		self._offset_z=userdata.part[0][2]
		self._numberParts=userdata.part[1][0]
		self._maxNumberPartsX=userdata.part[2][0]
		self._maxNumberPartsY=userdata.part[2][1]
		self._offsetSize_x=userdata.part[3][0]
		self._offsetSize_y=userdata.part[3][1]
		self._offsetSize_z=userdata.part[3][2]
		pass

	def on_exit(self, userdata):
		userdata.part[0][0]=self._offset_x
		userdata.part[0][1]=self._offset_y
		userdata.part[0][2]=self._offset_z
		userdata.part[1][0]=self._numberParts
		userdata.part[2][0]=self._maxNumberPartsX
		userdata.part[2][1]=self._maxNumberPartsY
		userdata.part[3][0]=self._offsetSize_x
		userdata.part[3][1]=self._offsetSize_y
		userdata.part[3][2]=self._offsetSize_z
		userdata.pose = [self._offset_x, self._offset_y, self._offset_z]
		Logger.loginfo('pose: ' + userdata.pose)
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