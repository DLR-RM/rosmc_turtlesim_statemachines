import rospy
from turtlesim.srv import *
from turtlesim.msg import *

def execute(self, inputs, outputs, gvm):
    topics = rospy.get_published_topics(namespace='/')
    #print(topics)
    set_of_turtles = []
    for [key, message_type] in topics:
        #print key
        if 'turtle' in key and 'pose' in key:
            elements = key.split('/')
            set_of_turtles.append(elements[1])
    if inputs["turtle_self"] in set_of_turtles:
        set_of_turtles.remove(inputs["turtle_self"])
    outputs["set_of_turtles"] = set_of_turtles
    if len(set_of_turtles) > 0:
        outputs["first_turtle"] = set_of_turtles[0]
    if len(set_of_turtles) > 0:
        return "turtle_found"
    else:
        return "no_turtle_found"
