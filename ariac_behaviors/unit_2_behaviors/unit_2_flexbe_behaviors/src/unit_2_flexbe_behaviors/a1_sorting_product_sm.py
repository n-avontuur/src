#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.select_Robot import selectRobot
from ariac_flexbe_states.set_Part import setPart
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
		_state_machine.userdata.gasket_OffsetSize = [0.15,0.1,0.035]
		_state_machine.userdata.piston_OffsetSize = [0.11,0.11,0.02]
		_state_machine.userdata.gear_OffsetSize = [0.13,0.1,0.025]
		_state_machine.userdata.gasket_NumberOf = 0
		_state_machine.userdata.piston_NumberOf = 0
		_state_machine.userdata.gear_NumberOf = 0
		_state_machine.userdata.gasket_MaxNumberOf = [3,2]
		_state_machine.userdata.piston_MaxNumberOf = [3,3]
		_state_machine.userdata.gear_MaxNumberOf = [4,4]
		_state_machine.userdata.gasket_Offset = [0.0,0.0,0.0]
		_state_machine.userdata.piston_Offset = [0.0,0.0,0.0]
		_state_machine.userdata.gear_Offset = [0.0,0.0,0.0]
		_state_machine.userdata.gasket = [_state_machine.userdata.gasket_OffsetSize,_state_machine.userdata.gasket_NumberOf,_state_machine.userdata.gasket_MaxNumberOf,_state_machine.userdata.gasket_Offset]
		_state_machine.userdata.piston = [_state_machine.userdata.piston_OffsetSize,_state_machine.userdata.piston_NumberOf,_state_machine.userdata.piston_MaxNumberOf,_state_machine.userdata.piston_Offset]
		_state_machine.userdata.gear = [_state_machine.userdata.gear_OffsetSize,_state_machine.userdata.gear_NumberOf,_state_machine.userdata.gear_MaxNumberOf,_state_machine.userdata.gear_Offset]
		_state_machine.userdata.part_Content = []
		_state_machine.userdata.part_Type = ''
		_state_machine.userdata.bin = 'bin3'
		_state_machine.userdata.pick_rotation = []
		_state_machine.userdata.preDrop_Config = ''
		_state_machine.userdata.pick_offset = []

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:123 y:39
			OperatableStateMachine.add('startAssignment',
										StartAssignment(),
										transitions={'continue': 'transport_ conveyor_to_pick_location'},
										autonomy={'continue': Autonomy.Off})

			# x:807 y:52
			OperatableStateMachine.add('a1_setting_Parameters',
										self.use_behavior(a1_setting_ParametersSM, 'a1_setting_Parameters'),
										transitions={'finished': 'select_Robot', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part_Type': 'part_Type', 'gasket': 'gasket', 'piston': 'piston', 'gear': 'gear', 'bin_Content': 'bin_Content', 'drop_pose': 'drop_Pose', 'pose_offset': 'drop_Offset', 'PreDrop_config': 'preDrop_config', 'robot_Name': 'robot_Name', 'bin': 'bin'})

			# x:796 y:127
			OperatableStateMachine.add('select_Robot',
										selectRobot(),
										transitions={'continue': 'a1_Move_Robot', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'bin': 'bin', 'robot_name': 'robot_name'})

			# x:612 y:56
			OperatableStateMachine.add('set_PartContent',
										setPart(),
										transitions={'continue': 'a1_setting_Parameters', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'part_Type': 'part_Type', 'gasket': 'gasket', 'piston': 'piston', 'gear': 'gear', 'part': 'part_Content'})

			# x:327 y:46
			OperatableStateMachine.add('transport_ conveyor_to_pick_location',
										self.use_behavior(transport_conveyor_to_pick_locationSM, 'transport_ conveyor_to_pick_location'),
										transitions={'finished': 'set_PartContent', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'pick_Pose': 'pick_Pose', 'part_Type': 'part_Type'})

			# x:537 y:294
			OperatableStateMachine.add('a1_Move_Robot',
										self.use_behavior(a1_Move_RobotSM, 'a1_Move_Robot'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'pick_Pose': 'pick_Pose', 'pick_offset': 'pick_offset', 'pick_rotation': 'pick_rotation', 'drop_Pose': 'drop_Pose', 'drop_Offset': 'drop_Offset', 'drop_Offset': 'drop_Offset', 'robot_Name': 'robot_Name', 'preDrop_Config': 'preDrop_Config'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
