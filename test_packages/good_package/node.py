import rospy
from std_msgs.msg import String

def main():
    rospy.init_node("test_node")
    pub = rospy.Publisher("chatter", String, queue_size=10)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        pub.publish("hello")
        rate.sleep()

if __name__ == "__main__":
    main()
