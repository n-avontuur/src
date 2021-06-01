#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from flexbe_core import EventState, Logger, logger


class testList(EventState):
	'''
	this state sets the new pose for the part

	'''

	def __init__(self):
		super(testList,self).__init__(input_keys = ['part_Content'],outcomes = ['continue', 'failed','bin_Full'], output_keys = ['part_Content','pose_offset'])

	def on_enter(self, userdata):
		offset=userdata.part_Content[0]
		self._offset_x=offset[0]
		self._offset_y=offset[1]
		self._offset_z=offset[2]

		offsetSize=userdata.part_Content[1]
		self._offsetSize_x=offsetSize[0]
		self._offsetSize_y=offsetSize[1]
		self._offsetSize_z=offsetSize[2]

		numberParts=userdata.part_Content[2]
		self._numberParts=(numberParts)

		maxNumberParts=userdata.part_Content[3]
		self._maxNumberPartsX=maxNumberParts[0]
		self._maxNumberPartsY=maxNumberParts[1]
		
		pass


	def execute(self, userdata):
		max_X=self._maxNumberPartsX
		max_Y=self._maxNumberPartsY
		matrix = [max_X][max_Y]
		if self._numberParts == (max_X * max_Y):
			self._numberParts = 0
			return 'bin_Full'
		x,y = matrix(self._numberParts)
		if x==0 and y==0:
			self._offset_y-=self._offsetSize_x
			self._offset_x-=self._offsetSize_y
			pass
		if x<max_X:
			self._offset_x+=self._offsetSize_x
			pass
		if x==max_X:
			self._offset_y+=self._offsetSize_y
		return 'continue'

	def on_exit(self, userdata):
		offset = [self._offset_x,self._offset_y,self._offset_z]
		userdata.part_Content[0]=offset
		offsetSize = [self._offsetSize_x,self._offsetSize_y,self._offsetSize_z]
		userdata.part_Content[1]=offsetSize
		maxNumber=[self._maxNumberPartsX,self._maxNumberPartsY]
		userdata.part_Content[3]=maxNumber
		pass

	def on_start(self):
		pass


	def on_stop(self):
		pass
