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
from flexbe_states.log_key_state import LogKeyState
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
		# x:38 y:200, x:330 y:365, x:278 y:259
		_state_machine = OperatableStateMachine(outcomes=['finished', 'bin_Full', 'failed'], input_keys=['bin', 'part_Type', 'gasket', 'piston', 'gear'], output_keys=['part_Type', 'robot_Name', 'pick_Pose', 'pick_Offset', 'pick_Rotation', 'drop_Pose', 'drop_Offset', 'drop_Rotation', 'prePick_Config', 'preDrop_Config'])
		_state_machine.userdata.bin = 'bin4'
		_state_machine.userdata.ref_frame = 'world'
		_state_machine.userdata.part_Type = 'gear_part'
		_state_machine.userdata.robot_Name = ' '
		_state_machine.userdata.robot1_Name = 'arm1'
		_state_machine.userdata.pick_Pose = []
		_state_machine.userdata.pick_Offset = 0
		_state_machine.userdata.pick_Rotation = 0
		_state_machine.userdata.drop_Pose = []
		_state_machine.userdata.drop_Offset = []
		_state_machine.userdata.drop_Rotation = 0
		_state_machine.userdata.preDrop_Config = ''
		_state_machine.userdata.prePick_Config = ''
		_state_machine.userdata.gasket = []
		_state_machine.userdata.piston = []
		_state_machine.userdata.gear = []

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:49 y:60
			OperatableStateMachine.add('selectRobot',
										selectRobot(),
										transitions={'continue': 'setPartWithPartType', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'bin': 'bin', 'robot_Name': 'robot_Name'})

			# x:721 y:255
			OperatableStateMachine.add('detectNumberOfParts',
										DetectTotalPartCameraAriacState(time_out=0.5),
										transitions={'continue': 'getPreGraspR1', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part_Type', 'pose': 'pose', 'numberOfModels': 'numberOfModels'})

			# x:861 y:496
			OperatableStateMachine.add('detectNumberOfParts_2',
										DetectTotalPartCameraAriacState(time_out=0.5),
										transitions={'continue': 'getPreGraspR2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part_Type', 'pose': 'pose', 'numberOfModels': 'numberOfModels'})

			# x:257 y:448
			OperatableStateMachine.add('getPreGraspR1',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_configuration_R1', index_title='bin', column_title='robot_config'),
										transitions={'found': 'setNewPose', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'preDrop_Config'})

			# x:515 y:498
			OperatableStateMachine.add('getPreGraspR2',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_configuration_R2', index_title='bin', column_title='robot_config'),
										transitions={'found': 'setNewPose', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'preDrop_Config'})

			# x:709 y:117
			OperatableStateMachine.add('lookUpCarmeraFrame',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_configuration_R1', index_title='bin', column_title='camera_frame'),
										transitions={'found': 'lookUpCarmeraTopic', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'camera_frame'})

			# x:894 y:341
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

			# x:897 y:415
			OperatableStateMachine.add('lookUpCarmeraTopic_2',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_configuration_R1', index_title='bin', column_title='camera_topic'),
										transitions={'found': 'detectNumberOfParts_2', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'camera_topic'})

			# x:14 y:457
			OperatableStateMachine.add('setNewPose',
										setNewPosePart(),
										transitions={'continue': 'PrintRobotName', 'failed': 'failed', 'bin_Full': 'bin_Full'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'bin_Full': Autonomy.Off},
										remapping={'part_Content': 'part_Content', 'numberOfModels': 'numberOfModels', 'drop_Pose': 'drop_Pose', 'pick_Offset': 'pick_Offset'})

			# x:368 y:73
			OperatableStateMachine.add('setPartWithPartType',
										setPart(),
										transitions={'continue': 'useR1', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'part_Type': 'part_Type', 'gasket': 'gasket', 'piston': 'piston', 'gear': 'gear', 'part_Content': 'part_Content'})

			# x:886 y:52
			OperatableStateMachine.add('useR1',
										EqualState(),
										transitions={'true': 'lookUpCarmeraFrame', 'false': 'lookUpCarmeraFrame_2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'robot_Name', 'value_b': 'robot1_Name'})

			# x:20 y:316
			OperatableStateMachine.add('PrintRobotName',
										LogKeyState(text='pickOffset :', severity=Logger.REPORT_HINT),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'data': 'pick_Offset'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
