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
from ariac_flexbe_states.compute_drop_ariac_state import ComputeDropState
from ariac_flexbe_states.create_dropPose import CreateDropPoseState
from ariac_flexbe_states.get_object_pose import GetObjectPoseState
from ariac_flexbe_states.moveit_to_joints_dyn_ariac_state import MoveitToJointsDynAriacState
from ariac_flexbe_states.set_Part import setPart
from ariac_flexbe_states.set_Part_FirstTime import setFirstTimePart
from ariac_flexbe_states.set_new_position import setNewPosePart
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from flexbe_states.wait_state import WaitState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sat Jun 05 2021
@author: Niels Avontuur
'''
class Test_Drop_movementSM(Behavior):
	'''
	This is for testing how to make a pose for dropping with offset's
	'''


	def __init__(self):
		super(Test_Drop_movementSM, self).__init__()
		self.name = 'Test_Drop_movement'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		joint_names = ['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
		# x:1402 y:174, x:130 y:463
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.preDrop_config = 'bin1PreGraspR2'
		_state_machine.userdata.move_group = 'manipulator'
		_state_machine.userdata.action_topic_namespace = '/ariac/arm2'
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.tool_link = 'ee_link'
		_state_machine.userdata.ref_frame = 'world'
		_state_machine.userdata.bin_frame = 'bin1_frame'
		_state_machine.userdata.part_Type = 'gear_part'
		_state_machine.userdata.numberOfModels = 4

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:42 y:49
			OperatableStateMachine.add('setPart',
										setFirstTimePart(),
										transitions={'continue': 'setPart_Content', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'gasket': 'gasket', 'piston': 'piston', 'gear': 'gear'})

			# x:366 y:135
			OperatableStateMachine.add('addOffsetPose',
										AddOffsetToPoseState(),
										transitions={'continue': 'moveToPreDrop'},
										autonomy={'continue': Autonomy.Off},
										remapping={'input_pose': 'bin_pose', 'offset_pose': 'offset_Drop_pose', 'output_pose': 'drop_Pose'})

			# x:936 y:132
			OperatableStateMachine.add('computeDrop',
										ComputeDropState(joint_names=joint_names),
										transitions={'continue': 'moveDrop', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'action_topic_namespace': 'action_topic_namespace', 'tool_link': 'tool_link', 'pose': 'drop_Pose', 'offset': 'drop_Offset', 'rotation': 'drop_Rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:365 y:41
			OperatableStateMachine.add('getBinPose',
										GetObjectPoseState(),
										transitions={'continue': 'addOffsetPose', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'frame': 'bin_frame', 'pose': 'bin_pose'})

			# x:1117 y:135
			OperatableStateMachine.add('moveDrop',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'finished', 'planning_failed': 'wait_2', 'control_failed': 'wait_2'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'action_topic_namespace': 'action_topic_namespace', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:712 y:134
			OperatableStateMachine.add('moveToPreDrop',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'computeDrop', 'planning_failed': 'wait', 'control_failed': 'wait', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'preDrop_config', 'move_group': 'move_group', 'action_topic_namespace': 'action_topic_namespace', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:195 y:46
			OperatableStateMachine.add('setNewPartOffsetPose',
										setNewPosePart(),
										transitions={'continue': 'CreateDropPose', 'failed': 'failed', 'bin_Full': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'bin_Full': Autonomy.Off},
										remapping={'part_Content': 'part_Content', 'numberOfModels': 'numberOfModels', 'drop_Offset': 'drop_Offset', 'pick_Offset': 'pick_Offset', 'drop_Rotation': 'drop_Rotation', 'pick_Rotation': 'pick_Rotation'})

			# x:42 y:138
			OperatableStateMachine.add('setPart_Content',
										setPart(),
										transitions={'continue': 'setNewPartOffsetPose', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'part_Type': 'part_Type', 'gasket': 'gasket', 'piston': 'piston', 'gear': 'gear', 'part_Content': 'part_Content'})

			# x:735 y:45
			OperatableStateMachine.add('wait',
										WaitState(wait_time=0.5),
										transitions={'done': 'moveToPreDrop'},
										autonomy={'done': Autonomy.Off})

			# x:1123 y:69
			OperatableStateMachine.add('wait_2',
										WaitState(wait_time=0.5),
										transitions={'done': 'moveDrop'},
										autonomy={'done': Autonomy.Off})

			# x:208 y:132
			OperatableStateMachine.add('CreateDropPose',
										CreateDropPoseState(),
										transitions={'continue': 'getBinPose', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'xyz': 'drop_Offset', 'rpy': 'drop_Rotation', 'pose': 'offset_Drop_pose'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
