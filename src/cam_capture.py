#! /usr/bin/env python 

from __future__ import print_function

import base64

import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError

def main(args):
    rospy.init_node("cam_capture_node")
    cvbridge=CvBridge()
    rate=rospy.Rate(25)
    message_pub = rospy.Publisher("image_topic", Image, queue_size=20)
    cam=cv2.VideoCapture(2)
    
    while not rospy.is_shutdown():
        ret,frame=cam.read()

        print("aa")
        message_pub.publish(cvbridge.cv2_to_imgmsg(frame,"bgr8"))

        cv2.imshow("capture",frame)
        print(rate.sleep())
        if cv2.waitKey(50) & 0xFF == ord('q'):
           break


    cv2.destroyAllWindows()
    cam.release()



if __name__ == '__main__':
    main(sys.argv)
    