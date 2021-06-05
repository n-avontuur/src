#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.add_offset_to_pose_state import AddOffsetToPoseState
from ariac_flexbe_states.compute_grasp_ariac_state import ComputeGraspAriacState
from ariac_flexbe_states.create_pose import CreatePoseState
from ariac_flexbe_states.get_vacuum_gripper_status_state import GetVacuumGripperStatusState
from ariac_flexbe_states.moveit_to_joints_dyn_ariac_state import MoveitToJointsDynAriacState
from ariac_flexbe_states.set_Part_FirstTime import setFirstTimePart
from ariac_flexbe_states.set_RobotParameters import set_Robot_Parameters
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from ariac_flexbe_states.start_assignment_state import StartAssignment
from ariac_flexbe_states.vacuum_gripper_control_state import VacuumGripperControlState
from ariac_logistics_flexbe_states.get_material_locations import GetMaterialLocationsState
from ariac_support_flexbe_states.equal_state import EqualState
from ariac_support_flexbe_states.get_item_from_list_state import GetItemFromListState
from flexbe_states.wait_state import WaitState
from unit_2_flexbe_behaviors.a1_robots_home_sm import a1_Robots_HomeSM
from unit_2_flexbe_behaviors.locate_place_in_bin_with_content_sm import locate_Place_In_Bin_With_ContentSM
from unit_2_flexbe_behaviors.locate_place_in_empty_bin_sm import Locate_Place_In_Empty_BinSM
from unit_2_flexbe_behaviors.transport__conveyor_to_pick_unit2_location_sm import transport_conveyor_to_pick_unit2_locationSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri Jun 04 2021
@author: Niels Avontuur
'''
class a1_TotalProgramSM(Behavior):
	'''
	test voor hele programma in een keer
	'''


	def __init__(self):
		super(a1_TotalProgramSM, self).__init__()
		self.name = 'a1_TotalProgram'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(Locate_Place_In_Empty_BinSM, 'Locate_Place_In_Empty_Bin')
		self.add_behavior(a1_Robots_HomeSM, 'a1_Robots_Home')
		self.add_behavior(locate_Place_In_Bin_With_ContentSM, 'locate_Place_In_Bin_With_Content')
		self.add_behavior(transport_conveyor_to_pick_unit2_locationSM, 'transport_ conveyor_to_pick_unit2_location')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		joint_names = ['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
		# x:36 y:864, x:744 y:271
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.bin_Content = ['empty', 'empty', 'empty', 'empty', 'empty', 'empty']
		_state_machine.userdata.numberOfModels = 0
		_state_machine.userdata.robot_Name = ''
		_state_machine.userdata.pick_Offset = 0
		_state_machine.userdata.pick_Rotation = 0.0
		_state_machine.userdata.zero = 0
		_state_machine.userdata.offset = 0.035
		_state_machine.userdata.rotation = 0.0
		_state_machine.userdata.trueVariable = True
		_state_machine.userdata.falseVariable = False

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:58 y:40
			OperatableStateMachine.add('start',
										StartAssignment(),
										transitions={'continue': 'setAllParts'},
										autonomy={'continue': Autonomy.Off})

			# x:1280 y:276
			OperatableStateMachine.add('a1_Robots_Home',
										self.use_behavior(a1_Robots_HomeSM, 'a1_Robots_Home'),
										transitions={'finished': 'setRobotParameters', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:443 y:714
			OperatableStateMachine.add('computeDrop',
										ComputeGraspAriacState(joint_names=joint_names),
										transitions={'continue': 'moveToDrop', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'action_topic_namespace': 'action_topic_namespace', 'tool_link': 'tool_link', 'pose': 'drop_Pose', 'offset': 'offset', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1284 y:564
			OperatableStateMachine.add('computePick',
										ComputeGraspAriacState(joint_names=joint_names),
										transitions={'continue': 'moveToPick', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'action_topic_namespace': 'action_topic_namespace', 'tool_link': 'tool_link', 'pose': 'pick_Pose', 'offset': 'offset', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:924 y:607
			OperatableStateMachine.add('decreaseOffsetPose',
										AddOffsetToPoseState(),
										transitions={'continue': 'computePick'},
										autonomy={'continue': Autonomy.Off},
										remapping={'input_pose': 'pick_Pose', 'offset_pose': 'poseDecrease', 'output_pose': 'output_pose'})

			# x:1092 y:723
			OperatableStateMachine.add('getGripperStatus',
										VacuumGripperControlState(enable=True),
										transitions={'continue': 'isPartAttached', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'service_name': 'gripper_service'})

			# x:824 y:46
			OperatableStateMachine.add('getLocationOfAllParts',
										GetMaterialLocationsState(),
										transitions={'continue': 'getPartLocation'},
										autonomy={'continue': Autonomy.Off},
										remapping={'part': 'part_Type', 'material_locations': 'locations'})

			# x:1018 y:50
			OperatableStateMachine.add('getPartLocation',
										GetItemFromListState(),
										transitions={'done': 'locate_Place_In_Bin_With_Content', 'invalid_index': 'Locate_Place_In_Empty_Bin'},
										autonomy={'done': Autonomy.Off, 'invalid_index': Autonomy.Off},
										remapping={'list': 'locations', 'index': 'zero', 'item': 'bin'})

			# x:811 y:718
			OperatableStateMachine.add('isPartAttached',
										EqualState(),
										transitions={'true': 'movePreDrop', 'false': 'newPickPose'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'trueVariable', 'value_b': 'gripper_status_attached'})

			# x:1249 y:48
			OperatableStateMachine.add('locate_Place_In_Bin_With_Content',
										self.use_behavior(locate_Place_In_Bin_With_ContentSM, 'locate_Place_In_Bin_With_Content'),
										transitions={'finished': 'a1_Robots_Home', 'bin_Full': 'Locate_Place_In_Empty_Bin', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'bin_Full': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'bin': 'bin', 'part_Type': 'part_Type', 'gasket': 'gasket', 'piston': 'piston', 'gear': 'gear', 'robot_Name': 'robot_Name', 'pick_Offset': 'pick_Offset', 'pick_Rotation': 'pick_Rotation', 'drop_Pose': 'drop_Pose', 'drop_Offset': 'drop_Offset', 'drop_Rotation': 'drop_Rotation', 'prePick_Config': 'prePick_Config', 'preDrop_Config': 'preDrop_Config'})

			# x:612 y:718
			OperatableStateMachine.add('movePreDrop',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'computeDrop', 'planning_failed': 'wait_3', 'control_failed': 'wait_3', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'preDrop_Config', 'move_group': 'move_group', 'action_topic_namespace': 'action_topic_namespace', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:255 y:708
			OperatableStateMachine.add('moveToDrop',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'finished', 'planning_failed': 'wait_4', 'control_failed': 'wait_4'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'action_topic_namespace': 'action_topic_namespace', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1279 y:647
			OperatableStateMachine.add('moveToPick',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'setGripperOn', 'planning_failed': 'wait_2', 'control_failed': 'wait_2'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'action_topic_namespace': 'action_topic_namespace', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1286 y:494
			OperatableStateMachine.add('moveToPrePick',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'computePick', 'planning_failed': 'wait', 'control_failed': 'wait', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'prePick_Config', 'move_group': 'move_group', 'action_topic_namespace': 'action_topic_namespace', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:791 y:609
			OperatableStateMachine.add('newPickPose',
										CreatePoseState(xyz=[0.0,0.0,-0.01], rpy=[0.0,0.0,0.0]),
										transitions={'continue': 'decreaseOffsetPose', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'poseDecrease'})

			# x:207 y:45
			OperatableStateMachine.add('setAllParts',
										setFirstTimePart(),
										transitions={'continue': 'transport_ conveyor_to_pick_unit2_location', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'gasket': 'gasket', 'piston': 'piston', 'gear': 'gear'})

			# x:1278 y:726
			OperatableStateMachine.add('setGripperOn',
										GetVacuumGripperStatusState(),
										transitions={'continue': 'getGripperStatus', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'topic_name': 'gripper_status_topic', 'enabled': 'gripper_status_enabled', 'attached': 'gripper_status_attached'})

			# x:1297 y:386
			OperatableStateMachine.add('setRobotParameters',
										set_Robot_Parameters(),
										transitions={'continue': 'moveToPrePick', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'robot_Name': 'robot_Name', 'move_group': 'move_group', 'action_topic_namespace': 'action_topic_namespace', 'action_topic': 'action_topic', 'tool_link': 'tool_link', 'gripper_service': 'gripper_service', 'gripper_status_topic': 'gripper_status_topic', 'gripper_status_attached': 'gripper_status_attached', 'gripper_status_enabled': 'gripper_status_enabled', 'prePick_Config': 'prePick_Config', 'robot_name': 'robot_name'})

			# x:522 y:39
			OperatableStateMachine.add('transport_ conveyor_to_pick_unit2_location',
										self.use_behavior(transport_conveyor_to_pick_unit2_locationSM, 'transport_ conveyor_to_pick_unit2_location'),
										transitions={'finished': 'getLocationOfAllParts', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'pick_Pose': 'pick_Pose', 'part_Type': 'part_Type'})

			# x:1516 y:513
			OperatableStateMachine.add('wait',
										WaitState(wait_time=0.5),
										transitions={'done': 'moveToPrePick'},
										autonomy={'done': Autonomy.Off})

			# x:1521 y:648
			OperatableStateMachine.add('wait_2',
										WaitState(wait_time=0.5),
										transitions={'done': 'moveToPick'},
										autonomy={'done': Autonomy.Off})

			# x:631 y:804
			OperatableStateMachine.add('wait_3',
										WaitState(wait_time=0.5),
										transitions={'done': 'wait_3'},
										autonomy={'done': Autonomy.Off})

			# x:278 y:796
			OperatableStateMachine.add('wait_4',
										WaitState(wait_time=0.5),
										transitions={'done': 'moveToDrop'},
										autonomy={'done': Autonomy.Off})

			# x:1277 y:177
			OperatableStateMachine.add('Locate_Place_In_Empty_Bin',
										self.use_behavior(Locate_Place_In_Empty_BinSM, 'Locate_Place_In_Empty_Bin'),
										transitions={'finished': 'a1_Robots_Home', 'failed': 'failed', 'bin_Full': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit, 'bin_Full': Autonomy.Inherit},
										remapping={'part_Type': 'part_Type', 'gasket': 'gasket', 'piston': 'piston', 'gear': 'gear', 'bin_Content': 'bin_Content', 'pick_Offset': 'pick_Offset', 'pick_Rotation': 'pick_Rotation', 'drop_Offset': 'drop_Offset', 'drop_Rotation': 'drop_Rotation', 'preDrop_Config': 'preDrop_Config', 'prePick_Config': 'prePick_Config', 'robot_Name': 'robot_Name', 'drop_Pose': 'drop_Pose'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
