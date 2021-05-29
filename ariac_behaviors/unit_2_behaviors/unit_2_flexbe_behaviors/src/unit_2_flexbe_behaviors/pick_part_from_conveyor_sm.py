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
from ariac_flexbe_states.moveit_to_joints_dyn_ariac_state import MoveitToJointsDynAriacState
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from flexbe_states.wait_state import WaitState
from unit_2_flexbe_behaviors.transport__conveyor_to_pick_location_sm import transport_conveyor_to_pick_locationSM
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
		self.add_behavior(transport_conveyor_to_pick_locationSM, 'transport_ conveyor_to_pick_location')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		partlist = ['gasket_part', 'piston_rod_part', 'gear_part', ' pulley_part', 'disk_part']
		detect_TimeOut = 0.5
		joint_names = ['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
		# x:606 y:693, x:871 y:512
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
		_state_machine.userdata.gripper_service = '/ariac/arm1/gripper/control'
		_state_machine.userdata.gripper_status_topic = '/ariac/arm1/gripper/state'
		_state_machine.userdata.gripper_status_attached = False
		_state_machine.userdata.gripper_status_enabled = False
		_state_machine.userdata.conveyor_camera_frame = 'logical_camera_1_frame'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:61 y:107
			OperatableStateMachine.add('transport_ conveyor_to_pick_location',
										self.use_behavior(transport_conveyor_to_pick_locationSM, 'transport_ conveyor_to_pick_location'),
										transitions={'finished': 'locateFirstPart', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:442 y:114
			OperatableStateMachine.add('locateFirstPart',
										DetectFirstPartCameraAriacState(part_list=partlist, time_out=detect_TimeOut),
										transitions={'continue': 'moveToPregrasp', 'failed': 'failed', 'not_found': 'wait_2_2'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'camera_ref_frame', 'camera_topic': 'Conveyor_camera_topic', 'camera_frame': 'conveyor_camera_frame', 'part': 'part', 'pose': 'pose'})

			# x:1413 y:713
			OperatableStateMachine.add('moveToPick',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'finished', 'planning_failed': 'wait_2', 'control_failed': 'wait_2'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'action_topic_namespace': 'action_topic_namespace', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1430 y:524
			OperatableStateMachine.add('moveToPregrasp',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'computePick', 'planning_failed': 'wait_1', 'control_failed': 'wait_1', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'conveyor_Config_Name', 'move_group': 'move_group', 'action_topic_namespace': 'action_topic_namespace', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1694 y:549
			OperatableStateMachine.add('wait_1',
										WaitState(wait_time=0.5),
										transitions={'done': 'moveToPregrasp'},
										autonomy={'done': Autonomy.Off})

			# x:1691 y:736
			OperatableStateMachine.add('wait_2',
										WaitState(wait_time=0.5),
										transitions={'done': 'moveToPick'},
										autonomy={'done': Autonomy.Off})

			# x:316 y:14
			OperatableStateMachine.add('wait_2_2',
										WaitState(wait_time=0.5),
										transitions={'done': 'transport_ conveyor_to_pick_location'},
										autonomy={'done': Autonomy.Off})

			# x:1423 y:629
			OperatableStateMachine.add('computePick',
										ComputeGraspAriacState(joint_names=joint_names),
										transitions={'continue': 'moveToPick', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'action_topic_namespace': 'action_topic_namespace', 'tool_link': 'tool_link', 'pose': 'pose', 'offset': 'offset', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
