#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.detect_part_camera_ariac_state import DetectPartCameraAriacState
from ariac_flexbe_states.end_assignment_state import EndAssignment
from ariac_flexbe_states.lookup_from_table import LookupFromTableState
from ariac_flexbe_states.moveit_to_joints_dyn_ariac_state import MoveitToJointsDynAriacState
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from ariac_flexbe_states.start_assignment_state import StartAssignment
from ariac_logistics_flexbe_states.get_material_locations import GetMaterialLocationsState
from ariac_support_flexbe_states.get_item_from_list_state import GetItemFromListState
from flexbe_states.wait_state import WaitState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri May 28 2021
@author: Niels Avontuur
'''
class place_part_on_binSM(Behavior):
	'''
	place
	'''


	def __init__(self):
		super(place_part_on_binSM, self).__init__()
		self.name = 'place_part_on_bin'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1727 y:63, x:685 y:383
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.part = "gear_part"
		_state_machine.userdata.config_name = ' '
		_state_machine.userdata.move_group = 'manipulator'
		_state_machine.userdata.action_topic_namespace = '/ariac/arm1'
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.ref_frame = 'world'
		_state_machine.userdata.location = []
		_state_machine.userdata.zero = 0

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:30 y:40
			OperatableStateMachine.add('startAssignment',
										StartAssignment(),
										transitions={'continue': 'getPartLocation'},
										autonomy={'continue': Autonomy.Off})

			# x:1561 y:47
			OperatableStateMachine.add('endAssigment',
										EndAssignment(),
										transitions={'continue': 'finished'},
										autonomy={'continue': Autonomy.Off})

			# x:25 y:121
			OperatableStateMachine.add('getPartLocation',
										GetMaterialLocationsState(),
										transitions={'continue': 'itemFromList'},
										autonomy={'continue': Autonomy.Off},
										remapping={'part': 'part', 'material_locations': 'bin'})

			# x:224 y:49
			OperatableStateMachine.add('itemFromList',
										GetItemFromListState(),
										transitions={'done': 'lookUpCameraFrame', 'invalid_index': 'failed'},
										autonomy={'done': Autonomy.Off, 'invalid_index': Autonomy.Off},
										remapping={'list': 'location', 'index': 'zero', 'item': 'bin'})

			# x:416 y:50
			OperatableStateMachine.add('lookUpCameraFrame',
										LookupFromTableState(parameter_name='/ariac_tables_unit2', table_name='bin_configuration_R1', index_title='bin', column_title='camera_frame'),
										transitions={'found': 'lookUpCameraTopic', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'camera_frame'})

			# x:613 y:53
			OperatableStateMachine.add('lookUpCameraTopic',
										LookupFromTableState(parameter_name='/ariac_tables_unit2', table_name='bin_configuration_R1', index_title='bin', column_title='camera_topic'),
										transitions={'found': 'lookUpPregrasp', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'camera_topic'})

			# x:811 y:36
			OperatableStateMachine.add('lookUpPregrasp',
										LookupFromTableState(parameter_name='/ariac_tables_unit2', table_name='bin_configuration_R1', index_title='bin', column_title='robot_config'),
										transitions={'found': 'detectPart', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'camera_topic'})

			# x:1518 y:133
			OperatableStateMachine.add('moveToPick',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'endAssigment', 'planning_failed': 'wait_2', 'control_failed': 'wait_2'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'action_topic_namespace': 'action_topic_namespace', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1277 y:75
			OperatableStateMachine.add('moveToPregrasp',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'moveToPick', 'planning_failed': 'wait_1', 'control_failed': 'wait_1', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'action_topic_namespace': 'action_topic_namespace', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1295 y:199
			OperatableStateMachine.add('wait_1',
										WaitState(wait_time=0.5),
										transitions={'done': 'moveToPregrasp'},
										autonomy={'done': Autonomy.Off})

			# x:1532 y:249
			OperatableStateMachine.add('wait_2',
										WaitState(wait_time=0.5),
										transitions={'done': 'moveToPick'},
										autonomy={'done': Autonomy.Off})

			# x:1035 y:44
			OperatableStateMachine.add('detectPart',
										DetectPartCameraAriacState(time_out=0.5),
										transitions={'continue': 'moveToPregrasp', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part', 'pose': 'pose'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
