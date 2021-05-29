#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.vacuum_gripper_control_state import VacuumGripperControlState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sat May 29 2021
@author: niels avontuur
'''
class initGripperSM(Behavior):
	'''
	Grippers aan uit zetten voor het gebruik
	'''


	def __init__(self):
		super(initGripperSM, self).__init__()
		self.name = 'initGripper'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:693 y:71, x:130 y:275
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.gripper1_service_name = "/ariac/arm1/gripper/control"
		_state_machine.userdata.gripper2_service_name = "/ariac/arm2/gripper/control"

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:120 y:40
			OperatableStateMachine.add('gripperON',
										VacuumGripperControlState(enable=True),
										transitions={'continue': 'gripperON_2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'service_name': 'gripper1_service_name'})

			# x:404 y:44
			OperatableStateMachine.add('gripperON_2',
										VacuumGripperControlState(enable=False),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'service_name': 'gripper1_service_name'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
