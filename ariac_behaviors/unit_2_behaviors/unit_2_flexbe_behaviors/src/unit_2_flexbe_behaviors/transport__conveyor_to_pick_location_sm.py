#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.detect_break_beam_state import DetectBreakBeamState
from ariac_flexbe_states.set_conveyorbelt_power_state import SetConveyorbeltPowerState
from ariac_flexbe_states.start_assignment_state import StartAssignment
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
		# x:1363 y:79, x:578 y:357
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.powerOFF = 0
		_state_machine.userdata.powerON = 100
		_state_machine.userdata.breakbeam = "/ariac/break_beam_1_change"

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:97 y:63
			OperatableStateMachine.add('startAssignment',
										StartAssignment(),
										transitions={'continue': 'conveyorON'},
										autonomy={'continue': Autonomy.Off})

			# x:301 y:62
			OperatableStateMachine.add('conveyorON',
										SetConveyorbeltPowerState(),
										transitions={'continue': 'partDetectByBreakbeam', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'power': 'powerON'})

			# x:577 y:65
			OperatableStateMachine.add('partDetectByBreakbeam',
										DetectBreakBeamState(),
										transitions={'continue': 'conveyorOFF', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'topic': 'breakbeam', 'object_detected': 'object_detected'})

			# x:828 y:69
			OperatableStateMachine.add('conveyorOFF',
										SetConveyorbeltPowerState(),
										transitions={'continue': 'finished', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'power': 'powerOFF'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
