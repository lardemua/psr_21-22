#!/usr/bin/env python

# --------------------------------------------------
# Miguel Riem Oliveira.
# PARI, September 2020.
# Adapted from http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
# -------------------------------------------------
import argparse
from colorama import Fore
from functools import partial

import rospy
from std_msgs.msg import String
from pari_aula8_ex4.msg import Dog
from pari_aula8_ex5.srv import SetDogName, SetDogNameResponse


def setDogNameCallback(request, dog):
    rospy.loginfo('Received setDogName request with name ' + request.new_name)
    dog.name = request.new_name
    response = SetDogNameResponse()
    response.result = True
    return response


def main():

    topic_name = 'chatter'
    pub = rospy.Publisher(topic_name, Dog, queue_size=10)
    rospy.init_node('publisher', anonymous=False)

    # randomize a dog instance
    dog = Dog()
    dog.name = 'Bobi'
    dog.age = 3
    dog.color = 'white'
    dog.brothers.append('Lassie')
    dog.brothers.append('Romeo')

    srv = rospy.Service('~set_dog_name', SetDogName, partial(setDogNameCallback, dog=dog))



    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        # Fetch value of parameter to define color in which to print message
        color = rospy.get_param('~highlight_text_color')

        rospy.loginfo('Publishing message:"\n' + getattr(Fore, color) + str(dog) + Fore.RESET
                      + '\n" on topic ' + rospy.remap_name(topic_name))
        pub.publish(dog)
        rate.sleep()

    # Call nome with names remapping like this:
    # rosrun pari_aula9_ex1 publisher.py chatter:=my_chat __name:=my_node ~set_dog_name:=set_my_dog_name

if __name__ == '__main__':
    main()
