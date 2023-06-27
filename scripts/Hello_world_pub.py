#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def hello_world_pub(): #define a function
    #initialize or create a node called hellow_world_pub
    rospy.init_node("hello_world_pub_node") 
    #create a publsiher node with topic_name,data_type,queue_size
    pub=rospy.Publisher("hello_world",String,queue_size=10)
    #time delay of 5 sec per msg send
    rate=rospy.Rate(5)

    i=0

    while not rospy.is_shutdown():#to keep looping sending the message so long ros is not shutdown
        #to publish the publisher node a string and a counter i
        #data send must match the data type declared when creating the pub node
        pub.publish("Hello world"+str(i))
        i+=1
        rate.sleep()


if __name__=='__main__':
    try:
        hello_world_pub()

    except rospy.ROSInterruptException:
        pass