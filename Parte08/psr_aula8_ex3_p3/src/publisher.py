#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


def main():
    # ------------------------------------------------
    # Initialization
    # ------------------------------------------------
    rospy.init_node('publisher', anonymous=True)
    pub = rospy.Publisher('politics', String, queue_size=10)
    rate = rospy.Rate(1)

    # ------------------------------------------------
    # Execution
    # ------------------------------------------------
    while not rospy.is_shutdown():
        text_to_send = "hello world " + str(rospy.get_time())
        rospy.loginfo(text_to_send)  # same as print ... for now
        pub.publish(text_to_send)  # finally, publish the message
        rate.sleep()

    # ------------------------------------------------
    # Termination
    # ------------------------------------------------


if __name__ == '__main__':
    main()
