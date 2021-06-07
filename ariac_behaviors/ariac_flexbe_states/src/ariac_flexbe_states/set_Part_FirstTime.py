#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from flexbe_core import EventState, Logger

class setFirstTimePart(EventState):
	'''


	'''

	def __init__(self):
		super(setFirstTimePart,self).__init__(outcomes = ['continue', 'failed'], output_keys = ['gasket','piston','gear','bin_Content'])


	def execute(self, userdata):
		gasket_offset=[[-0.15,00.15],[-0.15,-0.15]],[[00.00,00.15],[00.00,-0.15]],[[00.15,00.15],[00.15,-0.15]]
		piston_offset=[[-0.175,00.175],[-0.175,-0.175]],[[0.175,0.175],[0.175,-0.175]]
		gear_offset=[[-0.465,00.20],[-0.465,00.00],[-0.465,-0.20]],[[00.465,00.20],[00.465,00.00],[00.465,-0.20]]
		userdata.gasket=[[gasket_offset],[0.035],[0],[2,3]] #offsetXY,offsetZ,numberParts,matrixXY
		userdata.piston=[[piston_offset],[0.025],[0],[2,2]] #offsetXY,offsetZ,numberParts,matrixXY
		userdata.gear=[[gear_offset],[0.035],[0],[2,3]]	#offsetXY,offsetZ,numberParts,matrixXY
		self._content = ['empty','x']
		
		return 'continue'

	def on_enter(self, userdata):
		pass

	def on_exit(self, userdata):
		userdata.bin_Content=[self._content,self._content,self._content,self._content,self._content,self._content]
		pass

	def on_start(self):
		pass


	def on_stop(self):
		pass


