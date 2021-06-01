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
from ariac_flexbe_states.set_Part_FirstTime import setFirstTimePart
from ariac_flexbe_states.set_new_position import setNewPosePart
from ariac_support_flexbe_states.equal_state import EqualState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sun May 30 2021
@author: Niels Avontuur
'''
class Locate_Place_In_Empty_BinSM(Behavior):
	'''
	Locating a place for the part in an empty bin
	'''


	def __init__(self):
		super(Locate_Place_In_Empty_BinSM, self).__init__()
		self.name = 'Locate_Place_In_Empty_Bin'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		parameter_name = '/ariac_tables_unit2'
		# x:35 y:290, x:213 y:236, x:230 y:350
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed', 'bin_Full'], input_keys=['part_Type', 'gasket', 'piston', 'gear', 'bin_Content'], output_keys=['drop_pose', 'pose_offset', 'PreDrop_config', 'robot_Name', 'part_Type', 'gear', 'gasket', 'piston'])
		_state_machine.userdata.bin_Content = ["empty","empty","empty","empty","empty","empty"]
		_state_machine.userdata.bin = ' '
		_state_machine.userdata.bin_frame = ' '
		_state_machine.userdata.ref_frame = 'world'
		_state_machine.userdata.part_Type = 'gear_part'
		_state_machine.userdata.gear = []
		_state_machine.userdata.piston = []
		_state_machine.userdata.gasket = []
		_state_machine.userdata.robot_Name = ' '
		_state_machine.userdata.robot1_Name = 'arm1'
		_state_machine.userdata.pose_offset = []
		_state_machine.userdata.drop_pose = []
		_state_machine.userdata.part_Content = []
		_state_machine.userdata.PreDrop_config = ''

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:73 y:80
			OperatableStateMachine.add('getEmptyBin',
										getEmptyBin(),
										transitions={'continue': 'setFirstTimeParts', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'binPartType': 'bin_Content', 'bin': 'bin', 'bin_frame': 'bin_frame', 'robot_name': 'robot_name'})

			# x:439 y:345
			OperatableStateMachine.add('getPreGraspR1',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_configuration_R2', index_title='bin', column_title='robot_config'),
										transitions={'found': 'setNewOffsetPosition', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'PreDrop_config'})

			# x:429 y:429
			OperatableStateMachine.add('getPreGraspR2',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_configuration_R1', index_title='bin', column_title='robot_config'),
										transitions={'found': 'setNewOffsetPosition', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'PreDrop_config'})

			# x:668 y:114
			OperatableStateMachine.add('selectRobot',
										selectRobot(),
										transitions={'continue': 'getBinPose', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'bin': 'bin', 'robot_name': 'robot_name'})

			# x:313 y:58
			OperatableStateMachine.add('setFirstTimeParts',
										setFirstTimePart(),
										transitions={'continue': 'setPartWithPartType', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'gasket': 'gasket', 'piston': 'piston', 'gear': 'gear'})

			# x:152 y:390
			OperatableStateMachine.add('setNewOffsetPosition',
										setNewPosePart(),
										transitions={'continue': 'finished', 'failed': 'failed', 'bin_Full': 'bin_Full'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'bin_Full': Autonomy.Off},
										remapping={'part_Content': 'part_Content', 'pose_offset': 'pose_offset'})

			# x:635 y:43
			OperatableStateMachine.add('setPartWithPartType',
										setPart(),
										transitions={'continue': 'selectRobot', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'part_Type': 'part_Type', 'gasket': 'gasket', 'piston': 'piston', 'gear': 'gear', 'part_Content': 'part_Content'})

			# x:682 y:391
			OperatableStateMachine.add('useR1',
										EqualState(),
										transitions={'true': 'getPreGraspR1', 'false': 'getPreGraspR2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'robot_name', 'value_b': 'robot1_Name'})

			# x:680 y:285
			OperatableStateMachine.add('getBinPose',
										GetObjectPoseState(),
										transitions={'continue': 'useR1', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'frame': 'bin_frame', 'pose': 'drop_pose'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
