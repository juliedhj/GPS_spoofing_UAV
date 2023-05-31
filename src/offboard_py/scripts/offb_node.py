#! /usr/bin/python3

import rospy
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State
from mavros_msgs.srv import CommandBool, CommandBoolRequest, SetMode, SetModeRequest

current_state = State()

def state_cb(msg):
    global current_state
    current_state = msg


if __name__ == "__main__":
    rospy.init_node("offb_node_py")

    #UAV0
    state_sub_0 = rospy.Subscriber("/uav0/mavros/state", State, callback = state_cb)
    local_pos_pub_0 = rospy.Publisher("/uav0/mavros/setpoint_position/local", PoseStamped, queue_size=10)
    rospy.wait_for_service("/uav0/mavros/cmd/arming")
    arming_client_0 = rospy.ServiceProxy("/uav0/mavros/cmd/arming", CommandBool)    
    rospy.wait_for_service("/uav0/mavros/set_mode")
    set_mode_client_0 = rospy.ServiceProxy("/uav0/mavros/set_mode", SetMode)

    #UAV1
    state_sub_1 = rospy.Subscriber("/uav1/mavros/state", State, callback = state_cb)
    local_pos_pub_1 = rospy.Publisher("/uav1/mavros/setpoint_position/local", PoseStamped, queue_size=10)
    rospy.wait_for_service("/uav1/mavros/cmd/arming")
    arming_client_1 = rospy.ServiceProxy("/uav1/mavros/cmd/arming", CommandBool)    
    rospy.wait_for_service("/uav1/mavros/set_mode")
    set_mode_client_1 = rospy.ServiceProxy("/uav1/mavros/set_mode", SetMode)

    #UAV2
    state_sub_2 = rospy.Subscriber("/uav2/mavros/state", State, callback = state_cb)
    local_pos_pub_2 = rospy.Publisher("/uav2/mavros/setpoint_position/local", PoseStamped, queue_size=10)
    rospy.wait_for_service("/uav2/mavros/cmd/arming")
    arming_client_2 = rospy.ServiceProxy("/uav2/mavros/cmd/arming", CommandBool)    
    rospy.wait_for_service("/uav2/mavros/set_mode")
    set_mode_client_2 = rospy.ServiceProxy("/uav2/mavros/set_mode", SetMode)

    #UAV3
    state_sub_3 = rospy.Subscriber("/uav3/mavros/state", State, callback = state_cb)
    local_pos_pub_3 = rospy.Publisher("/uav3/mavros/setpoint_position/local", PoseStamped, queue_size=10)
    rospy.wait_for_service("/uav3/mavros/cmd/arming")
    arming_client_3 = rospy.ServiceProxy("/uav3/mavros/cmd/arming", CommandBool)    
    rospy.wait_for_service("/uav3/mavros/set_mode")
    set_mode_client_3 = rospy.ServiceProxy("/uav3/mavros/set_mode", SetMode)
    

    # Setpoint publishing MUST be faster than 2Hz
    rate = rospy.Rate(20)

    # Wait for Flight Controller connection
    while(not rospy.is_shutdown() and not current_state.connected):
        rate.sleep()

    pose = PoseStamped()
    pose.pose.position.x = 100
    pose.pose.position.y = 500
    pose.pose.position.z = 40

    # Send a few setpoints before starting
    for i in range(100):   
        if(rospy.is_shutdown()):
            break

        local_pos_pub_0.publish(pose)
        local_pos_pub_1.publish(pose)
        local_pos_pub_2.publish(pose)
        local_pos_pub_3.publish(pose)
        rate.sleep()

    offb_set_mode = SetModeRequest()
    offb_set_mode.custom_mode = 'OFFBOARD'

    arm_cmd = CommandBoolRequest()
    arm_cmd.value = True

    last_req = rospy.Time.now()

    while(not rospy.is_shutdown()):
        if(current_state.mode != "OFFBOARD" and (rospy.Time.now() - last_req) > rospy.Duration(5.0)):
            if(set_mode_client_0.call(offb_set_mode).mode_sent == True):
                rospy.loginfo("OFFBOARD enabled vehicle 1")
            if(set_mode_client_1.call(offb_set_mode).mode_sent == True):
                rospy.loginfo("OFFBOARD enabled vehicle 2")
            if(set_mode_client_2.call(offb_set_mode).mode_sent == True):
                rospy.loginfo("OFFBOARD enabled vehicle 3")
            if(set_mode_client_3.call(offb_set_mode).mode_sent == True):
                rospy.loginfo("OFFBOARD enabled vehicle 4")
        
            last_req = rospy.Time.now()
        else:
            if(not current_state.armed and (rospy.Time.now() - last_req) > rospy.Duration(5.0)):
                if(arming_client_0.call(arm_cmd).success == True):
                    rospy.loginfo("Vehicle 1 armed")
                if(arming_client_1.call(arm_cmd).success == True):
                    rospy.loginfo("Vehicle 2 armed")
                if(arming_client_2.call(arm_cmd).success == True):
                    rospy.loginfo("Vehicle 3 armed")
                if(arming_client_3.call(arm_cmd).success == True):
                    rospy.loginfo("Vehicle 4 armed")
            
                last_req = rospy.Time.now()

        local_pos_pub_0.publish(pose)
        local_pos_pub_1.publish(pose)
        local_pos_pub_2.publish(pose)
        local_pos_pub_3.publish(pose)
        rate.sleep()






