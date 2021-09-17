#!/usr/bin/env python

# --------------------------------------------------
# Miguel Riem Oliveira.
# PARI, September 2020.
# Adapted from http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
# -------------------------------------------------
import argparse
from colorama import Fore
import rospy
from pari_aula8_ex4.msg import Dog

highlight_text_color = 'RED'


def messageReceivedCallback(message):
    global highlight_text_color
    highlight_text_color = rospy.get_param("~highlight_text_color")
    rospy.loginfo('Received message: "\n' + getattr(Fore, highlight_text_color) + str(message) + Fore.RESET + '\n"')


def paramsChangedCallback(config, level):
    # Create a callback function for the dynamic reconfigure server.
    # Fill in local variables with values received from dynamic reconfigure clients (typically the GUI).
    global highlight_text_color
    highlight_text_color = config['highlight_text_color']
    return config


def main():
    parser = argparse.ArgumentParser(description='test')
    parser.add_argument('-tn', '--topic_name', type=str, default='chatter', help='Name of topic to publish.')
    args = vars(parser.parse_args())

    rospy.init_node('subscriber', anonymous=False)

    global highlight_text_color
    # less advanced version
    highlight_text_color = rospy.get_param("~highlight_text_color")
    # more advanced version
    # Give ourselves the ability to run a dynamic reconfigure server.
    # from dynamic_reconfigure.server import Server as DynamicReconfigureServer
    # server = DynamicReconfigureServer(ConfigType, paramsChangedCallback)

    rospy.Subscriber(args['topic_name'], Dog, messageReceivedCallback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    main()
