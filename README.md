# GPS_spoofing_UAV

This packet contains code to perform a GPS spoofing attack. 
Make sure you have ROS 1, MAVROS, PX4 Autopilot, Gazebo Classic and QGroundControl installed on an Ubunutu 20.04 machine.

Change the GPS coordinates in the file spoofing.py located in /src/offboard_py/scripts/spoofing.py to decide where to spoof the UAV.
Open QGroundControl
Launch the start_offb.py located /src/offboard_py/src/launch to make the UAV start by running "roslaunch offboard_py start_offb.launch"
Then launch the spoofing.py located in the same folder, when you want to interfere with the direction of the UAV by running "roslaunch offboard_py spoofing.launch" in another terminal.
