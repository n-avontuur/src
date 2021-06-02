#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.set_Part import setPart
from ariac_flexbe_states.set_Part_FirstTime import setFirstTimePart
from ariac_flexbe_states.test_list import testList
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Tue Jun 01 2021
@author: Niels Avontuur
'''
class Test_listSM(Behavior):
	'''
	testing how to use list
	'''


	def __init__(self):
		super(Test_listSM, self).__init__()
		self.name = 'Test_list'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:818 y:46, x:130 y:365
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.part_Content = []
		_state_machine.userdata.part_Type = 'gasket_part'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:63 y:39
			OperatableStateMachine.add('setFirstTimePart',
										setFirstTimePart(),
										transitions={'continue': 'setPart', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'gasket': 'gasket', 'piston': 'piston', 'gear': 'gear'})

			# x:267 y:44
			OperatableStateMachine.add('setPart',
										setPart(),
										transitions={'continue': 'testList', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'part_Type': 'part_Type', 'gasket': 'gasket', 'piston': 'piston', 'gear': 'gear', 'part_Content': 'part_Content'})

			# x:488 y:45
			OperatableStateMachine.add('testList',
										testList(),
										transitions={'continue': 'finished', 'failed': 'failed', 'bin_Full': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'bin_Full': Autonomy.Off},
										remapping={'part_Content': 'part_Content', 'pose_offset': 'pose_offset'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
