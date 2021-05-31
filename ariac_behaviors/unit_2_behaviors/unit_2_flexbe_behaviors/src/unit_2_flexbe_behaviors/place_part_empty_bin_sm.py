#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.getEmptyBin import getEmptyBin as ariac_flexbe_states__getEmptyBin
from ariac_flexbe_states.get_object_pose import GetObjectPoseState
from ariac_flexbe_states.lookup_from_table import LookupFromTableState
from ariac_flexbe_states.set_new_position import set_new_pose_part
from ariac_support_flexbe_states.equal_state import EqualState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sun May 30 2021
@author: Niels Avontuur
'''
class place_Part_Empty_BinSM(Behavior):
	'''
	placing parts in empty bin
	'''


	def __init__(self):
		super(place_Part_Empty_BinSM, self).__init__()
		self.name = 'place_Part_Empty_Bin'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		joint_names = ['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
		parameter_name = 'ariac_tables_unit2'
		# x:1625 y:87, x:782 y:331
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['part'])
		_state_machine.userdata.binPartType = ["empty","empty","empty","empty","empty","empty"]
		_state_machine.userdata.bin = ' '
		_state_machine.userdata.bin_frame = ' '
		_state_machine.userdata.ref_frame = 'world'
		_state_machine.userdata.pose_Piston_Part = [0,0,0]
		_state_machine.userdata.pose_Gear_Part = [0,0,0]
		_state_machine.userdata.pose_Gasket_Part = [0,0,0]
		_state_machine.userdata.part = ''
		_state_machine.userdata.robot1_Name = 'R1'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:91 y:66
			OperatableStateMachine.add('getEmptyBin',
										ariac_flexbe_states__getEmptyBin(),
										transitions={'continue': 'getBinPose', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'binPartType': 'binPartType', 'bin': 'bin', 'bin_frame': 'bin_frame', 'robot_name': 'robot_name'})

			# x:1068 y:49
			OperatableStateMachine.add('getPreGraspR1',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_configuration_R2', index_title='bin', column_title='robot_config'),
										transitions={'found': 'setNewPosition', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'congif_name'})

			# x:1055 y:119
			OperatableStateMachine.add('getPreGraspR2',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_configuration_R1', index_title='bin', column_title='robot_config'),
										transitions={'found': 'setNewPosition', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'congif_name'})

			# x:548 y:73
			OperatableStateMachine.add('lookUpOffset',
										LookupFromTableState(parameter_name=parameter_name, table_name='parts_offsets', index_title='part', column_title='offsetX'),
										transitions={'found': 'useR1', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'part', 'column_value': 'part_offset'})

			# x:1369 y:81
			OperatableStateMachine.add('setNewPosition',
										set_new_pose_part(),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'part_offset': 'part_offset'})

			# x:746 y:72
			OperatableStateMachine.add('useR1',
										EqualState(),
										transitions={'true': 'getPreGraspR1', 'false': 'getPreGraspR2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'robot_name', 'value_b': 'robot1_Name'})

			# x:283 y:64
			OperatableStateMachine.add('getBinPose',
										GetObjectPoseState(),
										transitions={'continue': 'lookUpOffset', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'frame': 'bin_frame', 'pose': 'pose'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
