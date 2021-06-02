#!/usr/bin/env python
import rospy
from rospy import exceptions
from std_msgs.msg import String
from flexbe_core import EventState, Logger, logger


class testList(EventState):
	'''
	this state sets the new pose for the part

	'''

	def __init__(self):
		super(testList,self).__init__(input_keys = ['part_Content'],outcomes = ['continue', 'failed','bin_Full'], output_keys = ['offset'])

	def on_enter(self, userdata):
		try:
			offset=userdata.part_Content[0]
			self._offset=offset[0]
		except:
			Logger.logwarn('offsetX or Y not correct' )

		try:
			offset_z=userdata.part_Content[1]		
			self._offset_z=offset_z[0]
		except:
			Logger.logwarn('offsetZ not correct')

		try:	
			numberParts=userdata.part_Content[2]
			self._numberParts=numberParts[0]
		except:
			Logger.logwarn('numberparts not correct')

		try:
			maxNumberParts=userdata.part_Content[3]
			self._maxNumberParts=maxNumberParts
			self._maxNumberPartsX=maxNumberParts[0]
			self._maxNumberPartsY=maxNumberParts[1]
		except:
			Logger.logwarn('maxnumberparts not correct')
		pass


	def execute(self, userdata):
		x=0
		y=0
		max_X=self._maxNumberPartsX
		max_Y=self._maxNumberPartsY
		max_parts=max_Y*max_X
		numberOfParts=self._numberParts
		col=[]
		row=[]
		Logger.loginfo("maxXnumer:"+str(max_X))
		Logger.loginfo("maxYnumer:"+str(max_Y))
		Logger.loginfo("Number of part :"+ str(self._numberParts))
		if (self._numberParts == max_parts):
			self._numberParts = 0
			return 'bin_Full'
		matrix= [[0 for _ in range(max_Y)] for _ in range(max_X)]
		for i in range(max_X):
			for j in range(max_Y):
				matrix[i][j] = i*max_Y+j
		liststr = ' '.join([str(elem) for elem in matrix])
		Logger.loginfo('row:'+liststr)
		for i in range(max_X):
			for j in range(max_Y):
				if (numberOfParts == matrix[i][j]):
					x=i
					y=j
					offset=self._offset[i][j]
					liststr = ' '.join([str(elem) for elem in offset])
					Logger.loginfo('offset:'+liststr)
		try:
			self._offset_x=offset[0]
			Logger.loginfo('offsetX'+str(self._offset_x))
			self._offset_y=offset[1]
			Logger.loginfo('offsetY'+str(self._offset_y))
		except:
			Logger.loginfo('X&Y not correct out table')

		return 'continue'

	def on_exit(self, userdata):
		userdata.offset=[self._offset_x,self._offset_y,self._offset_z]
		liststr = ' '.join([str(elem) for elem in userdata.offset])
		Logger.loginfo('offset:'+liststr)
		pass

	def on_start(self):
		pass


	def on_stop(self):
		pass
