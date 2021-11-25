#!/usr/bin/env python3
import argparse

import rospy
from std_msgs.msg import String
from psr_parte08_ex3.msg import Dog

def main():
    # ---------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------
    parser = argparse.ArgumentParser(description='PSR argparse example.')
    parser.add_argument('--message', type=str,
                        default='Do not know what to say ',
                        help='phttps://github.com/miguelriemoliveira/psr_21-22/tree/main/Parte08#exerc%C3%ADcio-5---servidores-e-clientes-em-rosrint stuff to the screen or not.')
    parser.add_argument('--rate', type=float,default=1)
    args = vars(parser.parse_args())

    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('chatter', Dog, queue_size=10)
    # pub2 = rospy.Publisher('A17', String, queue_size=10)
    rate = rospy.Rate(args['rate'])  # 10hz

    # ---------------------------------------------------
    # Execution
    # ---------------------------------------------------
    while not rospy.is_shutdown():
        # text_to_send = args['message'] + str(rospy.get_time())
        # rospy.loginfo(text_to_send)

        # create a dog message to sent
        dog = Dog()
        dog.name = 'max'
        dog.age = 18
        dog.color = 'black'
        dog.brothers.append('lily')
        dog.brothers.append('boby')

        pub.publish(dog)

        # pub2.publish('Aqui vai um para sul')
        rate.sleep()

    # ---------------------------------------------------
    # Termination
    # ---------------------------------------------------


if __name__ == '__main__':
    main()
