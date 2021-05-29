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
from ariac_flexbe_states.detect_first_part_camera_ariac_state import DetectFirstPartCameraAriacState
from ariac_flexbe_states.get_vacuum_gripper_status_state import GetVacuumGripperStatusState
from ariac_flexbe_states.moveit_to_joints_dyn_ariac_state import MoveitToJointsDynAriacState
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from ariac_flexbe_states.vacuum_gripper_control_state import VacuumGripperControlState
from flexbe_states.wait_state import WaitState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sun Apr 25 2021
@author: docent
'''
class pick_part_from_conveyorSM(Behavior):
	'''
	pick's a part form athe conveyor
	'''


	def __init__(self):
		super(pick_part_from_conveyorSM, self).__init__()
		self.name = 'pick_part_from_conveyor'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		partlist = ['gasket_part', 'piston_rod_part', 'gear_part', ' pulley_part', 'disk_part']
		detect_TimeOut = 0.5
		joint_names = ['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
		# x:985 y:688, x:871 y:512
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['robot_namespace'], output_keys=['part'])
		_state_machine.userdata.part = ""
		_state_machine.userdata.robot_namespace = ''
		_state_machine.userdata.bin = 'bin1'
		_state_machine.userdata.Conveyor_camera_topic = '/ariac/logical_camera_1'
		_state_machine.userdata.part = "gear_part"
		_state_machine.userdata.conveyor_Config_Name = 'homeR1'
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
		_state_machine.userdata.gripper_service_name = '/ariac/arm1/gripper/control'
		_state_machine.userdata.gripper_status_topic = '/ariac/arm1/gripper/state'
		_state_machine.userdata.gripper_status_attached = False
		_state_machine.userdata.gripper_status_enabled = False
		_state_machine.userdata.conveyor_camera_frame = 'logical_camera_1_frame'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:47 y:123
			OperatableStateMachine.add('gripperON_2',
										VacuumGripperControlState(enable=False),
										transitions={'continue': 'gripperOFF_2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'service_name': 'gripper_service_name'})

			# x:1218 y:145
			OperatableStateMachine.add('computePick',
										ComputeGraspAriacState(joint_names=joint_names),
										transitions={'continue': 'moveToPick', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'action_topic_namespace': 'action_topic_namespace', 'tool_link': 'tool_link', 'pose': 'pose', 'offset': 'offset', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:341 y:117
			OperatableStateMachine.add('gripperOFF_2',
										VacuumGripperControlState(enable=False),
										transitions={'continue': 'locateFirstPart', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'service_name': 'gripper_service_name'})

			# x:1509 y:555
			OperatableStateMachine.add('gripperON',
										VacuumGripperControlState(enable=True),
										transitions={'continue': 'wait_2_3', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'service_name': 'gripper_service_name'})

			# x:559 y:117
			OperatableStateMachine.add('locateFirstPart',
										DetectFirstPartCameraAriacState(part_list=partlist, time_out=detect_TimeOut),
										transitions={'continue': 'moveToPregrasp', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'camera_ref_frame', 'camera_topic': 'Conveyor_camera_topic', 'camera_frame': 'conveyor_camera_frame', 'part': 'part', 'pose': 'pose'})

			# x:1498 y:445
			OperatableStateMachine.add('moveToPick',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'gripperON', 'planning_failed': 'wait_2', 'control_failed': 'wait_2'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'action_topic_namespace': 'action_topic_namespace', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:897 y:157
			OperatableStateMachine.add('moveToPregrasp',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'computePick', 'planning_failed': 'wait_1', 'control_failed': 'wait_1', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'conveyor_Config_Name', 'move_group': 'move_group', 'action_topic_namespace': 'action_topic_namespace', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1119 y:669
			OperatableStateMachine.add('moveToPregrasp_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'finished', 'planning_failed': 'wait_1_2', 'control_failed': 'wait_1_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'conveyor_Config_Name', 'move_group': 'move_group', 'action_topic_namespace': 'action_topic_namespace', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:915 y:53
			OperatableStateMachine.add('wait_1',
										WaitState(wait_time=0.5),
										transitions={'done': 'moveToPregrasp'},
										autonomy={'done': Autonomy.Off})

			# x:1148 y:784
			OperatableStateMachine.add('wait_1_2',
										WaitState(wait_time=0.5),
										transitions={'done': 'moveToPregrasp_2'},
										autonomy={'done': Autonomy.Off})

			# x:1553 y:338
			OperatableStateMachine.add('wait_2',
										WaitState(wait_time=0.5),
										transitions={'done': 'moveToPick'},
										autonomy={'done': Autonomy.Off})

			# x:1547 y:664
			OperatableStateMachine.add('wait_2_3',
										WaitState(wait_time=0.5),
										transitions={'done': 'checkGripperON'},
										autonomy={'done': Autonomy.Off})

			# x:1317 y:669
			OperatableStateMachine.add('checkGripperON',
										GetVacuumGripperStatusState(),
										transitions={'continue': 'moveToPregrasp_2', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'topic_name': 'gripper_status_topic', 'enabled': 'gripper_status_enabled', 'attached': 'gripper_status_attached'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
