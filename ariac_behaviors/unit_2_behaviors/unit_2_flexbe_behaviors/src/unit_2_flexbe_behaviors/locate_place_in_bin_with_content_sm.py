#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.detect_total_part_camera_ariac_state import DetectTotalPartCameraAriacState
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
Created on Mon May 31 2021
@author: Niels Avontuur
'''
class locate_Place_In_Bin_With_ContentSM(Behavior):
	'''
	place parts in bin's with content
	'''


	def __init__(self):
		super(locate_Place_In_Bin_With_ContentSM, self).__init__()
		self.name = 'locate_Place_In_Bin_With_Content'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		parameter_name = '/ariac_tables_unit2'
		# x:27 y:280, x:243 y:253, x:580 y:384, x:330 y:365
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed', 'not_found', 'bin_Full'], input_keys=['bin', 'part_Type'], output_keys=['drop_pose', 'pose_offset', 'PreDrop_config', 'robot_Name', 'part_Type'])
		_state_machine.userdata.bin = 'bin4'
		_state_machine.userdata.ref_frame = 'world'
		_state_machine.userdata.PreDrop_config = ''
		_state_machine.userdata.drop_pose = []
		_state_machine.userdata.part_Type = 'gear_part'
		_state_machine.userdata.robot_Name = ' '
		_state_machine.userdata.robot1_Name = 'arm1'
		_state_machine.userdata.pose_offset = []

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:49 y:60
			OperatableStateMachine.add('selectRobot',
										selectRobot(),
										transitions={'continue': 'setPartFirstTime', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'bin': 'bin', 'robot_name': 'robot_Name'})

			# x:1014 y:470
			OperatableStateMachine.add('detectNumberOfParts_2',
										DetectTotalPartCameraAriacState(time_out=0.5),
										transitions={'continue': 'getPreGraspR2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part_Type', 'pose': 'pose', 'numberOfModels': 'numberOfModels'})

			# x:176 y:592
			OperatableStateMachine.add('getPreGraspR1',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_configuration_R1', index_title='bin', column_title='robot_config'),
										transitions={'found': 'setNewPose', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'PreDrop_config'})

			# x:577 y:661
			OperatableStateMachine.add('getPreGraspR2',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_configuration_R2', index_title='bin', column_title='robot_config'),
										transitions={'found': 'setNewPose', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'PreDrop_config'})

			# x:709 y:117
			OperatableStateMachine.add('lookUpCarmeraFrame',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_configuration_R1', index_title='bin', column_title='camera_frame'),
										transitions={'found': 'lookUpCarmeraTopic', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'camera_frame'})

			# x:1045 y:318
			OperatableStateMachine.add('lookUpCarmeraFrame_2',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_configuration_R1', index_title='bin', column_title='camera_frame'),
										transitions={'found': 'lookUpCarmeraTopic_2', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'camera_frame'})

			# x:708 y:185
			OperatableStateMachine.add('lookUpCarmeraTopic',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_configuration_R1', index_title='bin', column_title='camera_topic'),
										transitions={'found': 'detectNumberOfParts', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'camera_topic'})

			# x:1052 y:385
			OperatableStateMachine.add('lookUpCarmeraTopic_2',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_configuration_R1', index_title='bin', column_title='camera_topic'),
										transitions={'found': 'detectNumberOfParts_2', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'camera_topic'})

			# x:14 y:457
			OperatableStateMachine.add('setNewPose',
										setNewPosePart(),
										transitions={'continue': 'finished', 'failed': 'failed', 'bin_Full': 'bin_Full'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'bin_Full': Autonomy.Off},
										remapping={'part_Content': 'part_Content', 'numberOfModels': 'numberOfModels', 'pose_offset': 'pose_offset'})

			# x:202 y:48
			OperatableStateMachine.add('setPartFirstTime',
										setFirstTimePart(),
										transitions={'continue': 'setPartWithPartType', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'gasket': 'gasket', 'piston': 'piston', 'gear': 'gear', 'gasket_offset': 'gasket_offset', 'piston_offset': 'piston_offset', 'gear_offset': 'gear_offset'})

			# x:368 y:73
			OperatableStateMachine.add('setPartWithPartType',
										setPart(),
										transitions={'continue': 'useR1', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'part_Type': 'part_Type', 'gasket': 'gasket', 'piston': 'piston', 'gear': 'gear', 'part_Content': 'part_Content'})

			# x:938 y:54
			OperatableStateMachine.add('useR1',
										EqualState(),
										transitions={'true': 'lookUpCarmeraFrame', 'false': 'lookUpCarmeraFrame_2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'robot_Name', 'value_b': 'robot1_Name'})

			# x:721 y:255
			OperatableStateMachine.add('detectNumberOfParts',
										DetectTotalPartCameraAriacState(time_out=0.5),
										transitions={'continue': 'getPreGraspR1', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part_Type', 'pose': 'pose', 'numberOfModels': 'numberOfModels'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
