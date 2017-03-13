#!/usr/bin/env python
import rospy
import cv2
import numpy as np


def shutdownActions():
    cv2.destroyAllWindows()

def main():
    #pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('vis', anonymous=True)
    rate = rospy.Rate(10) # 10hz



    #rospy.on_shutdown(shutdownActions)
    rospy.logerr("&&&&&&&&&&&&&&&&&&&&&&&&&&")
    #rospy.logerr(cv2.getBuildInformation())
    image_path = "~/hovercat.jpg"
    #cv2.LoadImage(image_path, iscolor=CV_LOAD_IMAGE_COLOR)
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    rospy.logerr(image.size)

    #size = 200, 200
    #m = np.zeros(size, dtype=np.uint8)
    cv2.namedWindow("draw", cv2.CV_WINDOW_AUTOSIZE)

    while not rospy.is_shutdown():

        hello_str = "hello wod %s" % rospy.get_time()
        rospy.logerr(hello_str)
        #pub.publish(hello_str)
        cv2.imshow("draw", image)
        cv2.waitKey(1)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass