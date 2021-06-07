#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.detect_first_part_camera_ariac_state import DetectFirstPartCameraAriacState
from ariac_flexbe_states.lookup_from_table import LookupFromTableState
from ariac_flexbe_states.set_Bin_PartType import setBinPartType
from flexbe_states.log_state import LogState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sat May 29 2021
@author: niels avontuur
'''
class GetLocationPartsBinsV2SM(Behavior):
	'''
	Add part to bin content
	'''


	def __init__(self):
		super(GetLocationPartsBinsV2SM, self).__init__()
		self.name = 'GetLocationPartsBinsV2'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		parameter_name = '/ariac_tables_unit2'
		part_list = ['gasket_part', 'piston_rod_part', 'gear_part', ' pulley_part', 'disk_part']
		# x:1347 y:560, x:562 y:770
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['bin_Content'], output_keys=['bin_Content'])
		_state_machine.userdata.part_Type = []
		_state_machine.userdata.locations = []
		_state_machine.userdata.zero = 0
		_state_machine.userdata.gasket = 'gasket_part'
		_state_machine.userdata.piston = 'piston_rod_part'
		_state_machine.userdata.gear = 'gear_part'
		_state_machine.userdata.bin1 = 'bin1'
		_state_machine.userdata.bin2 = 'bin2'
		_state_machine.userdata.bin3 = 'bin3'
		_state_machine.userdata.bin4 = 'bin4'
		_state_machine.userdata.bin6 = 'bin5'
		_state_machine.userdata.bin5 = 'bin6'
		_state_machine.userdata.ref_frame = 'world'
		_state_machine.userdata.bin_Content = [['empty','x'], ['empty','x'], ['empty','x'], ['empty','x'], ['empty','x'], ['empty','x']]
		_state_machine.userdata.bin = ''
		_state_machine.userdata.status = 'used'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:82 y:65
			OperatableStateMachine.add('bin 1',
										LogState(text='bin1', severity=Logger.REPORT_HINT),
										transitions={'done': 'lookUpTopic'},
										autonomy={'done': Autonomy.Off})

			# x:64 y:171
			OperatableStateMachine.add('bin 2',
										LogState(text='bin2', severity=Logger.REPORT_HINT),
										transitions={'done': 'lookUpTopic_2'},
										autonomy={'done': Autonomy.Off})

			# x:68 y:264
			OperatableStateMachine.add('bin 3',
										LogState(text='bin3', severity=Logger.REPORT_HINT),
										transitions={'done': 'lookUpTopic_3'},
										autonomy={'done': Autonomy.Off})

			# x:69 y:343
			OperatableStateMachine.add('bin 4',
										LogState(text='bin4', severity=Logger.REPORT_HINT),
										transitions={'done': 'lookUpTopic_4'},
										autonomy={'done': Autonomy.Off})

			# x:71 y:420
			OperatableStateMachine.add('bin 5',
										LogState(text='bin5', severity=Logger.REPORT_HINT),
										transitions={'done': 'lookUpTopic_5'},
										autonomy={'done': Autonomy.Off})

			# x:76 y:532
			OperatableStateMachine.add('bin 6',
										LogState(text='bin6', severity=Logger.REPORT_HINT),
										transitions={'done': 'lookUpTopic_6'},
										autonomy={'done': Autonomy.Off})

			# x:763 y:43
			OperatableStateMachine.add('detectPartInBin',
										DetectFirstPartCameraAriacState(part_list=part_list, time_out=0.5),
										transitions={'continue': 'setPartTypeInBins', 'failed': 'failed', 'not_found': 'bin 2'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part_Type', 'pose': 'pose'})

			# x:763 y:135
			OperatableStateMachine.add('detectPartInBin_2',
										DetectFirstPartCameraAriacState(part_list=part_list, time_out=0.5),
										transitions={'continue': 'setPartTypeInBins_2', 'failed': 'failed', 'not_found': 'bin 3'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part_Type', 'pose': 'pose'})

			# x:763 y:227
			OperatableStateMachine.add('detectPartInBin_3',
										DetectFirstPartCameraAriacState(part_list=part_list, time_out=0.5),
										transitions={'continue': 'setPartTypeInBins_3', 'failed': 'failed', 'not_found': 'bin 4'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part_Type', 'pose': 'pose'})

			# x:763 y:319
			OperatableStateMachine.add('detectPartInBin_4',
										DetectFirstPartCameraAriacState(part_list=part_list, time_out=0.5),
										transitions={'continue': 'setPartTypeInBins_4', 'failed': 'failed', 'not_found': 'bin 5'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part_Type', 'pose': 'pose'})

			# x:763 y:411
			OperatableStateMachine.add('detectPartInBin_5',
										DetectFirstPartCameraAriacState(part_list=part_list, time_out=0.5),
										transitions={'continue': 'setPartTypeInBins_5', 'failed': 'failed', 'not_found': 'bin 6'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part_Type', 'pose': 'pose'})

			# x:751 y:534
			OperatableStateMachine.add('detectPartInBin_6',
										DetectFirstPartCameraAriacState(part_list=part_list, time_out=0.5),
										transitions={'continue': 'setPartTypeInBins_6', 'failed': 'failed', 'not_found': 'finished'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part_Type', 'pose': 'pose'})

			# x:487 y:57
			OperatableStateMachine.add('lookUpFrame',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_Camera', index_title='bin', column_title='camera_frame'),
										transitions={'found': 'detectPartInBin', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin1', 'column_value': 'camera_frame'})

			# x:487 y:154
			OperatableStateMachine.add('lookUpFrame_2',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_Camera', index_title='bin', column_title='camera_frame'),
										transitions={'found': 'detectPartInBin_2', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin2', 'column_value': 'camera_frame'})

			# x:494 y:253
			OperatableStateMachine.add('lookUpFrame_3',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_Camera', index_title='bin', column_title='camera_frame'),
										transitions={'found': 'detectPartInBin_3', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin3', 'column_value': 'camera_frame'})

			# x:499 y:332
			OperatableStateMachine.add('lookUpFrame_4',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_Camera', index_title='bin', column_title='camera_frame'),
										transitions={'found': 'detectPartInBin_4', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin4', 'column_value': 'camera_frame'})

			# x:489 y:416
			OperatableStateMachine.add('lookUpFrame_5',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_Camera', index_title='bin', column_title='camera_frame'),
										transitions={'found': 'detectPartInBin_5', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin5', 'column_value': 'camera_frame'})

			# x:490 y:538
			OperatableStateMachine.add('lookUpFrame_6',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_Camera', index_title='bin', column_title='camera_frame'),
										transitions={'found': 'detectPartInBin_6', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin6', 'column_value': 'camera_frame'})

			# x:254 y:52
			OperatableStateMachine.add('lookUpTopic',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_Camera', index_title='bin', column_title='camera_topic'),
										transitions={'found': 'lookUpFrame', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin1', 'column_value': 'camera_topic'})

			# x:254 y:168
			OperatableStateMachine.add('lookUpTopic_2',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_Camera', index_title='bin', column_title='camera_topic'),
										transitions={'found': 'lookUpFrame_2', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin2', 'column_value': 'camera_topic'})

			# x:254 y:260
			OperatableStateMachine.add('lookUpTopic_3',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_Camera', index_title='bin', column_title='camera_topic'),
										transitions={'found': 'lookUpFrame_3', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin3', 'column_value': 'camera_topic'})

			# x:257 y:350
			OperatableStateMachine.add('lookUpTopic_4',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_Camera', index_title='bin', column_title='camera_topic'),
										transitions={'found': 'lookUpFrame_4', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin4', 'column_value': 'camera_topic'})

			# x:257 y:427
			OperatableStateMachine.add('lookUpTopic_5',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_Camera', index_title='bin', column_title='camera_topic'),
										transitions={'found': 'lookUpFrame_5', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin5', 'column_value': 'camera_topic'})

			# x:260 y:535
			OperatableStateMachine.add('lookUpTopic_6',
										LookupFromTableState(parameter_name=parameter_name, table_name='bin_Camera', index_title='bin', column_title='camera_topic'),
										transitions={'found': 'lookUpFrame_6', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'index_value': 'bin6', 'column_value': 'camera_topic'})

			# x:1009 y:52
			OperatableStateMachine.add('setPartTypeInBins',
										setBinPartType(),
										transitions={'continue': 'bin 2'},
										autonomy={'continue': Autonomy.Off},
										remapping={'status': 'status', 'bin': 'bin1', 'part_Type': 'part_Type', 'bin_Content': 'bin_Content'})

			# x:1009 y:129
			OperatableStateMachine.add('setPartTypeInBins_2',
										setBinPartType(),
										transitions={'continue': 'bin 3'},
										autonomy={'continue': Autonomy.Off},
										remapping={'status': 'status', 'bin': 'bin2', 'part_Type': 'part_Type', 'bin_Content': 'bin_Content'})

			# x:1009 y:221
			OperatableStateMachine.add('setPartTypeInBins_3',
										setBinPartType(),
										transitions={'continue': 'bin 4'},
										autonomy={'continue': Autonomy.Off},
										remapping={'status': 'status', 'bin': 'bin3', 'part_Type': 'part_Type', 'bin_Content': 'bin_Content'})

			# x:1009 y:313
			OperatableStateMachine.add('setPartTypeInBins_4',
										setBinPartType(),
										transitions={'continue': 'lookUpTopic_5'},
										autonomy={'continue': Autonomy.Off},
										remapping={'status': 'status', 'bin': 'bin4', 'part_Type': 'part_Type', 'bin_Content': 'bin_Content'})

			# x:1009 y:405
			OperatableStateMachine.add('setPartTypeInBins_5',
										setBinPartType(),
										transitions={'continue': 'bin 6'},
										autonomy={'continue': Autonomy.Off},
										remapping={'status': 'status', 'bin': 'bin5', 'part_Type': 'part_Type', 'bin_Content': 'bin_Content'})

			# x:995 y:505
			OperatableStateMachine.add('setPartTypeInBins_6',
										setBinPartType(),
										transitions={'continue': 'finished'},
										autonomy={'continue': Autonomy.Off},
										remapping={'status': 'status', 'bin': 'bin6', 'part_Type': 'part_Type', 'bin_Content': 'bin_Content'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
