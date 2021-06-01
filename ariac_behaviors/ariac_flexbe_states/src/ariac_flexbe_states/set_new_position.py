#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from flexbe_core import EventState, Logger


class setNewPosePart(EventState):
	'''
	this state sets the new pose for the part

	'''

	def __init__(self):
		super(setNewPosePart,self).__init__(input_keys = ['part_Content'],outcomes = ['continue', 'failed','bin_Full'], output_keys = ['part_Content','pose_offset'])

	def on_enter(self, userdata):
		self._offset_x=userdata.part_Content[0][0]
		self._offset_y=userdata.part_Content[0][1]
		self._offset_z=userdata.part_Content[0][2]
		self._numberParts=userdata.part_Content[0][0]
		self._maxNumberPartsX=userdata.part_Content[0][0]
		self._maxNumberPartsY=userdata.part_Content[0][1]
		self._offsetSize_x=userdata.part_Content[0][0]
		self._offsetSize_y=userdata.part_Content[0][1]
		self._offsetSize_z=userdata.part_Content[0][2]
		pass


	def execute(self, userdata):
		matrix =[self._maxNumberPartsX][self._maxNumberPartsY]
		if (self._numberParts+1) ==  (self._maxNumberPartsX * self._maxNumberPartsY):
			self._numberParts = 0
			return 'bin_Full'
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

	def on_exit(self, userdata):
		userdata.part_Content[0][0]=self._offset_x
		userdata.part_Content[0][1]=self._offset_y
		userdata.part_Content[0][2]=self._offset_z
		userdata.part_Content[1][0]=self._numberParts
		userdata.part_Content[2][0]=self._maxNumberPartsX
		userdata.part_Content[2][1]=self._maxNumberPartsY
		userdata.part_Content[3][0]=self._offsetSize_x
		userdata.part_Content[3][1]=self._offsetSize_y
		userdata.part_Content[3][2]=self._offsetSize_z
		userdata.pose = [self._offset_x, self._offset_y, self._offset_z]
		Logger.loginfo('pose: ' + userdata.pose)
		pass

	def on_start(self):
		pass


	def on_stop(self):
		pass
