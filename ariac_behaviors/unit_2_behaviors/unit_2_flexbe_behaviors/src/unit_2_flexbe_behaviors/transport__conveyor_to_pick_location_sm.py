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
from ariac_flexbe_states.set_conveyorbelt_power_state import SetConveyorbeltPowerState
from flexbe_states.subscriber_state import SubscriberState
from flexbe_states.wait_state import WaitState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu May 27 2021
@author: niels avontuur
'''
class transport_conveyor_to_pick_locationSM(Behavior):
	'''
	For starting conveyor and stopping if part is in the right place
	'''


	def __init__(self):
		super(transport_conveyor_to_pick_locationSM, self).__init__()
		self.name = 'transport_ conveyor_to_pick_location'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		breakbeam = "/ariac/break_beam_1_change"
		part_list = ['gasket_part', 'piston_rod_part', 'gear_part', ' pulley_part', 'disk_part']
		# x:1612 y:75, x:578 y:357
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], output_keys=['pick_Pose', 'part_Type'])
		_state_machine.userdata.powerOFF = 0
		_state_machine.userdata.powerON = 100
		_state_machine.userdata.part_Type = ''
		_state_machine.userdata.pick_Pose = []
		_state_machine.userdata.ref_frame = 'world'
		_state_machine.userdata.camera_topic = '/ariac/logical_camera_1'
		_state_machine.userdata.camera_frame = 'logical_camera_1_frame'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:138 y:59
			OperatableStateMachine.add('wait_2',
										WaitState(wait_time=0.5),
										transitions={'done': 'conveyorON'},
										autonomy={'done': Autonomy.Off})

			# x:831 y:111
			OperatableStateMachine.add('conveyorOFF',
										SetConveyorbeltPowerState(),
										transitions={'continue': 'detectPartOnConveyor', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'power': 'powerOFF'})

			# x:301 y:62
			OperatableStateMachine.add('conveyorON',
										SetConveyorbeltPowerState(),
										transitions={'continue': 'wait', 'fail': 'failed'},
										autonomy={'continue': Autonomy.Off, 'fail': Autonomy.Off},
										remapping={'power': 'powerON'})

			# x:1055 y:52
			OperatableStateMachine.add('detectPartOnConveyor',
										DetectFirstPartCameraAriacState(part_list=part_list, time_out=0.5),
										transitions={'continue': 'finished', 'failed': 'failed', 'not_found': 'conveyorON'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part_Type', 'pose': 'pick_Pose'})

			# x:511 y:106
			OperatableStateMachine.add('wait',
										WaitState(wait_time=0.5),
										transitions={'done': 'checkBreamBeam'},
										autonomy={'done': Autonomy.Off})

			# x:637 y:102
			OperatableStateMachine.add('checkBreamBeam',
										SubscriberState(topic=breakbeam, blocking=True, clear=True),
										transitions={'received': 'conveyorOFF', 'unavailable': 'failed'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
