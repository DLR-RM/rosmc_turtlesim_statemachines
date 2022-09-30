from __future__ import print_function
from builtins import str
import math
import rospy
from geometry_msgs.msg import Vector3
from geometry_msgs.msg import Twist

max_rotation = 0.75


def normalize_angle_to_positive_360(angle):
    return (angle + 2.0 * math.pi) % (2 * math.pi)


def normalize_angle_to_pos_neg_180(angle):
    result_angle = angle
    while result_angle > math.pi:
        result_angle -= 2 * math.pi
    while result_angle < - math.pi:
        result_angle += 2 * math.pi
    return result_angle


def sign(number):
    if number < 0:
        return -1
    else:
        return 1


def set_velocity(x, phi, turtle_name, logger):
    position_vector = Vector3(x, 0, 0)
    rotation_vector = Vector3(0, 0, phi)
    twist_msg = Twist(position_vector, rotation_vector)
    try:
        logger.info("rotate_to_direction: publish twist to turtle {}".format(turtle_name))
        turtle_vel_publisher = rospy.Publisher("/" + turtle_name + "/cmd_vel", Twist, queue_size=10, latch=True)
        turtle_vel_publisher.publish(twist_msg)
        rate = rospy.Rate(10)
        rate.sleep()
    except rospy.ROSInterruptException as e:
        logger.error("Failed to send a velocity command to turtle {}: {}".format(turtle_name, str(e)))


def execute(self, inputs, outputs, gvm):
    self.logger.info("rotate_to_direction: inputs: {}".format(str(inputs)))

    global_storage_id_of_turtle_pose = inputs["global_storage_id_of_turtle_pos"]
    turtle_name = inputs["turtle_name"]

    my_x = gvm.get_variable(global_storage_id_of_turtle_pose + "/" + "x")
    my_y = gvm.get_variable(global_storage_id_of_turtle_pose + "/" + "y")
    my_phi = gvm.get_variable(global_storage_id_of_turtle_pose + "/" + "phi")

    r = rospy.Rate(2)

    if (my_x or my_y or my_phi) is None:
        self.logger.info("rotate_to_direction: global variable is None, return from execute function")
        self.logger.info("rotate_to_direction: my_x")
        self.logger.info("rotate_to_direction: my_y")
        self.logger.info("rotate_to_direction: my_phi")
        r.sleep()
        return 1

    self.logger.info("my_x: %f" % my_x)
    self.logger.info("my_y: %f" % my_y)
    self.logger.info("my_phi: %f" % my_phi)

    ######################################################
    # calc the target orientation to drive
    ######################################################

    target_angle = inputs["target_angle"]
    self.logger.info("rotate_to_direction: target_angle: %f" % target_angle)
    target_angle = normalize_angle_to_pos_neg_180(target_angle)
    self.logger.info("rotate_to_direction: target_angle: %f" % target_angle)
    orientation_diff = normalize_angle_to_pos_neg_180(my_phi - target_angle)
    self.logger.info("rotate_to_direction: orientation_diff: %f" % orientation_diff)

    # negative sign as we want to countersteer
    target_orientation_sign = -sign(orientation_diff)
    # normalize absolute value to max_rotation
    tmp = math.fabs(orientation_diff) / max_rotation
    if tmp > 1.0:
        tmp = 1.0
    theta_move = tmp * max_rotation * target_orientation_sign

    if math.fabs(orientation_diff) < 0.05:
        theta_move = 0
    self.logger.info("rotate_to_direction: final theta_move: {}".format(str(theta_move)))

    set_velocity(0.0, theta_move, turtle_name, self.logger)
    if theta_move == 0:
        return 0

    r.sleep()
    return 1