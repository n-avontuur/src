#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.detect_part_camera_ariac_state import DetectPartCameraAriacState
from ariac_flexbe_states.lookup_from_table import LookupFromTableState
from ariac_flexbe_states.select_Robot import selectRobot
from ariac_flexbe_states.set_Part import setPart
from ariac_flexbe_states.set_new_position import set_new_pose_part
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
		# x:10 y:487, x:420 y:292
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['bin', 'partType', 'gear', 'gasket', 'piston'], output_keys=['bin', 'pose', 'gear', 'gasket', 'piston', 'config_name', 'robot_Name', 'pose_offset'])
		_state_machine.userdata.bin = '3'
		_state_machine.userdata.ref_frame = 'world'
		_state_machine.userdata.config_name = ''
		_state_machine.userdata.pose = [0,0,0]
		_state_machine.userdata.partType = 'piston_rod_part'
		_state_machine.userdata.gear = []
		_state_machine.userdata.piston = []
		_state_machine.userdata.gasket = []
		_state_machine.userdata.robot_Name = ' '
		_state_machine.userdata.robot1_Name = 'arm1'
		_state_machine.userdata.part = []
		_state_machine.userdata.pose_offset = []

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:40 y:94
			OperatableStateMachine.add('selectRobot',
										selectRobot(),
										transitions={'continue': 'setPartWithPartType', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'bin': 'bin', 'robot_name': 'robot_Name'})

			# x:345 y:413
			OperatableStateMachine.add('getPreGraspR1',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_configuration_R2', index_title='bin', column_title='robot_config'),
										transitions={'found': 'setNewPose', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'congif_name'})

			# x:556 y:483
			OperatableStateMachine.add('getPreGraspR2',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_configuration_R1', index_title='bin', column_title='robot_config'),
										transitions={'found': 'setNewPose', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'congif_name'})

			# x:431 y:95
			OperatableStateMachine.add('lookUpCarmeraFrame',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_configuration_R1', index_title='bin', column_title='camera_frame'),
										transitions={'found': 'lookUpCarmeraTopic', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'camera_frame'})

			# x:624 y:143
			OperatableStateMachine.add('lookUpCarmeraTopic',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_configuration_R1', index_title='bin', column_title='camera_topic'),
										transitions={'found': 'detectPartFromBin', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin', 'column_value': 'camera_topic'})

			# x:109 y:453
			OperatableStateMachine.add('setNewPose',
										set_new_pose_part(),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'part': 'part', 'pose': 'pose_offset'})

			# x:236 y:74
			OperatableStateMachine.add('setPartWithPartType',
										setPart(),
										transitions={'continue': 'lookUpCarmeraFrame', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'partType': 'partType', 'gasket': 'gasket', 'piston': 'piston', 'gear': 'gear', 'part': 'part'})

			# x:697 y:349
			OperatableStateMachine.add('useR1',
										EqualState(),
										transitions={'true': 'getPreGraspR1', 'false': 'getPreGraspR2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'robot_Name', 'value_b': 'robot1_Name'})

			# x:643 y:232
			OperatableStateMachine.add('detectPartFromBin',
										DetectPartCameraAriacState(time_out=0.5),
										transitions={'continue': 'useR1', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part', 'pose': 'pose', 'numberOfModels': 'numberOfModels'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
