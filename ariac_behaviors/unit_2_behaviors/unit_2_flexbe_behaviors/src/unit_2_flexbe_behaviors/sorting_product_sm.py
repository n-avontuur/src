#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from unit_2_flexbe_behaviors.getlocationpartsbins_sm import GetLocationPartsBinsSM
from unit_2_flexbe_behaviors.initgripper_sm import initGripperSM
from unit_2_flexbe_behaviors.pick_part_from_conveyor_sm import pick_part_from_conveyorSM
from unit_2_flexbe_behaviors.place_part_on_bin_sm import place_part_on_binSM
from unit_2_flexbe_behaviors.transport__conveyor_to_pick_location_sm import transport_conveyor_to_pick_locationSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sat May 29 2021
@author: niels avontuur
'''
class sorting_productSM(Behavior):
	'''
	overview behavior for sorting products
	'''


	def __init__(self):
		super(sorting_productSM, self).__init__()
		self.name = 'sorting_product'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(GetLocationPartsBinsSM, 'GetLocationPartsBins')
		self.add_behavior(initGripperSM, 'initGripper')
		self.add_behavior(pick_part_from_conveyorSM, 'pick_part_from_conveyor')
		self.add_behavior(place_part_on_binSM, 'place_part_on_bin')
		self.add_behavior(transport_conveyor_to_pick_locationSM, 'transport_ conveyor_to_pick_location')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:967 y:602, x:534 y:297
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.binPartType = ['empty','empty', 'empty', 'empty', 'empty', 'empty']
		_state_machine.userdata.gasket_OffsetSize = [0.15,0.1,0.035]
		_state_machine.userdata.piston_OffsetSize = [0.11,0.11,0.02]
		_state_machine.userdata.gear_OffsetSize = [0.13,0.1,0.025]
		_state_machine.userdata.gasket_NumberOf = 0
		_state_machine.userdata.piston_NumberOf = 0
		_state_machine.userdata.gear_NumberOf = 0
		_state_machine.userdata.gasket_MaxNumberOf = [3,2]
		_state_machine.userdata.piston_MaxNumberOf = [3,3]
		_state_machine.userdata.gear_MaxNumberOf = [4,4]
		_state_machine.userdata.gasket_Offset = [0.0,0.0,0.0]
		_state_machine.userdata.piston_Offset = [0.0,0.0,0.0]
		_state_machine.userdata.gear_Offset = [0.0,0.0,0.0]
		_state_machine.userdata.gasket = [_state_machine.userdata.gasket_OffsetSize,_state_machine.userdata.gasket_NumberOf,_state_machine.userdata.gasket_MaxNumberOf,_state_machine.userdata.gasket_Offset]
		_state_machine.userdata.piston = [_state_machine.userdata.piston_OffsetSize,_state_machine.userdata.piston_NumberOf,_state_machine.userdata.piston_MaxNumberOf,_state_machine.userdata.piston_Offset]
		_state_machine.userdata.gear = [_state_machine.userdata.gear_OffsetSize,_state_machine.userdata.gear_NumberOf,_state_machine.userdata.gear_MaxNumberOf,_state_machine.userdata.gear_Offset]
		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:157 y:16
			OperatableStateMachine.add('initGripper',
										self.use_behavior(initGripperSM, 'initGripper'),
										transitions={'finished': 'GetLocationPartsBins', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:984 y:144
			OperatableStateMachine.add('pick_part_from_conveyor',
										self.use_behavior(pick_part_from_conveyorSM, 'pick_part_from_conveyor',
											default_keys=['robot_namespace']),
										transitions={'finished': 'place_part_on_bin', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part': 'part'})

			# x:987 y:251
			OperatableStateMachine.add('place_part_on_bin',
										self.use_behavior(place_part_on_binSM, 'place_part_on_bin'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part': 'part'})

			# x:769 y:20
			OperatableStateMachine.add('transport_ conveyor_to_pick_location',
										self.use_behavior(transport_conveyor_to_pick_locationSM, 'transport_ conveyor_to_pick_location'),
										transitions={'finished': 'pick_part_from_conveyor', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:486 y:13
			OperatableStateMachine.add('GetLocationPartsBins',
										self.use_behavior(GetLocationPartsBinsSM, 'GetLocationPartsBins'),
										transitions={'finished': 'transport_ conveyor_to_pick_location', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'binPartType': 'binPartType'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
