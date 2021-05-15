#! /usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError
import sys

cv_bridge=CvBridge()
def callback(image):

    global cv_bridge
    try:
        cv_image=cv_bridge.imgmsg_to_cv2(image,"bgr8")
    except CvBridgeError as error:
        print(error)
    
    cv2.imshow("camera capture",cv_image)

    if cv2.waitKey(1) & 0xFF== ord("q"):
        rospy.signal_shutdown("closing the rospy from cam_stream_node")
        



def main():
    rospy.init_node("cam_stream_node")
    rospy.Subscriber("/image_topic", Image, callback)

    try: 
        rospy.spin()
    except:
        cv2.destroyAllWindows()
    


if __name__ == '__main__':
    main()
    