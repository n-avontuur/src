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
from ariac_logistics_flexbe_states.get_material_locations import GetMaterialLocationsState
from ariac_support_flexbe_states.get_item_from_list_state import GetItemFromListState
from unit_2_flexbe_behaviors.a1_robots_home_sm import a1_Robots_HomeSM
from unit_2_flexbe_behaviors.a2_moverobot_sm import a2_MoveRobotSM
from unit_2_flexbe_behaviors.initgripper_sm import initGripperSM
from unit_2_flexbe_behaviors.locate_place_in_bin_with_content_sm import locate_Place_In_Bin_With_ContentSM
from unit_2_flexbe_behaviors.locate_place_in_empty_bin_sm import Locate_Place_In_Empty_BinSM
from unit_2_flexbe_behaviors.transport__conveyor_to_pick_unit2_location_sm import transport_conveyor_to_pick_unit2_locationSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri Jun 04 2021
@author: Niels Avontuur
'''
class a1_TotalProgramSM(Behavior):
	'''
	test voor hele programma in een keer
	'''


	def __init__(self):
		super(a1_TotalProgramSM, self).__init__()
		self.name = 'a1_TotalProgram'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(Locate_Place_In_Empty_BinSM, 'Locate_Place_In_Empty_Bin')
		self.add_behavior(a1_Robots_HomeSM, 'a1_Robots_Home')
		self.add_behavior(a2_MoveRobotSM, 'a2_MoveRobot')
		self.add_behavior(initGripperSM, 'initGripper')
		self.add_behavior(locate_Place_In_Bin_With_ContentSM, 'locate_Place_In_Bin_With_Content')
		self.add_behavior(transport_conveyor_to_pick_unit2_locationSM, 'transport_ conveyor_to_pick_unit2_location')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		joint_names = ['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
		# x:47 y:200, x:740 y:356
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.bin_Content = ['empty', 'empty', 'empty', 'empty', 'empty', 'empty']
		_state_machine.userdata.numberOfModels = 0
		_state_machine.userdata.robot_Name = ''
		_state_machine.userdata.zero = 0
		_state_machine.userdata.trueVariable = True
		_state_machine.userdata.falseVariable = False
		_state_machine.userdata.zeroFloat = 0.0

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:58 y:40
			OperatableStateMachine.add('start',
										StartAssignment(),
										transitions={'continue': 'setAllParts'},
										autonomy={'continue': Autonomy.Off})

			# x:409 y:33
			OperatableStateMachine.add('a1_Robots_Home',
										self.use_behavior(a1_Robots_HomeSM, 'a1_Robots_Home'),
										transitions={'finished': 'initGripper', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:1178 y:518
			OperatableStateMachine.add('a2_MoveRobot',
										self.use_behavior(a2_MoveRobotSM, 'a2_MoveRobot'),
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'pick_Offset': 'pick_Offset', 'pick_Rotation': 'pick_Rotation', 'robot_Name': 'robot_Name', 'preDrop_Config': 'preDrop_Config', 'prePick_Config': 'prePick_Config', 'bin_Pose': 'bin_Pose', 'drop_Offset': 'drop_Offset', 'drop_Rotation': 'drop_Rotation', 'pick_Pose': 'pick_Pose'})

			# x:1195 y:36
			OperatableStateMachine.add('getLocationOfAllParts',
										GetMaterialLocationsState(),
										transitions={'continue': 'getPartLocation'},
										autonomy={'continue': Autonomy.Off},
										remapping={'part': 'part_Type', 'material_locations': 'locations'})

			# x:1202 y:121
			OperatableStateMachine.add('getPartLocation',
										GetItemFromListState(),
										transitions={'done': 'locate_Place_In_Bin_With_Content', 'invalid_index': 'Locate_Place_In_Empty_Bin'},
										autonomy={'done': Autonomy.Off, 'invalid_index': Autonomy.Off},
										remapping={'list': 'locations', 'index': 'zero', 'item': 'bin'})

			# x:623 y:30
			OperatableStateMachine.add('initGripper',
										self.use_behavior(initGripperSM, 'initGripper'),
										transitions={'finished': 'transport_ conveyor_to_pick_unit2_location', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:1369 y:227
			OperatableStateMachine.add('locate_Place_In_Bin_With_Content',
										self.use_behavior(locate_Place_In_Bin_With_ContentSM, 'locate_Place_In_Bin_With_Content'),
										transitions={'finished': 'a2_MoveRobot', 'bin_Full': 'Locate_Place_In_Empty_Bin', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'bin_Full': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'bin': 'bin', 'part_Type': 'part_Type', 'gasket': 'gasket', 'piston': 'piston', 'gear': 'gear', 'robot_Name': 'robot_Name', 'pick_Offset': 'pick_Offset', 'pick_Rotation': 'pick_Rotation', 'bin_Pose': 'bin_Pose', 'drop_Offset': 'drop_Offset', 'drop_Rotation': 'drop_Rotation', 'prePick_Config': 'prePick_Config', 'preDrop_Config': 'preDrop_Config'})

			# x:198 y:43
			OperatableStateMachine.add('setAllParts',
										setFirstTimePart(),
										transitions={'continue': 'a1_Robots_Home', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'gasket': 'gasket', 'piston': 'piston', 'gear': 'gear'})

			# x:823 y:32
			OperatableStateMachine.add('transport_ conveyor_to_pick_unit2_location',
										self.use_behavior(transport_conveyor_to_pick_unit2_locationSM, 'transport_ conveyor_to_pick_unit2_location'),
										transitions={'finished': 'getLocationOfAllParts', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'pick_Pose': 'pick_Pose', 'part_Type': 'part_Type'})

			# x:1153 y:335
			OperatableStateMachine.add('Locate_Place_In_Empty_Bin',
										self.use_behavior(Locate_Place_In_Empty_BinSM, 'Locate_Place_In_Empty_Bin'),
										transitions={'finished': 'a2_MoveRobot', 'failed': 'failed', 'bin_Full': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit, 'bin_Full': Autonomy.Inherit},
										remapping={'part_Type': 'part_Type', 'gasket': 'gasket', 'piston': 'piston', 'gear': 'gear', 'bin_Content': 'bin_Content', 'pick_Offset': 'pick_Offset', 'pick_Rotation': 'pick_Rotation', 'drop_Offset': 'drop_Offset', 'drop_Rotation': 'drop_Rotation', 'preDrop_Config': 'preDrop_Config', 'prePick_Config': 'prePick_Config', 'robot_Name': 'robot_Name', 'bin_Pose': 'bin_Pose'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
