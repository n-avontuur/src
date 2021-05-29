#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.setBinPartType import setBinPartType
from ariac_logistics_flexbe_states.get_material_locations import GetMaterialLocationsState
from ariac_support_flexbe_states.get_item_from_list_state import GetItemFromListState
from ariac_support_flexbe_states.replace_state import ReplaceState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sat May 29 2021
@author: niels avontuur
'''
class GetLocationPartsBinsSM(Behavior):
	'''
	Add location to bins
	'''


	def __init__(self):
		super(GetLocationPartsBinsSM, self).__init__()
		self.name = 'GetLocationPartsBins'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:771 y:503, x:834 y:291
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.bin1PartType = 'empty'
		_state_machine.userdata.bin2PartType = 'empty'
		_state_machine.userdata.bin3PartType = 'empty'
		_state_machine.userdata.bin4PartType = 'empty'
		_state_machine.userdata.bin5PartType = 'empty'
		_state_machine.userdata.bin6PartType = 'empty'
		_state_machine.userdata.part = ''
		_state_machine.userdata.locations = []
		_state_machine.userdata.zero = 0
		_state_machine.userdata.gasket = 'gasket_part'
		_state_machine.userdata.piston = 'piston_rod_part'
		_state_machine.userdata.gear = 'gear_part'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:40 y:52
			OperatableStateMachine.add('replacePart',
										ReplaceState(),
										transitions={'done': 'getPartLocation'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'gear', 'result': 'part'})

			# x:415 y:179
			OperatableStateMachine.add('getBin_2',
										GetItemFromListState(),
										transitions={'done': 'setPartTypeInBins_2', 'invalid_index': 'replacePart_2_2'},
										autonomy={'done': Autonomy.Off, 'invalid_index': Autonomy.Off},
										remapping={'list': 'locations', 'index': 'zero', 'item': 'bin'})

			# x:424 y:374
			OperatableStateMachine.add('getBin_2_2',
										GetItemFromListState(),
										transitions={'done': 'setPartTypeInBins_2_2', 'invalid_index': 'finished'},
										autonomy={'done': Autonomy.Off, 'invalid_index': Autonomy.Off},
										remapping={'list': 'locations', 'index': 'zero', 'item': 'bin'})

			# x:217 y:52
			OperatableStateMachine.add('getPartLocation',
										GetMaterialLocationsState(),
										transitions={'continue': 'getBin'},
										autonomy={'continue': Autonomy.Off},
										remapping={'part': 'part', 'material_locations': 'locations'})

			# x:218 y:166
			OperatableStateMachine.add('getPartLocation_2',
										GetMaterialLocationsState(),
										transitions={'continue': 'getBin_2'},
										autonomy={'continue': Autonomy.Off},
										remapping={'part': 'part', 'material_locations': 'locations'})

			# x:222 y:372
			OperatableStateMachine.add('getPartLocation_2_2',
										GetMaterialLocationsState(),
										transitions={'continue': 'getBin_2_2'},
										autonomy={'continue': Autonomy.Off},
										remapping={'part': 'part', 'material_locations': 'locations'})

			# x:40 y:160
			OperatableStateMachine.add('replacePart_2',
										ReplaceState(),
										transitions={'done': 'getPartLocation_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'piston', 'result': 'part'})

			# x:40 y:375
			OperatableStateMachine.add('replacePart_2_2',
										ReplaceState(),
										transitions={'done': 'getPartLocation_2_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'piston', 'result': 'part'})

			# x:613 y:69
			OperatableStateMachine.add('setPartTypeInBins',
										setBinPartType(),
										transitions={'continue': 'replacePart_2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'bin': 'bin', 'part': 'part', 'bin1PartType': 'bin1PartType', 'bin2PartType': 'bin2PartType', 'bin3PartType': 'bin3PartType', 'bin4PartType': 'bin4PartType', 'bin5PartType': 'bin5PartType', 'bin6PartType': 'bin6PartType'})

			# x:638 y:173
			OperatableStateMachine.add('setPartTypeInBins_2',
										setBinPartType(),
										transitions={'continue': 'replacePart_2_2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'bin': 'bin', 'part': 'part', 'bin1PartType': 'bin1PartType', 'bin2PartType': 'bin2PartType', 'bin3PartType': 'bin3PartType', 'bin4PartType': 'bin4PartType', 'bin5PartType': 'bin5PartType', 'bin6PartType': 'bin6PartType'})

			# x:637 y:369
			OperatableStateMachine.add('setPartTypeInBins_2_2',
										setBinPartType(),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'bin': 'bin', 'part': 'part', 'bin1PartType': 'bin1PartType', 'bin2PartType': 'bin2PartType', 'bin3PartType': 'bin3PartType', 'bin4PartType': 'bin4PartType', 'bin5PartType': 'bin5PartType', 'bin6PartType': 'bin6PartType'})

			# x:416 y:53
			OperatableStateMachine.add('getBin',
										GetItemFromListState(),
										transitions={'done': 'setPartTypeInBins', 'invalid_index': 'replacePart_2'},
										autonomy={'done': Autonomy.Off, 'invalid_index': Autonomy.Off},
										remapping={'list': 'locations', 'index': 'zero', 'item': 'bin'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
