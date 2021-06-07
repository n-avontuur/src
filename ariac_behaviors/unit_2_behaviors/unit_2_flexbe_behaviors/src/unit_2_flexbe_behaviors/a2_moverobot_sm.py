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
from ariac_flexbe_states.create_dropPose import CreateDropPoseState
from ariac_flexbe_states.create_pose import CreatePoseState
from ariac_flexbe_states.get_vacuum_gripper_status_state import GetVacuumGripperStatusState
from ariac_flexbe_states.moveit_to_joints_dyn_ariac_state import MoveitToJointsDynAriacState
from ariac_flexbe_states.set_RobotParameters import set_Robot_Parameters
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from ariac_flexbe_states.vacuum_gripper_control_state import VacuumGripperControlState
from ariac_support_flexbe_states.equal_state import EqualState
from flexbe_states.wait_state import WaitState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sun Jun 06 2021
@author: Niels Avontuur
'''
class a2_MoveRobotSM(Behavior):
	'''
	Version 2 of moving robot
	'''


	def __init__(self):
		super(a2_MoveRobotSM, self).__init__()
		self.name = 'a2_MoveRobot'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		joint_names = ['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
		# x:30 y:463, x:554 y:386
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['pick_Offset', 'pick_Rotation', 'robot_Name', 'preDrop_Config', 'prePick_Config', 'bin_Pose', 'drop_Offset', 'drop_Rotation', 'pick_Pose'])
		_state_machine.userdata.offset = 0.0
		_state_machine.userdata.rotation = 0.0
		_state_machine.userdata.pick_Offset = []
		_state_machine.userdata.pick_Rotation = []
		_state_machine.userdata.trueVariable = True
		_state_machine.userdata.falseVariable = False
		_state_machine.userdata.robot_Name = ''
		_state_machine.userdata.preDrop_Config = ''
		_state_machine.userdata.prePick_Config = ''
		_state_machine.userdata.bin_Pose = []
		_state_machine.userdata.drop_Offset = []
		_state_machine.userdata.drop_Rotation = []
		_state_machine.userdata.pick_Pose = []
		_state_machine.userdata.home_Config = ''

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:30 y:40
			OperatableStateMachine.add('setRobotParameters',
										set_Robot_Parameters(),
										transitions={'continue': 'createPickOffsetPose', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'robot_Name': 'robot_Name', 'move_group': 'move_group', 'action_topic_namespace': 'action_topic_namespace', 'action_topic': 'action_topic', 'tool_link': 'tool_link', 'gripper_service': 'gripper_service', 'gripper_status_topic': 'gripper_status_topic', 'gripper_status_attached': 'gripper_status_attached', 'gripper_status_enabled': 'gripper_status_enabled', 'prePick_Config': 'prePick_Config', 'robot_name': 'robot_name', 'home_Config': 'home_Config'})

			# x:772 y:134
			OperatableStateMachine.add('addDecreasePose_2',
										AddOffsetToPoseState(),
										transitions={'continue': 'computePick'},
										autonomy={'continue': Autonomy.Off},
										remapping={'input_pose': 'pick_Pose', 'offset_pose': 'pose_Decrease', 'output_pose': 'pick_Pose'})

			# x:1572 y:400
			OperatableStateMachine.add('addDropOffsetPose',
										AddOffsetToPoseState(),
										transitions={'continue': 'moveToPreDrop'},
										autonomy={'continue': Autonomy.Off},
										remapping={'input_pose': 'bin_Pose', 'offset_pose': 'drop_OffsetPose', 'output_pose': 'drop_Pose'})

			# x:1554 y:44
			OperatableStateMachine.add('chechGripperStatus',
										GetVacuumGripperStatusState(),
										transitions={'continue': 'isPartAttached', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'topic_name': 'gripper_status_topic', 'enabled': 'gripper_Enabled', 'attached': 'gripper_Attached'})

			# x:23 y:722
			OperatableStateMachine.add('chechGripperStatus_2',
										GetVacuumGripperStatusState(),
										transitions={'continue': 'isPartAttached_2', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'topic_name': 'gripper_status_topic', 'enabled': 'gripper_Enabled', 'attached': 'gripper_Attached'})

			# x:367 y:43
			OperatableStateMachine.add('combinePosePick',
										AddOffsetToPoseState(),
										transitions={'continue': 'moveToPrePick'},
										autonomy={'continue': Autonomy.Off},
										remapping={'input_pose': 'pick_Pose', 'offset_pose': 'pick_OffsetPose', 'output_pose': 'pick_Pose'})

			# x:879 y:733
			OperatableStateMachine.add('computeDrop',
										ComputeGraspAriacState(joint_names=joint_names),
										transitions={'continue': 'moveToDrop', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'action_topic_namespace': 'action_topic_namespace', 'tool_link': 'tool_link', 'pose': 'drop_Pose', 'offset': 'offset', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:768 y:27
			OperatableStateMachine.add('computePick',
										ComputeGraspAriacState(joint_names=joint_names),
										transitions={'continue': 'moveToPick', 'failed': 'moveHome'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'action_topic_namespace': 'action_topic_namespace', 'tool_link': 'tool_link', 'pose': 'pick_Pose', 'offset': 'offset', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1282 y:225
			OperatableStateMachine.add('createDecreasePick',
										CreatePoseState(xyz=[0.0,0.0,-0.002], rpy=[0.0,0.0,0.0]),
										transitions={'continue': 'addDecreasePose', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'pose_Decrease'})

			# x:751 y:221
			OperatableStateMachine.add('createDecreasePick_2',
										CreatePoseState(xyz=[0.0,0.0,0.002], rpy=[0.0,0.0,0.0]),
										transitions={'continue': 'addDecreasePose_2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'pose_Decrease'})

			# x:1576 y:290
			OperatableStateMachine.add('createDropOffsetPose',
										CreateDropPoseState(),
										transitions={'continue': 'addDropOffsetPose', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'xyz': 'drop_Offset', 'rpy': 'drop_Rotation', 'pose': 'drop_OffsetPose'})

			# x:194 y:39
			OperatableStateMachine.add('createPickOffsetPose',
										CreateDropPoseState(),
										transitions={'continue': 'combinePosePick', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'xyz': 'pick_Offset', 'rpy': 'pick_Rotation', 'pose': 'pick_OffsetPose'})

			# x:1562 y:176
			OperatableStateMachine.add('isPartAttached',
										EqualState(),
										transitions={'true': 'createDropOffsetPose', 'false': 'createDecreasePick'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'gripper_Attached', 'value_b': 'trueVariable'})

			# x:23 y:653
			OperatableStateMachine.add('isPartAttached_2',
										EqualState(),
										transitions={'true': 'moveBackToPreDrop', 'false': 'wait_3_2_2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'gripper_Attached', 'value_b': 'falseVariable'})

			# x:23 y:583
			OperatableStateMachine.add('moveBackToPreDrop',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'finished', 'planning_failed': 'wait_6', 'control_failed': 'wait_6', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'preDrop_Config', 'move_group': 'move_group', 'action_topic_namespace': 'action_topic_namespace', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:630 y:106
			OperatableStateMachine.add('moveHome',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'wait', 'planning_failed': 'wait_7', 'control_failed': 'wait_7', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'home_Config', 'move_group': 'move_group', 'action_topic_namespace': 'action_topic_namespace', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:669 y:731
			OperatableStateMachine.add('moveToDrop',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'setGripperOff', 'planning_failed': 'wait_5', 'control_failed': 'wait_5'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'action_topic_namespace': 'action_topic_namespace', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:984 y:38
			OperatableStateMachine.add('moveToPick',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'setGripperOn', 'planning_failed': 'createDecreasePick_2', 'control_failed': 'createDecreasePick_2'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'action_topic_namespace': 'action_topic_namespace', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1087 y:734
			OperatableStateMachine.add('moveToPreDrop',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'computeDrop', 'planning_failed': 'wait_4', 'control_failed': 'wait_4', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'preDrop_Config', 'move_group': 'move_group', 'action_topic_namespace': 'action_topic_namespace', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:557 y:43
			OperatableStateMachine.add('moveToPrePick',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'computePick', 'planning_failed': 'wait', 'control_failed': 'wait', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'prePick_Config', 'move_group': 'move_group', 'action_topic_namespace': 'action_topic_namespace', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:456 y:732
			OperatableStateMachine.add('setGripperOff',
										VacuumGripperControlState(enable=False),
										transitions={'continue': 'wait_3_2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'service_name': 'gripper_service'})

			# x:1208 y:39
			OperatableStateMachine.add('setGripperOn',
										VacuumGripperControlState(enable=True),
										transitions={'continue': 'wait_3', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'service_name': 'gripper_service'})

			# x:480 y:162
			OperatableStateMachine.add('wait',
										WaitState(wait_time=0.5),
										transitions={'done': 'moveToPrePick'},
										autonomy={'done': Autonomy.Off})

			# x:1437 y:40
			OperatableStateMachine.add('wait_3',
										WaitState(wait_time=0.5),
										transitions={'done': 'chechGripperStatus'},
										autonomy={'done': Autonomy.Off})

			# x:306 y:734
			OperatableStateMachine.add('wait_3_2',
										WaitState(wait_time=0.5),
										transitions={'done': 'chechGripperStatus_2'},
										autonomy={'done': Autonomy.Off})

			# x:411 y:642
			OperatableStateMachine.add('wait_3_2_2',
										WaitState(wait_time=0.5),
										transitions={'done': 'setGripperOff'},
										autonomy={'done': Autonomy.Off})

			# x:1095 y:650
			OperatableStateMachine.add('wait_4',
										WaitState(wait_time=0.5),
										transitions={'done': 'moveToPreDrop'},
										autonomy={'done': Autonomy.Off})

			# x:678 y:643
			OperatableStateMachine.add('wait_5',
										WaitState(wait_time=0.5),
										transitions={'done': 'moveToDrop'},
										autonomy={'done': Autonomy.Off})

			# x:192 y:517
			OperatableStateMachine.add('wait_6',
										WaitState(wait_time=0.5),
										transitions={'done': 'moveBackToPreDrop'},
										autonomy={'done': Autonomy.Off})

			# x:480 y:224
			OperatableStateMachine.add('wait_7',
										WaitState(wait_time=0.5),
										transitions={'done': 'moveHome'},
										autonomy={'done': Autonomy.Off})

			# x:1026 y:248
			OperatableStateMachine.add('addDecreasePose',
										AddOffsetToPoseState(),
										transitions={'continue': 'computePick'},
										autonomy={'continue': Autonomy.Off},
										remapping={'input_pose': 'pick_Pose', 'offset_pose': 'pose_Decrease', 'output_pose': 'pick_Pose'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
