#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_logistics_flexbe_states.get_material_locations import GetMaterialLocationsState
from ariac_support_flexbe_states.get_item_from_list_state import GetItemFromListState
from unit_2_flexbe_behaviors.locate_place_in_bin_with_content_sm import locate_Place_In_Bin_With_ContentSM
from unit_2_flexbe_behaviors.locate_place_in_empty_bin_sm import Locate_Place_In_Empty_BinSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Mon May 31 2021
@author: Niels Avontuur
'''
class a1_setting_ParametersSM(Behavior):
	'''
	This behavior wil set parameters for sorting the parts
	'''


	def __init__(self):
		super(a1_setting_ParametersSM, self).__init__()
		self.name = 'a1_setting_Parameters'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(Locate_Place_In_Empty_BinSM, 'Locate_Place_In_Empty_Bin')
		self.add_behavior(locate_Place_In_Bin_With_ContentSM, 'locate_Place_In_Bin_With_Content')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1154 y:207, x:780 y:242
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['part_Type', 'gasket', 'piston', 'gear', 'bin_Content'], output_keys=['drop_pose', 'pose_offset', 'PreDrop_config', 'robot_Name', 'gear', 'gasket', 'piston'])
		_state_machine.userdata.part_Type = ''
		_state_machine.userdata.zero = 0
		_state_machine.userdata.drop_pose = []
		_state_machine.userdata.pose_offset = []
		_state_machine.userdata.PreDrop_config = ''
		_state_machine.userdata.robot_Name = ''
		_state_machine.userdata.gasket = []
		_state_machine.userdata.piston = []
		_state_machine.userdata.gear = []
		_state_machine.userdata.bin_Content = []
		_state_machine.userdata.bin = ''
		_state_machine.userdata.part_Content = []

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:30 y:40
			OperatableStateMachine.add('getLocationOfAllParts',
										GetMaterialLocationsState(),
										transitions={'continue': 'getPartLocation'},
										autonomy={'continue': Autonomy.Off},
										remapping={'part': 'part_Type', 'material_locations': 'locations'})

			# x:34 y:145
			OperatableStateMachine.add('getPartLocation',
										GetItemFromListState(),
										transitions={'done': 'locate_Place_In_Bin_With_Content', 'invalid_index': 'Locate_Place_In_Empty_Bin'},
										autonomy={'done': Autonomy.Off, 'invalid_index': Autonomy.Off},
										remapping={'list': 'locations', 'index': 'zero', 'item': 'bin'})

			# x:436 y:136
			OperatableStateMachine.add('locate_Place_In_Bin_With_Content',
										self.use_behavior(locate_Place_In_Bin_With_ContentSM, 'locate_Place_In_Bin_With_Content'),
										transitions={'finished': 'finished', 'failed': 'failed', 'not_found': 'failed', 'bin_Full': 'Locate_Place_In_Empty_Bin'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit, 'not_found': Autonomy.Inherit, 'bin_Full': Autonomy.Inherit},
										remapping={'bin': 'bin', 'part_Type': 'part_Type', 'drop_pose': 'drop_pose', 'pose_offset': 'pose_offset', 'PreDrop_config': 'PreDrop_config', 'robot_Name': 'robot_Name'})

			# x:441 y:369
			OperatableStateMachine.add('Locate_Place_In_Empty_Bin',
										self.use_behavior(Locate_Place_In_Empty_BinSM, 'Locate_Place_In_Empty_Bin'),
										transitions={'finished': 'finished', 'failed': 'failed', 'bin_Full': 'getLocationOfAllParts'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit, 'bin_Full': Autonomy.Inherit},
										remapping={'part_Type': 'part_Type', 'gasket': 'gasket', 'piston': 'piston', 'gear': 'gear', 'bin_Content': 'bin_Content', 'drop_pose': 'drop_pose', 'pose_offset': 'pose_offset', 'PreDrop_config': 'PreDrop_config', 'robot_Name': 'robot_Name'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
