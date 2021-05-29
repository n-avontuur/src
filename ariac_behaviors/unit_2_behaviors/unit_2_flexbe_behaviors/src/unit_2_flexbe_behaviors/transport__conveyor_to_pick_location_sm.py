#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.set_conveyorbelt_power_state import SetConveyorbeltPowerState
from ariac_flexbe_states.start_assignment_state import StartAssignment
from flexbe_states.subscriber_state import SubscriberState
from flexbe_states.wait_state import WaitState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu May 27 2021
@author: niels avontuur
'''
class transport_conveyor_to_pick_locationSM(Behavior):
	'''
	For starting conveyor and stopping if part is in the right place
	'''


	def __init__(self):
		super(transport_conveyor_to_pick_locationSM, self).__init__()
		self.name = 'transport_ conveyor_to_pick_location'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		breakbeam = "/ariac/break_beam_1_change"
		# x:1363 y:79, x:578 y:357
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.powerOFF = 0
		_state_machine.userdata.powerON = 100

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:97 y:63
			OperatableStateMachine.add('startAssignment',
										StartAssignment(),
										transitions={'continue': 'conveyorON'},
										autonomy={'continue': Autonomy.Off})

			# x:828 y:69
			OperatableStateMachine.add('conveyorOFF',
										SetConveyorbeltPowerState(),
										transitions={'continue': 'finished', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'power': 'powerOFF'})

			# x:301 y:62
			OperatableStateMachine.add('conveyorON',
										SetConveyorbeltPowerState(),
										transitions={'continue': 'wait', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'power': 'powerON'})

			# x:506 y:51
			OperatableStateMachine.add('wait',
										WaitState(wait_time=0.5),
										transitions={'done': 'checkBreamBeam'},
										autonomy={'done': Autonomy.Off})

			# x:653 y:60
			OperatableStateMachine.add('checkBreamBeam',
										SubscriberState(topic=breakbeam, blocking=True, clear=True),
										transitions={'received': 'conveyorOFF', 'unavailable': 'failed'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
