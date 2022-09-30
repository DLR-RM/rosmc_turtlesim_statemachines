#!/usr/bin/env python

import rospy
import yaml
from rosmc_interface_msgs.srv import Mission, MissionRequest, MissionResponse
from rosmc_interface_msgs.msg import SyncIDs, AgentActions, Action, ActionContent, ActionStatus


# def execute(agent_name):
#     rospy.init_node(agent_name)
#     service_name = 'mission_advertiser1/mission'
#     print "wait for service: " + str(service_name)
#     rospy.wait_for_service(service_name)
#
#     try:
#         mission_request = rospy.ServiceProxy(service_name, Mission)
#
#         action_status1 = ActionStatus(1)
#         action_status2 = ActionStatus(2)
#         action_content1 = ActionContent("action_name1", True, False, True, action_status1, "(param1.1, param1.2)")
#         action_content2 = ActionContent("action_name1", True, False, True, action_status2, "(param2.1, param2.2)")
#         action1 = Action("action_id1", action_content1)
#         action2 = Action("action_id2", action_content2)
#         agent_action1 = AgentActions("agent1", [action1])
#         agent_action2 = AgentActions("agent2", [action1, action2])
#         agent_actions = [agent_action1, agent_action2]
#
#         string_list1 = ["string1", "string2"]
#         string_list2 = ["string3", "string4"]
#         sync_ids = [SyncIDs(string_list1), SyncIDs(string_list2)]
#
#         resp1 = mission_request(agent_actions, sync_ids)
#         print resp1
#     except rospy.ServiceException, e:
#         print "Service call failed: %s" %e


def execute(agent_name):
    rospy.init_node(agent_name)
    # service_name = '/turtle1/mission_update'
    service_name = 'send_mission'
    print "wait for service: " + str(service_name)
    rospy.wait_for_service(service_name)

    try:
        mission_request = rospy.ServiceProxy(service_name, Mission)

        action_status1 = ActionStatus(1, "")
        action_status2 = ActionStatus(2, "")
        params = {'turtle_name': {'data_type': 'str', 'value': 'turtle1'},
                #   'pose': {'data_type': 'list', 'value': [1.0, 8.0, 45.0]},
                  'x_pos': {'data_type': 'float', 'value': 1.0},
                  'y_pos': {'data_type': 'float', 'value': 8.0},
                  'yaw': {'data_type': 'float', 'value': 0.785}}
        params = yaml.dump(params)
        action_content0 = ActionContent("move_to_pose", "", False, True, False, action_status2, params)
        params = {'turtle_name': {'data_type': 'str', 'value': 'turtle1'},
                  'x_pos': {'data_type': 'float', 'value': 5.0},
                  'x_scale': {'data_type': 'float', 'value': 4.0},
                  'y_pos': {'data_type': 'float', 'value': 5.0},
                  'y_scale': {'data_type': 'float', 'value': 3.0}}
        params = yaml.dump(params)
        action_content1 = ActionContent("explore", "", True, False, False, action_status1, params)
        params = {'turtle_name': {'data_type': 'str', 'value': 'turtle1'},
                  'x_pos': {'data_type': 'float', 'value': 1.0},
                  'y_pos': {'data_type': 'float', 'value': 8.0}}
        params = yaml.dump(params)
        action_content2 = ActionContent("move_to_position", "", False, True, False, action_status2, params)
        params = {'turtle_name': {'data_type': 'str', 'value': 'turtle1'},
                  'x_pos': {'data_type': 'float', 'value': 4.0},
                  'y_pos': {'data_type': 'float', 'value': 2.0}}
        params = yaml.dump(params)
        action_content3 = ActionContent("move_to_position_backward", "", False, False, True, action_status1, params)
        params = {'turtle_name': {'data_type': 'str', 'value': 'turtle1'},
                  'x_pos': {'data_type': 'float', 'value': 7.0},
                  'y_pos': {'data_type': 'float', 'value': 3.0}}
        params = yaml.dump(params)
        action_content4 = ActionContent("take_measurements", "", True, True, False, action_status1, params)
        params = {'turtle_name': {'data_type': 'str', 'value': 'turtle1'},
                  'turtle_to_follow': {'data_type': 'str', 'value': 'turtle2'}}
        params = yaml.dump(params)
        action_content5 = ActionContent("follow_turtle", "", False, True, True, action_status2, params)
        params = {'list_pose': {'data_type': 'list', 'value': [
                {
                    "pitch": 0.0,
                    "roll": 0.0,
                    "x": 5.0,
                    "y": 7.0,
                    "yaw": 0.0,
                    "z": 0.0
                },
                {
                    "pitch": 0.0,
                    "roll": 0.0,
                    "x": 2.0,
                    "y": 7.0,
                    "yaw": 0.0,
                    "z": 0.0
                },
                {
                    "pitch": 0.0,
                    "roll": 0.0,
                    "x": 2.0,
                    "y": 3.0,
                    "yaw": 0.0,
                    "z": 0.0
                },
                {
                    "pitch": 0.0,
                    "roll": 0.0,
                    "x": 5.0,
                    "y": 3.0,
                    "yaw": 0.0,
                    "z": 0.0
                }
            ]}}
        params = yaml.dump(params)
        action_content6 = ActionContent("mapping", "", False, True, True, action_status2, params)
        action0 = Action("action_id0", action_content0)
        action1 = Action("action_id1", action_content1)
        action2 = Action("action_id2", action_content2)
        action3 = Action("action_id3", action_content3)
        action4 = Action("action_id4", action_content4)
        action5 = Action("action_id5", action_content5)
        action6 = Action("action_id6", action_content6)
        agent_action1 = AgentActions("agent1", [action1])
        # agent_action2 = AgentActions("turtle1", [action0, action1, action2, action3, action4, action5, action6])
        agent_action2 = AgentActions("turtle1", [action0, action4])
        # agent_action2 = AgentActions("turtle1", [Action("11", action_content0), Action("44", action_content4)])
        agent_actions = [agent_action1, agent_action2]

        string_list1 = ["string1", "string2"]
        string_list2 = ["string3", "string4"]
        sync_ids = [SyncIDs(string_list1), SyncIDs(string_list2)]

        resp1 = mission_request(agent_actions, sync_ids)
        print resp1
    except rospy.ServiceException, e:
        print "Service call failed: %s" %e


if __name__ == "__main__":
    execute('mission_caller')
