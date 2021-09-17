#!/usr/bin/env python

# --------------------------------------------------
# Miguel Riem Oliveira.
# PARI, September 2020.
# Adapted from http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
# -------------------------------------------------
import argparse
from colorama import Fore

import rospy
from std_msgs.msg import String
from pari_aula8_ex4_A.msg import Dog_A


def messageReceivedCallback(message):
    rospy.loginfo('Received message: "' + Fore.RED + str(message) + Fore.RESET + '"')


def main():
    parser = argparse.ArgumentParser(description='test')
    parser.add_argument('-tn', '--topic_name', type=str, default='chatter', help='Name of topic to publish.')
    args = vars(parser.parse_args())

    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber(args['topic_name'], Dog_A, messageReceivedCallback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    main()
