#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.compute_grasp_ariac_state import ComputeGraspAriacState
from ariac_flexbe_states.detect_part_camera_ariac_state import DetectPartCameraAriacState
from ariac_flexbe_states.end_assignment_state import EndAssignment
from ariac_flexbe_states.get_vacuum_gripper_status_state import GetVacuumGripperStatusState
from ariac_flexbe_states.lookup_from_table import LookupFromTableState
from ariac_flexbe_states.moveit_to_joints_dyn_ariac_state import MoveitToJointsDynAriacState
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from ariac_flexbe_states.start_assignment_state import StartAssignment
from ariac_flexbe_states.vacuum_gripper_control_state import VacuumGripperControlState
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
		joint_names = ['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
		# x:51 y:714, x:853 y:393
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['part'])
		_state_machine.userdata.part = "gear_part"
		_state_machine.userdata.config_name = ' '
		_state_machine.userdata.move_group = 'manipulator'
		_state_machine.userdata.action_topic_namespace = '/ariac/arm1'
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.locations = []
		_state_machine.userdata.zero = 0
		_state_machine.userdata.camera_ref_frame = 'world'
		_state_machine.userdata.tool_link = 'ee_link'
		_state_machine.userdata.offset = 0.03
		_state_machine.userdata.rotation = 0
		_state_machine.userdata.gripper_service = '/ariac/arm1/gripper/control'
		_state_machine.userdata.gripper_status_topic = '/ariac/arm1/gripper/state'
		_state_machine.userdata.gripper_status_attached = False
		_state_machine.userdata.gripper_status_enabled = False

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:78 y:31
			OperatableStateMachine.add('startAssignment',
										StartAssignment(),
										transitions={'continue': 'getPartLocation'},
										autonomy={'continue': Autonomy.Off})

			# x:1416 y:445
			OperatableStateMachine.add('detectPart',
										DetectPartCameraAriacState(time_out=0.5),
										transitions={'continue': 'moveToPregrasp', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'camera_ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part', 'pose': 'pose'})

			# x:1192 y:709
			OperatableStateMachine.add('disableGripper',
										VacuumGripperControlState(enable=False),
										transitions={'continue': 'getStatusGripper', 'failed': 'wait_2_2'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'service_name': 'gripper_service'})

			# x:170 y:706
			OperatableStateMachine.add('endAssigment',
										EndAssignment(),
										transitions={'continue': 'finished'},
										autonomy={'continue': Autonomy.Off})

			# x:304 y:31
			OperatableStateMachine.add('getPartLocation',
										GetMaterialLocationsState(),
										transitions={'continue': 'itemFromList'},
										autonomy={'continue': Autonomy.Off},
										remapping={'part': 'part', 'material_locations': 'locations'})

			# x:672 y:704
			OperatableStateMachine.add('getStatusGripper',
										GetVacuumGripperStatusState(),
										transitions={'continue': 'endAssigment', 'fail': 'wait_2_2'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'topic_name': 'gripper_status_topic', 'enabled': 'gripper_status_enabled', 'attached': 'gripper_status_attached'})

			# x:519 y:29
			OperatableStateMachine.add('itemFromList',
										GetItemFromListState(),
										transitions={'done': 'lookUpCameraFrame', 'invalid_index': 'failed'},
										autonomy={'done': Autonomy.Off, 'invalid_index': Autonomy.Off},
										remapping={'list': 'locations', 'index': 'zero', 'item': 'bin'})

			# x:793 y:33
			OperatableStateMachine.add('lookUpCameraFrame',
										LookupFromTableState(parameter_name='/ariac_tables_unit2', table_name='bin_configuration_R1', index_title='bin', column_title='camera_frame'),
										transitions={'found': 'lookUpCameraTopic', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'camera_frame'})

			# x:1430 y:47
			OperatableStateMachine.add('lookUpCameraTopic',
										LookupFromTableState(parameter_name='/ariac_tables_unit2', table_name='bin_configuration_R1', index_title='bin', column_title='camera_topic'),
										transitions={'found': 'lookUpPregrasp', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'camera_topic'})

			# x:1424 y:130
			OperatableStateMachine.add('lookUpPregrasp',
										LookupFromTableState(parameter_name='/ariac_tables_unit2', table_name='bin_configuration_R1', index_title='bin', column_title='robot_config'),
										transitions={'found': 'detectPart', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'config_name'})

			# x:1413 y:713
			OperatableStateMachine.add('moveToDrop',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'disableGripper', 'planning_failed': 'wait_2', 'control_failed': 'wait_2'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'action_topic_namespace': 'action_topic_namespace', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1437 y:542
			OperatableStateMachine.add('moveToPregrasp',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'computeDrop', 'planning_failed': 'wait_1', 'control_failed': 'wait_1', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'action_topic_namespace': 'action_topic_namespace', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1694 y:549
			OperatableStateMachine.add('wait_1',
										WaitState(wait_time=0.5),
										transitions={'done': 'moveToPregrasp'},
										autonomy={'done': Autonomy.Off})

			# x:1691 y:736
			OperatableStateMachine.add('wait_2',
										WaitState(wait_time=0.5),
										transitions={'done': 'moveToDrop'},
										autonomy={'done': Autonomy.Off})

			# x:1156 y:801
			OperatableStateMachine.add('wait_2_2',
										WaitState(wait_time=0.5),
										transitions={'done': 'disableGripper'},
										autonomy={'done': Autonomy.Off})

			# x:1423 y:629
			OperatableStateMachine.add('computeDrop',
										ComputeGraspAriacState(joint_names=joint_names),
										transitions={'continue': 'moveToDrop', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'action_topic_namespace': 'action_topic_namespace', 'tool_link': 'tool_link', 'pose': 'pose', 'offset': 'offset', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
