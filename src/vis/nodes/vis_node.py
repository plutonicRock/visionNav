#!/usr/bin/env python
import rospy
import cv2



def main():
    #pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('vis', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    m = cv2.cvtColor((200,200))

    while not rospy.is_shutdown():
        cv2.namedWindow("stuff")
        hello_str = "hello wod %s" % rospy.get_time()
        rospy.logerr(hello_str)
        #pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass