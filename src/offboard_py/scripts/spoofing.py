#! /usr/bin/python3

import rospy
from geographic_msgs.msg import GeoPoseStamped
from mavros_msgs.msg import State
from mavros_msgs.srv import CommandBool, CommandBoolRequest, SetMode, SetModeRequest

current_state = State()

def state_cb(msg):
    global current_state
    current_state = msg


if __name__ == "__main__":
    rospy.init_node("offb_node_py")

    state_sub = rospy.Subscriber("/uav3/mavros/state", State, callback = state_cb)
    global_pos_pub_uav3 = rospy.Publisher("/uav3/mavros/setpoint_position/global", GeoPoseStamped, queue_size=10 )
    rospy.wait_for_service("/uav3/mavros/cmd/arming")
    arming_client = rospy.ServiceProxy("/uav3mavros/cmd/arming", CommandBool)    

    rospy.wait_for_service("/uav3/mavros/set_mode")
    set_mode_client = rospy.ServiceProxy("/uav3/mavros/set_mode", SetMode)
    

    # Setpoint publishing MUST be faster than 2Hz
    rate = rospy.Rate(20)

    # Wait for Flight Controller connection
    while(not rospy.is_shutdown() and not current_state.connected):
        rate.sleep()

    geopose = GeoPoseStamped()
    
    geopose.pose.position.latitude = 63.413808006354735
    geopose.pose.position.longitude = 10.4111722559795
    geopose.pose.position.altitude = 40.0

    # Send a few setpoints before starting
    for i in range(100):   
        if(rospy.is_shutdown()):
            break

        global_pos_pub_uav3.publish(geopose)
        rate.sleep()

    offb_set_mode = SetModeRequest()
    offb_set_mode.custom_mode = 'OFFBOARD'

    arm_cmd = CommandBoolRequest()
    arm_cmd.value = True

    last_req = rospy.Time.now()

    while(not rospy.is_shutdown()):
        if(current_state.mode != "OFFBOARD" and (rospy.Time.now() - last_req) > rospy.Duration(5.0)):
            if(set_mode_client.call(offb_set_mode).mode_sent == True):
                rospy.loginfo("OFFBOARD enabled")
            
            last_req = rospy.Time.now()
        else:
            if(not current_state.armed and (rospy.Time.now() - last_req) > rospy.Duration(5.0)):
                if(arming_client.call(arm_cmd).success == True):
                    rospy.loginfo("Vehicle armed")
            
                last_req = rospy.Time.now()

        global_pos_pub_uav3.publish(geopose)
        rate.sleep()