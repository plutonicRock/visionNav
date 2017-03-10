import rospy

def main():
    pass
    rospy.init_node('vis_node', anonymous=False)

    # Rate in Hz
    rate = rospy.Rate(20)
    print "hello wod"
    rate.sleep()