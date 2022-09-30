#!/usr/bin/env python

import rospy
from rosmc_interface_msgs.srv import TriggerMissionExecutor, TriggerMissionExecutorRequest, TriggerMissionExecutorResponse


def execute(agent_name):
    rospy.init_node(agent_name)

    service_name = 'trigger_mission_executor'
    print "wait for service: " + str(service_name)
    rospy.wait_for_service(service_name)

    try:
        trigger_execution = rospy.ServiceProxy(service_name, TriggerMissionExecutor)
        # uint8 RUN = 0
        # uint8 PAUSE = 1
        # uint8 STOP = 2
        # uint8 RESET = 3
        resp1 = trigger_execution(0, "turtle1")
        print resp1
    except rospy.ServiceException, e:
        print "Service call failed: %s" %e


if __name__ == "__main__":
    execute('mission_executor_caller')
