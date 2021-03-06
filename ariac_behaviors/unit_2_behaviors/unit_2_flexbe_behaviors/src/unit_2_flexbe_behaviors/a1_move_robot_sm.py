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
from ariac_flexbe_states.set_RobotParameters import set_Robot_Parameters
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from ariac_flexbe_states.vacuum_gripper_control_state import VacuumGripperControlState
from flexbe_states.wait_state import WaitState
from unit_2_flexbe_behaviors.a1_robots_home_sm import a1_Robots_HomeSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Mon May 31 2021
@author: Niels Avontuur
'''
class a1_Move_RobotSM(Behavior):
	'''
	This is for picking up the part and place it in the correct bin
	'''


	def __init__(self):
		super(a1_Move_RobotSM, self).__init__()
		self.name = 'a1_Move_Robot'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(a1_Robots_HomeSM, 'a1_Robots_Home')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		joint_names = ['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
		# x:100 y:214, x:587 y:317
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['pick_Pose', 'pick_Rotation', 'drop_Pose', 'drop_Offset', 'drop_Rotation', 'prePick_Config', 'preDrop_Config', 'pick_Offset', 'robot_Name'])
		_state_machine.userdata.pick_Pose = []
		_state_machine.userdata.pick_Offset = [0,0,0]
		_state_machine.userdata.pick_Rotation = 0.0
		_state_machine.userdata.drop_Pose = []
		_state_machine.userdata.drop_Offset = [0,0,0]
		_state_machine.userdata.drop_Rotation = 0.0
		_state_machine.userdata.prePick_Config = ''
		_state_machine.userdata.preDrop_Config = ''
		_state_machine.userdata.robot_Name = ''
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.gripper_status_enabled = False
		_state_machine.userdata.gripper_status_attached = False
		_state_machine.userdata.height = 0
		_state_machine.userdata.rotation = 0.0
		_state_machine.userdata.offset = 0.0

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:30 y:40
			OperatableStateMachine.add('a1_Robots_Home',
										self.use_behavior(a1_Robots_HomeSM, 'a1_Robots_Home'),
										transitions={'finished': 'set_Robot_Parameters', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:1035 y:538
			OperatableStateMachine.add('addPoseToBinPose',
										AddOffsetToPoseState(),
										transitions={'continue': 'computePick_2'},
										autonomy={'continue': Autonomy.Off},
										remapping={'input_pose': 'drop_OffsetPose', 'offset_pose': 'drop_Pose', 'output_pose': 'drop_Pose'})

			# x:1020 y:189
			OperatableStateMachine.add('check_Gripper',
										GetVacuumGripperStatusState(),
										transitions={'continue': 'move_To_PreDrop', 'fail': 'move_To_PrePick'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'topic_name': 'gripper_status_topic', 'enabled': 'gripper_status_enabled', 'attached': 'gripper_status_attached'})

			# x:51 y:438
			OperatableStateMachine.add('check_Gripper_2',
										GetVacuumGripperStatusState(),
										transitions={'continue': 'move_To_PrePick_2', 'fail': 'wait_4'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'topic_name': 'gripper_status_topic', 'enabled': 'gripper_status_enabled', 'attached': 'gripper_status_attached'})

			# x:609 y:110
			OperatableStateMachine.add('computePick',
										ComputeGraspAriacState(joint_names=joint_names),
										transitions={'continue': 'move_To_Pick', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'action_topic_namespace': 'action_topic_namespace', 'tool_link': 'tool_link', 'pose': 'pick_Pose', 'offset': 'offset', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:852 y:495
			OperatableStateMachine.add('computePick_2',
										ComputeGraspAriacState(joint_names=joint_names),
										transitions={'continue': 'move_To_Pick_2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'action_topic_namespace': 'action_topic_namespace', 'tool_link': 'tool_link', 'pose': 'drop_Pose', 'offset': 'offset', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1025 y:400
			OperatableStateMachine.add('createDropPose',
										CreatePoseState(xyz=[0.0,0.0,0.035], rpy=[0.0,0.0,0.0]),
										transitions={'continue': 'addPoseToBinPose', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'pose': 'drop_OffsetPose'})

			# x:300 y:438
			OperatableStateMachine.add('disable_Gripper',
										VacuumGripperControlState(enable=True),
										transitions={'continue': 'check_Gripper_2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'service_name': 'gripper_service'})

			# x:1015 y:107
			OperatableStateMachine.add('enable_Gripper',
										VacuumGripperControlState(enable=True),
										transitions={'continue': 'check_Gripper', 'failed': 'wait_6'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'service_name': 'gripper_service'})

			# x:810 y:115
			OperatableStateMachine.add('move_To_Pick',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'enable_Gripper', 'planning_failed': 'wait_2', 'control_failed': 'wait_2'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'action_topic_namespace': 'action_topic_namespace', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:553 y:434
			OperatableStateMachine.add('move_To_Pick_2',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'disable_Gripper', 'planning_failed': 'wait_5', 'control_failed': 'wait_5'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'action_topic_namespace': 'action_topic_namespace', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1031 y:284
			OperatableStateMachine.add('move_To_PreDrop',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'createDropPose', 'planning_failed': 'wait_3', 'control_failed': 'wait_3', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'preDrop_Config', 'move_group': 'move_group', 'action_topic_namespace': 'action_topic_namespace', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:382 y:99
			OperatableStateMachine.add('move_To_PrePick',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'computePick', 'planning_failed': 'wait', 'control_failed': 'wait', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'prePick_Config', 'move_group': 'move_group', 'action_topic_namespace': 'action_topic_namespace', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:55 y:290
			OperatableStateMachine.add('move_To_PrePick_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'finished', 'planning_failed': 'wait_7', 'control_failed': 'wait_7', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'prePick_Config', 'move_group': 'move_group', 'action_topic_namespace': 'action_topic_namespace', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:31 y:129
			OperatableStateMachine.add('set_Robot_Parameters',
										set_Robot_Parameters(),
										transitions={'continue': 'move_To_PrePick', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'robot_Name': 'robot_Name', 'move_group': 'move_group', 'action_topic_namespace': 'action_topic_namespace', 'action_topic': 'action_topic', 'tool_link': 'tool_link', 'gripper_service': 'gripper_service', 'gripper_status_topic': 'gripper_status_topic', 'gripper_status_attached': 'gripper_status_attached', 'gripper_status_enabled': 'gripper_status_enabled', 'prePick_Config': 'prePick_Config', 'robot_name': 'robot_name'})

			# x:401 y:24
			OperatableStateMachine.add('wait',
										WaitState(wait_time=0.5),
										transitions={'done': 'move_To_PrePick'},
										autonomy={'done': Autonomy.Off})

			# x:846 y:19
			OperatableStateMachine.add('wait_2',
										WaitState(wait_time=0.5),
										transitions={'done': 'move_To_Pick'},
										autonomy={'done': Autonomy.Off})

			# x:1215 y:281
			OperatableStateMachine.add('wait_3',
										WaitState(wait_time=0.5),
										transitions={'done': 'move_To_PreDrop'},
										autonomy={'done': Autonomy.Off})

			# x:600 y:602
			OperatableStateMachine.add('wait_4',
										WaitState(wait_time=0.5),
										transitions={'done': 'move_To_PreDrop'},
										autonomy={'done': Autonomy.Off})

			# x:596 y:527
			OperatableStateMachine.add('wait_5',
										WaitState(wait_time=0.5),
										transitions={'done': 'move_To_Pick_2'},
										autonomy={'done': Autonomy.Off})

			# x:731 y:35
			OperatableStateMachine.add('wait_6',
										WaitState(wait_time=0.5),
										transitions={'done': 'move_To_PrePick'},
										autonomy={'done': Autonomy.Off})

			# x:280 y:345
			OperatableStateMachine.add('wait_7',
										WaitState(wait_time=0.5),
										transitions={'done': 'move_To_PrePick_2'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
