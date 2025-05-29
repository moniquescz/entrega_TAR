rosparam set /use_sim_time true
rosparam set /slam_gmapping/particles 30
rosparam set /slam_gmapping/linearUpdate 1.0
rosparam set /slam_gmapping/angularUpdate 0.5
rosparam set /slam_gmapping/minimumScore 0
rosparam set /slam_gmapping/resampleThreshold 0.5
rosparam set /slam_gmapping/delta 0.05
rosparam set /slam_gmapping/maxUrange 3.5

cd catkin_ws/
source devel/setup.bash
export TURTLEBOT3_MODEL=waffle
roslaunch turtlebot3_slam turtlebot3_slam.launch
