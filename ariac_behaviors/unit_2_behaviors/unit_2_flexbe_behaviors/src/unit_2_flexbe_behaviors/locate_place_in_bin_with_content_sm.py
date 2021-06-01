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
		parameter_name = 'ariac_tables_unit2'
		# x:27 y:280, x:243 y:253, x:608 y:437
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed', 'not_found'], input_keys=['bin', 'part_Type', 'gear', 'gasket', 'piston'], output_keys=['drop_pose', 'pose_offset', 'PreDrop_config', 'robot_Name', 'part_Type', 'gear', 'gasket', 'piston'])
		_state_machine.userdata.bin = 'bin3'
		_state_machine.userdata.ref_frame = 'world'
		_state_machine.userdata.PreDrop_config = ''
		_state_machine.userdata.drop_pose = []
		_state_machine.userdata.part_Type = 'piston_rod_part'
		_state_machine.userdata.gear = []
		_state_machine.userdata.piston = []
		_state_machine.userdata.gasket = []
		_state_machine.userdata.robot_Name = ' '
		_state_machine.userdata.robot1_Name = 'arm1'
		_state_machine.userdata.part_Content = []
		_state_machine.userdata.pose_offset = []

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:49 y:60
			OperatableStateMachine.add('selectRobot',
										selectRobot(),
										transitions={'continue': 'setPartWithPartType', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'bin': 'bin', 'robot_name': 'robot_Name'})

			# x:623 y:527
			OperatableStateMachine.add('detectNumberOfParts_2',
										DetectTotalPartCameraAriacState(time_out=0.5),
										transitions={'continue': 'getPreGraspR2', 'failed': 'failed', 'not_found': 'not_found'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part_Type', 'pose': 'pose', 'numberOfModels': 'numberOfModels'})

			# x:199 y:419
			OperatableStateMachine.add('getPreGraspR1',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_configuration_R2', index_title='bin', column_title='robot_config'),
										transitions={'found': 'setNewPose', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'PreDrop_config'})

			# x:330 y:497
			OperatableStateMachine.add('getPreGraspR2',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_configuration_R1', index_title='bin', column_title='robot_config'),
										transitions={'found': 'setNewPose', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'PreDrop_config'})

			# x:508 y:139
			OperatableStateMachine.add('lookUpCarmeraFrame',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_configuration_R1', index_title='bin', column_title='camera_frame'),
										transitions={'found': 'lookUpCarmeraTopic', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'camera_frame'})

			# x:712 y:318
			OperatableStateMachine.add('lookUpCarmeraFrame_2',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_configuration_R1', index_title='bin', column_title='camera_frame'),
										transitions={'found': 'lookUpCarmeraTopic_2', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'camera_frame'})

			# x:506 y:199
			OperatableStateMachine.add('lookUpCarmeraTopic',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_configuration_R1', index_title='bin', column_title='camera_topic'),
										transitions={'found': 'detectNumberOfParts', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'camera_topic'})

			# x:705 y:390
			OperatableStateMachine.add('lookUpCarmeraTopic_2',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_configuration_R1', index_title='bin', column_title='camera_topic'),
										transitions={'found': 'detectNumberOfParts_2', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'camera_topic'})

			# x:14 y:457
			OperatableStateMachine.add('setNewPose',
										setNewPosePart(),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'part_Content': 'part_Content', 'pose_offset': 'pose_offset'})

			# x:236 y:74
			OperatableStateMachine.add('setPartWithPartType',
										setPart(),
										transitions={'continue': 'useR1', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'partType': 'part_Type', 'gasket': 'gasket', 'piston': 'piston', 'gear': 'gear', 'part': 'part_Contect'})

			# x:635 y:42
			OperatableStateMachine.add('useR1',
										EqualState(),
										transitions={'true': 'lookUpCarmeraFrame', 'false': 'lookUpCarmeraFrame_2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'robot_Name', 'value_b': 'robot1_Name'})

			# x:467 y:261
			OperatableStateMachine.add('detectNumberOfParts',
										DetectTotalPartCameraAriacState(time_out=0.5),
										transitions={'continue': 'getPreGraspR1', 'failed': 'failed', 'not_found': 'not_found'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part_Type', 'pose': 'pose', 'numberOfModels': 'numberOfModels'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
