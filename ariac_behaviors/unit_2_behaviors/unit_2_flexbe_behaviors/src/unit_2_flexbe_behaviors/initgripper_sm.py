#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.get_vacuum_gripper_status_state import GetVacuumGripperStatusState
from ariac_flexbe_states.vacuum_gripper_control_state import VacuumGripperControlState
from ariac_support_flexbe_states.equal_state import EqualState
from flexbe_states.wait_state import WaitState
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
		# x:1290 y:737, x:594 y:252
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.gripper1_service_name = "/ariac/arm1/gripper/control"
		_state_machine.userdata.gripper2_service_name = "/ariac/arm2/gripper/control"
		_state_machine.userdata.gripper1_status_topic = '/ariac/arm1/gripper/state'
		_state_machine.userdata.gripper2_status_topic = '/ariac/arm1/gripper/state'
		_state_machine.userdata.falseVariable = False

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:120 y:40
			OperatableStateMachine.add('gripperON',
										VacuumGripperControlState(enable=True),
										transitions={'continue': 'wait', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'service_name': 'gripper1_service_name'})

			# x:1145 y:498
			OperatableStateMachine.add('checkNothingAttached_2',
										EqualState(),
										transitions={'true': 'finished', 'false': 'gripperON_2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'falseVariable', 'value_b': 'attached'})

			# x:880 y:52
			OperatableStateMachine.add('getGripper1Status',
										GetVacuumGripperStatusState(),
										transitions={'continue': 'checkNothingAttached', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'topic_name': 'gripper1_status_topic', 'enabled': 'enabled', 'attached': 'attached'})

			# x:956 y:512
			OperatableStateMachine.add('getGripper2Status',
										GetVacuumGripperStatusState(),
										transitions={'continue': 'checkNothingAttached_2', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'topic_name': 'gripper2_status_topic', 'enabled': 'enabled', 'attached': 'attached'})

			# x:514 y:44
			OperatableStateMachine.add('gripperOFF',
										VacuumGripperControlState(enable=False),
										transitions={'continue': 'wait_3', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'service_name': 'gripper1_service_name'})

			# x:555 y:512
			OperatableStateMachine.add('gripperOFF_2',
										VacuumGripperControlState(enable=False),
										transitions={'continue': 'wait_4', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'service_name': 'gripper2_service_name'})

			# x:102 y:504
			OperatableStateMachine.add('gripperON_2',
										VacuumGripperControlState(enable=True),
										transitions={'continue': 'wait_2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'service_name': 'gripper2_service_name'})

			# x:348 y:31
			OperatableStateMachine.add('wait',
										WaitState(wait_time=0.1),
										transitions={'done': 'gripperOFF'},
										autonomy={'done': Autonomy.Off})

			# x:376 y:514
			OperatableStateMachine.add('wait_2',
										WaitState(wait_time=0.1),
										transitions={'done': 'gripperOFF_2'},
										autonomy={'done': Autonomy.Off})

			# x:736 y:37
			OperatableStateMachine.add('wait_3',
										WaitState(wait_time=0.5),
										transitions={'done': 'getGripper1Status'},
										autonomy={'done': Autonomy.Off})

			# x:795 y:521
			OperatableStateMachine.add('wait_4',
										WaitState(wait_time=0.5),
										transitions={'done': 'getGripper2Status'},
										autonomy={'done': Autonomy.Off})

			# x:1087 y:45
			OperatableStateMachine.add('checkNothingAttached',
										EqualState(),
										transitions={'true': 'gripperON_2', 'false': 'gripperON'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'falseVariable', 'value_b': 'attached'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
