import time
import rafcon
import rospy
from rosmc_interface_msgs.msg import AgentStatus, ActionStatus
from rosmc_interface_msgs.srv import TriggerMissionExecutor, TriggerMissionExecutorRequest, TriggerMissionExecutorResponse,\
    UpdateActionStatus, UpdateActionStatusRequest
from rafcon.utils import log


class AgentStatusObserver:

    def __init__(self, gvm):
        self.gvm = gvm

        self.agent_status = None

        self.is_in_wifi_range = True  # wifi_threshold < receiver.power
        self.is_in_wifi_range_with_margin = True  # wifi_threshold + wifi_threshold_margin < receiver.power
        self.wifi_threshold = -68.6
        self.wifi_threshold_margin = 4.4

        self.is_battery_remaining = True
        self.is_battery_remaining_with_margin = True
        self.battery_threshold = 0.2  # TODO: this should be configurable

        # the status will be name-spaced by ROS_NAMESPACE and is thus agent specific
        self.agent_status_subscriber = rospy.Subscriber('status',
                                                        AgentStatus,
                                                        callback=self.agent_status_callback)

    def agent_status_callback(self, agent_status):
        self.agent_status = agent_status
        self.is_in_wifi_range = self.wifi_threshold < self.agent_status.wlan_signal
        self.is_in_wifi_range_with_margin = self.wifi_threshold + self.wifi_threshold_margin < self.agent_status.wlan_signal
        self.is_battery_remaining = 0 < self.agent_status.battery
        self.is_battery_remaining_with_margin = self.battery_threshold < self.agent_status.battery

        # Set global variables
        #  NOTE: this sm does not start/pause execution!!
        self.gvm.set_variable("is_in_wifi_range", self.is_in_wifi_range)
        self.gvm.set_variable("is_in_wifi_range_with_margin", self.is_in_wifi_range_with_margin)
        self.gvm.set_variable("is_battery_remaining", self.is_battery_remaining)
        self.gvm.set_variable("is_battery_remaining_with_margin", self.is_battery_remaining_with_margin)


def execute(self, inputs, outputs, gvm):
    self.logger.debug("Observe agent status and store info as global variables ...")
    agent_status_observer = AgentStatusObserver(gvm)

    while True:
        # use preemptive wait instead of sleep; otherwise the state does it not responsive to the execution engine
        if self.wait_for_interruption(gvm.get_variable("global_timeout")):
            if self.preempted:
                agent_status_observer.agent_status_subscriber.unregister()
                return -2
            if self.paused:
                self.wait_for_unpause(0.2)
                if self.preempted:
                    agent_status_observer.agent_status_subscriber.unregister()
                    return -2
