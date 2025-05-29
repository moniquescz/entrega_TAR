cd catkin_ws/
source devel/setup.bash
rosbag play --clock --pause src/slam_pkg/bagfiles/slam_experimento_lento.bag -r 8.0
