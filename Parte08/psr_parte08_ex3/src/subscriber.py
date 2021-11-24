#!/usr/bin/env python3
import argparse

import rospy
from std_msgs.msg import String


def callbackMsgReceived(msg):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", msg.data)


def main():
    # ---------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------
    parser = argparse.ArgumentParser(description='PSR argparse example.')
    parser.add_argument('--topic', type=str, default='chatter')
    args = vars(parser.parse_args())

    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber(args['topic'], String, callbackMsgReceived)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    main()