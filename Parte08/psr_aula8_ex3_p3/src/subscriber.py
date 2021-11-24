#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


def callback(data):
    rospy.loginfo('Received ' + str(data.data))


def main():
    # ------------------------------------------------
    # Initialization
    # ------------------------------------------------
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber("politics", String, callback)

    # ------------------------------------------------
    # Execution
    # ------------------------------------------------
    rospy.spin()

    # ------------------------------------------------
    # Termination
    # ------------------------------------------------


if __name__ == '__main__':
    main()
