#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.get_Empty_Bin import getEmptyBin
from ariac_flexbe_states.get_object_pose import GetObjectPoseState
from ariac_flexbe_states.lookup_from_table import LookupFromTableState
from ariac_flexbe_states.select_Robot import selectRobot
from ariac_flexbe_states.set_Part import setPart
from ariac_flexbe_states.set_new_position import setNewPosePart
from ariac_logistics_flexbe_states.get_material_locations import GetMaterialLocationsState
from ariac_support_flexbe_states.equal_state import EqualState
from ariac_support_flexbe_states.get_item_from_list_state import GetItemFromListState
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

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1670 y:194, x:913 y:490
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['part_Type', 'gasket', 'piston', 'gear', 'bin_Content', 'numberOfModels'], output_keys=['robot_Name', 'gear', 'gasket', 'piston', 'pick_Offset', 'pick_Rotation', 'drop_Pose', 'drop_Offset', 'drop_Rotation', 'preDrop_Config', 'prePick_Config'])
		_state_machine.userdata.part_Type = 'gear_part'
		_state_machine.userdata.zero = 0
		_state_machine.userdata.robot_Name = ''
		_state_machine.userdata.gasket = []
		_state_machine.userdata.piston = []
		_state_machine.userdata.gear = []
		_state_machine.userdata.bin_Content = ['empty', 'empty', 'empty', 'empty', 'empty', 'empty']
		_state_machine.userdata.bin = ''
		_state_machine.userdata.pick_Offset = []
		_state_machine.userdata.pick_Rotation = 0.0
		_state_machine.userdata.drop_Pose = []
		_state_machine.userdata.drop_Offset = []
		_state_machine.userdata.drop_Rotation = 0.0
		_state_machine.userdata.preDrop_Config = ''
		_state_machine.userdata.prePick_Config = ''
		_state_machine.userdata.robot1Name = 'arm1'
		_state_machine.userdata.ref_frame = 'world'
		_state_machine.userdata.bin_Pose = []
		_state_machine.userdata.numberOfModels = 0

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

			# x:257 y:178
			OperatableStateMachine.add('getEmptyBin',
										getEmptyBin(),
										transitions={'continue': 'selectRobot', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'binPartType': 'bin_Content', 'bin': 'bin', 'bin_frame': 'bin_frame'})

			# x:34 y:145
			OperatableStateMachine.add('getPartLocation',
										GetItemFromListState(),
										transitions={'done': 'failed', 'invalid_index': 'getEmptyBin'},
										autonomy={'done': Autonomy.Off, 'invalid_index': Autonomy.Off},
										remapping={'list': 'locations', 'index': 'zero', 'item': 'bin'})

			# x:1055 y:18
			OperatableStateMachine.add('getPreDropR1',
										LookupFromTableState(parameter_name='/ariac_tables_unit2', table_name='bin_configuration_R1', index_title='bin', column_title='robot_config'),
										transitions={'found': 'setNewDropPose', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'preDrop_Config'})

			# x:1061 y:122
			OperatableStateMachine.add('getPreDropR2',
										LookupFromTableState(parameter_name='/ariac_tables_unit2', table_name='bin_configuration_R2', index_title='bin', column_title='robot_config'),
										transitions={'found': 'setNewDropPose', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'preDrop_Config'})

			# x:422 y:39
			OperatableStateMachine.add('partType_part_Content',
										setPart(),
										transitions={'continue': 'getBinPose', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'part_Type': 'part_Type', 'gasket': 'gasket', 'piston': 'piston', 'gear': 'gear', 'part_Content': 'part_Content'})

			# x:257 y:43
			OperatableStateMachine.add('selectRobot',
										selectRobot(),
										transitions={'continue': 'partType_part_Content', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'bin': 'bin', 'robot_Name': 'robot_Name'})

			# x:1309 y:78
			OperatableStateMachine.add('setNewDropPose',
										setNewPosePart(),
										transitions={'continue': 'finished', 'failed': 'failed', 'bin_Full': 'finished'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'bin_Full': Autonomy.Off},
										remapping={'part_Content': 'part_Content', 'numberOfModels': 'numberOfModels', 'drop_Offset': 'drop_Offset', 'pick_Offset': 'pick_Offset', 'drop_Rotation': 'drop_Rotation', 'pick_Rotation': 'pick_Rotation'})

			# x:803 y:36
			OperatableStateMachine.add('useR1orR2',
										EqualState(),
										transitions={'true': 'getPreDropR1', 'false': 'getPreDropR2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'robot_Name', 'value_b': 'robot1Name'})

			# x:614 y:41
			OperatableStateMachine.add('getBinPose',
										GetObjectPoseState(),
										transitions={'continue': 'useR1orR2', 'failed': 'getBinPose'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'frame': 'bin_frame', 'pose': 'bin_Pose'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
