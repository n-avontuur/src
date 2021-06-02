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
		super(testList,self).__init__(input_keys = ['part_Content'],outcomes = ['continue', 'failed','bin_Full'], output_keys = ['part_Content','pose_offset'])

	def on_enter(self, userdata):
		try:
			offset=userdata.part_Content[0]
			self._offset_x=offset[0]
			self._offset_y=offset[1]
			self._offset_z=offset[2]
		except:
			Logger.logwarn('offset not correct' )

		try:
			offsetSize=userdata.part_Content[1]
			self._offsetSize_x=offsetSize[0]
			self._offsetSize_y=offsetSize[1]
			self._offsetSize_z=offsetSize[2]
		except:
			Logger.logwarn('offsetSize not correct')

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
		max_X=self._maxNumberPartsX
		max_Y=self._maxNumberPartsY
		max_parts=max_Y*max_X
		col=[]
		row=[]
		j=0
		Logger.loginfo("maxXnumer:"+str(max_X))
		Logger.loginfo("maxYnumer:"+str(max_Y))
		Logger.loginfo("Number of part :"+ str(self._numberParts))
		if (self._numberParts == max_parts):
			self._numberParts = 0
			return 'bin_Full'
		for i in range(max_Y):
			while j < max_X:
				new = j+1
				col.append(new)
				j+=1
				Logger.logwarn('New j')
			Logger.logwarn('New i')
			row.append(col)
			liststr = ' '.join([str(elem) for elem in row])
			Logger.loginfo('col:'+liststr)
		Logger.loginfo('j:'+str(j))
		Logger.loginfo('i:'+str(i))
		liststr = ' '.join([str(elem) for elem in row])
		Logger.loginfo('row:'+liststr)

		try:
			for p,row in enumerate(row):
				value=self._numberParts
				for value in row:
					p+1
					row.index(value)
				x=p-1
				y=row.index(value)-1
				Logger.loginfo(str('col'+x))
				Logger.loginfo(str('row'+y))
		except:
			Logger.logwarn('Looking true the matrix went wrong')
		try:
			if x==0 and y==0:
				self._offset_y-=self._offsetSize_x
				self._offset_x-=self._offsetSize_y
				pass
			if x<max_X:
				self._offset_x+=self._offsetSize_x
				pass
			if x==max_X:
				self._offset_y+=self._offsetSize_y
		except:
			Logger.logwarn('Error in setting new offset')
		Logger.logwarn("end of state")
		return 'continue'

	def on_exit(self, userdata):
		offset = [self._offset_x,self._offset_y,self._offset_z]
		offsetSize = [self._offsetSize_x,self._offsetSize_y,self._offsetSize_z]
		numberParts=self._numberParts
		maxNumber=[self._maxNumberPartsX,self._maxNumberPartsY]
		userdata.part_Content=[offset,offsetSize,numberParts,maxNumber]		
		pass

	def on_start(self):
		pass


	def on_stop(self):
		pass
