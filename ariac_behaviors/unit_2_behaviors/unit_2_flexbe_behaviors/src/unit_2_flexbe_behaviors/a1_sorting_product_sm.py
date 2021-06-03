#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.set_Part_FirstTime import setFirstTimePart
from ariac_flexbe_states.start_assignment_state import StartAssignment
from unit_2_flexbe_behaviors.a1_move_robot_sm import a1_Move_RobotSM
from unit_2_flexbe_behaviors.a1_setting_parameters_sm import a1_setting_ParametersSM
from unit_2_flexbe_behaviors.transport__conveyor_to_pick_location_sm import transport_conveyor_to_pick_locationSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Mon May 31 2021
@author: Niels Avontuur
'''
class a1_Sorting_ProductSM(Behavior):
	'''
	This behavior is the main behavior for sorting of product
	'''


	def __init__(self):
		super(a1_Sorting_ProductSM, self).__init__()
		self.name = 'a1_Sorting_Product'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(a1_Move_RobotSM, 'a1_Move_Robot')
		self.add_behavior(a1_setting_ParametersSM, 'a1_setting_Parameters')
		self.add_behavior(transport_conveyor_to_pick_locationSM, 'transport_ conveyor_to_pick_location')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1325 y:289, x:130 y:463
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.bin_Content = ['empty','empty', 'empty', 'empty', 'empty', 'empty']

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:97 y:33
			OperatableStateMachine.add('startAssignment',
										StartAssignment(),
										transitions={'continue': 'setFirstTimePart'},
										autonomy={'continue': Autonomy.Off})

			# x:655 y:116
			OperatableStateMachine.add('a1_setting_Parameters',
										self.use_behavior(a1_setting_ParametersSM, 'a1_setting_Parameters'),
										transitions={'finished': 'a1_Move_Robot', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part_Type': 'part_Type', 'gasket': 'gasket', 'piston': 'piston', 'gear': 'gear', 'bin_Content': 'bin_Content', 'robot_Name': 'robot_Name', 'pick_Pose': 'pick_Pose', 'pick_Offset': 'pick_Offset', 'pick_Rotation': 'pick_Rotation', 'drop_Pose': 'drop_Pose', 'drop_Offset': 'drop_Offset', 'drop_Rotation': 'drop_Rotation', 'preDrop_Config': 'preDrop_Config', 'prePick_Config': 'prePick_Config'})

			# x:78 y:113
			OperatableStateMachine.add('setFirstTimePart',
										setFirstTimePart(),
										transitions={'continue': 'transport_ conveyor_to_pick_location', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'gasket': 'gasket', 'piston': 'piston', 'gear': 'gear', 'gasket_offset': 'gasket_offset', 'piston_offset': 'piston_offset', 'gear_offset': 'gear_offset'})

			# x:241 y:112
			OperatableStateMachine.add('transport_ conveyor_to_pick_location',
										self.use_behavior(transport_conveyor_to_pick_locationSM, 'transport_ conveyor_to_pick_location'),
										transitions={'finished': 'a1_setting_Parameters', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'pick_Pose': 'pick_Pose', 'part_Type': 'part_Type'})

			# x:396 y:419
			OperatableStateMachine.add('a1_Move_Robot',
										self.use_behavior(a1_Move_RobotSM, 'a1_Move_Robot'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'pick_Pose': 'pick_Pose', 'pick_Offset': 'pick_Offset', 'pick_Rotation': 'pick_Rotation', 'drop_Pose': 'drop_Pose', 'drop_Offset': 'drop_Offset', 'drop_Rotation': 'drop_Rotation', 'prePick_Config': 'prePick_Config', 'preDrop_Config': 'preDrop_Config', 'pick_Offset': 'pick_Offset', 'robot_Name': 'robot_Name'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
