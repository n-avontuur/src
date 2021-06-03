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
from flexbe_states.log_key_state import LogKeyState
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
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['part_Type', 'gasket', 'piston', 'gear', 'bin_Content'], output_keys=['robot_Name', 'gear', 'gasket', 'piston', 'pick_Pose', 'pick_Offset', 'pick_Rotation', 'drop_Pose', 'drop_Offset', 'drop_Rotation', 'preDrop_Config', 'prePick_Config'])
		_state_machine.userdata.part_Type = ''
		_state_machine.userdata.zero = 0
		_state_machine.userdata.robot_Name = ''
		_state_machine.userdata.gasket = []
		_state_machine.userdata.piston = []
		_state_machine.userdata.gear = []
		_state_machine.userdata.bin_Content = []
		_state_machine.userdata.bin = ''
		_state_machine.userdata.part_Content = []
		_state_machine.userdata.pick_Pose = []
		_state_machine.userdata.pick_Offset = []
		_state_machine.userdata.pick_Rotation = 0
		_state_machine.userdata.drop_Pose = []
		_state_machine.userdata.drop_Offset = []
		_state_machine.userdata.drop_Rotation = []
		_state_machine.userdata.preDrop_Config = ''
		_state_machine.userdata.prePick_Config = ''

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
										transitions={'finished': 'printRobotName', 'bin_Full': 'Locate_Place_In_Empty_Bin', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'bin_Full': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'bin': 'bin', 'part_Type': 'part_Type', 'gasket': 'gasket', 'piston': 'piston', 'gear': 'gear', 'robot_Name': 'robot_Name', 'pick_Pose': 'pick_Pose', 'pick_Offset': 'pick_Offset', 'pick_Rotation': 'pick_Rotation', 'drop_Pose': 'drop_Pose', 'drop_Offset': 'drop_Offset', 'drop_Rotation': 'drop_Rotation', 'prePick_Config': 'prePick_Config', 'preDrop_Config': 'preDrop_Config'})

			# x:966 y:213
			OperatableStateMachine.add('printRobotName',
										LogKeyState(text="Pick offset : ", severity=Logger.REPORT_HINT),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'data': 'pick_Offset'})

			# x:441 y:369
			OperatableStateMachine.add('Locate_Place_In_Empty_Bin',
										self.use_behavior(Locate_Place_In_Empty_BinSM, 'Locate_Place_In_Empty_Bin'),
										transitions={'finished': 'printRobotName', 'failed': 'failed', 'bin_Full': 'getLocationOfAllParts'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit, 'bin_Full': Autonomy.Inherit},
										remapping={'part_Type': 'part_Type', 'gasket': 'gasket', 'piston': 'piston', 'gear': 'gear', 'bin_Content': 'bin_Content', 'pick_Pose': 'pick_Pose', 'pick_Offset': 'pick_Offset', 'pick_Rotation': 'pick_Rotation', 'drop_Pose': 'drop_Pose', 'drop_Offset': 'drop_Offset', 'drop_Rotation': 'drop_Rotation', 'preDrop_Config': 'preDrop_Config', 'prePick_Config': 'prePick_Config', 'robot_Name': 'robot_Name'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
