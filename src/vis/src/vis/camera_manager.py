#!/usr/bin/python
import rospy

import cv2

class camera_manager:
    #camera_port = 0

    def __init__(self):
        pass
        camera_port = 0

        self.camera = cv2.VideoCapture(camera_port)

    def get_image(self):
        retval, im = self.camera.read()
        return im


