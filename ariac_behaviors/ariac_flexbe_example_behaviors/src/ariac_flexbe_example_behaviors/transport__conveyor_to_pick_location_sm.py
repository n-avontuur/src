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
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu May 27 2021
@author: niels avontuur
'''
class transport_conveyor_to_pick_locationSM(Behavior):
	'''
	Locating the parts of the transport-conveyor
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
		# x:1011 y:36, x:370 y:245
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.ConveyorON = 100
		_state_machine.userdata.ConveyorOFF = 0
		_state_machine.userdata.BreakbeamTopic = "/ariac/break_beam_1"

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:106 y:29
			OperatableStateMachine.add('Start_Conveyor',
										SetConveyorbeltPowerState(),
										transitions={'continue': 'Detect_Part_arrived', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'power': 'ConveyorON'})

			# x:696 y:27
			OperatableStateMachine.add('Stop_Conveyor',
										SetConveyorbeltPowerState(),
										transitions={'continue': 'finished', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'power': 'ConveyorOFF'})

			# x:388 y:35
			OperatableStateMachine.add('Detect_Part_arrived',
										DetectBreakBeamState(),
										transitions={'continue': 'Stop_Conveyor', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'topic': 'BreakbeamTopic', 'object_detected': 'object_detected'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
