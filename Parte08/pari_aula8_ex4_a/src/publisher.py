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
from dog_lib import Dog
from pari_aula8_ex4_A.msg import Dog_A

def main():
    parser = argparse.ArgumentParser(description='test')
    parser.add_argument('-tn', '--topic_name', type=str, default='chatter', help='Name of topic to publish.')
    parser.add_argument('-m', '--message_content', type=str, default='Notthing to say',
                        help='content of message to publish.')
    parser.add_argument('-f', '--frequency', type=float, default=10,
                        help='content of message to publish.')
    args = vars(parser.parse_args())

    pub = rospy.Publisher(args['topic_name'], Dog_A, queue_size=10)
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(args['frequency'])  # 10hz

    # Create an instance of class Dog
    # dog = Dog(name='Bobi', age=7, color='Black')
    # dog.addBrother('Lassie')

    dog_msg = Dog_A()
    dog_msg.name = 'Bobi'
    dog_msg.age = 7
    dog_msg.color = 'Black'
    dog_msg.brothers.append('Lassie')

    while not rospy.is_shutdown():
        rospy.loginfo('Publishing message: "' + Fore.RED + str(dog_msg) + Fore.RESET
                      + '" on topic ' + args['topic_name'])
        pub.publish(dog_msg)
        rate.sleep()


if __name__ == '__main__':
    main()
