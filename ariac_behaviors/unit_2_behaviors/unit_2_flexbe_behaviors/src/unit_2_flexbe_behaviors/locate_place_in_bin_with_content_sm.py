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
from ariac_flexbe_states.getBinFrame import getBinFrame
from ariac_flexbe_states.get_New_Bin_PartType import getNewBinPartType
from ariac_flexbe_states.get_object_pose import GetObjectPoseState
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
		parameter_name = '/ariac_tables_unit2'
		# x:38 y:214, x:164 y:154, x:278 y:259, x:181 y:216
		_state_machine = OperatableStateMachine(outcomes=['finished', 'getEmptyBin', 'failed', 'system_Full'], input_keys=['bin', 'part_Type', 'gasket', 'piston', 'gear', 'bin_Content'], output_keys=['part_Type', 'robot_Name', 'pick_Offset', 'pick_Rotation', 'bin_Pose', 'drop_Offset', 'drop_Rotation', 'prePick_Config', 'preDrop_Config'])
		_state_machine.userdata.bin = ''
		_state_machine.userdata.ref_frame = 'world'
		_state_machine.userdata.part_Type = 'gear_part'
		_state_machine.userdata.robot_Name = ' '
		_state_machine.userdata.robot1_Name = 'arm1'
		_state_machine.userdata.pick_Offset = []
		_state_machine.userdata.pick_Rotation = 0.0
		_state_machine.userdata.bin_Pose = []
		_state_machine.userdata.drop_Offset = []
		_state_machine.userdata.drop_Rotation = 0.0
		_state_machine.userdata.preDrop_Config = ''
		_state_machine.userdata.prePick_Config = ''
		_state_machine.userdata.gasket = []
		_state_machine.userdata.piston = []
		_state_machine.userdata.gear = []
		_state_machine.userdata.bin_Content = []

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:49 y:60
			OperatableStateMachine.add('selectRobot',
										selectRobot(),
										transitions={'continue': 'getBinFrame', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'bin': 'bin', 'robot_Name': 'robot_Name'})

			# x:861 y:496
			OperatableStateMachine.add('detectNumberOfParts_2',
										DetectTotalPartCameraAriacState(time_out=0.5),
										transitions={'continue': 'getPreGraspR2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part_Type', 'pose': 'pose', 'numberOfModels': 'numberOfModels'})

			# x:244 y:62
			OperatableStateMachine.add('getBinFrame',
										getBinFrame(),
										transitions={'continue': 'getBinPose'},
										autonomy={'continue': Autonomy.Off},
										remapping={'bin': 'bin', 'bin_frame': 'bin_frame'})

			# x:431 y:44
			OperatableStateMachine.add('getBinPose',
										GetObjectPoseState(),
										transitions={'continue': 'setPartWithPartType', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'frame': 'bin_frame', 'pose': 'bin_Pose'})

			# x:59 y:260
			OperatableStateMachine.add('getNewBinWithPartType',
										getNewBinPartType(),
										transitions={'continue': 'selectRobot', 'findEmptyBin': 'getEmptyBin', 'system_Full': 'system_Full'},
										autonomy={'continue': Autonomy.Off, 'findEmptyBin': Autonomy.Off, 'system_Full': Autonomy.Off},
										remapping={'bin': 'bin', 'part_Type': 'part_Type', 'bin_Content': 'bin_Content', 'bin_frame': 'bin_frame'})

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
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_configuration_R2', index_title='bin', column_title='camera_frame'),
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
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_configuration_R2', index_title='bin', column_title='camera_topic'),
										transitions={'found': 'detectNumberOfParts_2', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'camera_topic'})

			# x:14 y:457
			OperatableStateMachine.add('setNewPose',
										setNewPosePart(),
										transitions={'continue': 'finished', 'failed': 'failed', 'bin_Full': 'getNewBinWithPartType'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'bin_Full': Autonomy.Off},
										remapping={'part_Content': 'part_Content', 'numberOfModels': 'numberOfModels', 'drop_Offset': 'drop_Offset', 'pick_Offset': 'pick_Offset', 'drop_Rotation': 'drop_Rotation', 'pick_Rotation': 'pick_Rotation'})

			# x:689 y:41
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
