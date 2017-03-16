#!/usr/bin/env python
import rospy
import cv2
import numpy as np
from vis.camera_manager import camera_manager



def shutdownActions():
    cv2.destroyAllWindows()

def main():
    #pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('vis', anonymous=True)
    rate = rospy.Rate(10) # 10hz



    rospy.logerr("&&&&&&&&&&&&&&&&&&&&&&&&&&")
    datafolder_path = "/home/vijay/Source/visionNav/data/"
    image_file = "hovercat.jpg"
    image = cv2.imread(datafolder_path + image_file, cv2.IMREAD_COLOR)
    #rospy.logerr(image.size)

    cv2.namedWindow("draw", cv2.CV_WINDOW_AUTOSIZE)


    camera = camera_manager()

    while not rospy.is_shutdown():

        hello_str = "hello wod %s" % rospy.get_time()
        rospy.logerr(hello_str)
        #pub.publish(hello_str)

        #cv2.imshow("draw", camimage)
        cv2.waitKey(1)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass