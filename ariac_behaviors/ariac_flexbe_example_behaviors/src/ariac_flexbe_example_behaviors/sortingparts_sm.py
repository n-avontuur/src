#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from unit_2_flexbe_behaviors.pick_part_from_conveyor_sm import pick_part_from_conveyorSM
from unit_2_flexbe_behaviors.place_part_on_bin_sm import place_part_on_binSM
from unit_2_flexbe_behaviors.transport__conveyor_to_pick_location_sm import transport_conveyor_to_pick_locationSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sat May 29 2021
@author: Niels Avontuur
'''
class sortingPartsSM(Behavior):
	'''
	For sorting the parts to different bins
	'''


	def __init__(self):
		super(sortingPartsSM, self).__init__()
		self.name = 'sortingParts'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(pick_part_from_conveyorSM, 'pick_part_from_conveyor')
		self.add_behavior(place_part_on_binSM, 'place_part_on_bin')
		self.add_behavior(transport_conveyor_to_pick_locationSM, 'transport_ conveyor_to_pick_location')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:116 y:356, x:666 y:139
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:40 y:55
			OperatableStateMachine.add('pick_part_from_conveyor',
										self.use_behavior(pick_part_from_conveyorSM, 'pick_part_from_conveyor',
											default_keys=['robot_namespace']),
										transitions={'finished': 'transport_ conveyor_to_pick_location', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part': 'part'})

			# x:30 y:236
			OperatableStateMachine.add('place_part_on_bin',
										self.use_behavior(place_part_on_binSM, 'place_part_on_bin'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:30 y:138
			OperatableStateMachine.add('transport_ conveyor_to_pick_location',
										self.use_behavior(transport_conveyor_to_pick_locationSM, 'transport_ conveyor_to_pick_location'),
										transitions={'finished': 'place_part_on_bin', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
