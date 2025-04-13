#! /usr/bin/env python3
import rospy
# Brings in the SimpleActionClient
import actionlib
# Brings in the messages used by the fibonacci action, including the
# goal message and the result message.
import mi_accion.msg
from std_msgs.msg import String
def fibonacci_client(order):
    # Creates the SimpleActionClient, passing the type of the action
    # (FibonacciAction) to the constructor.
    client = actionlib.SimpleActionClient('fibonacci', mi_accion.msg.ejFibonacciAction)
    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()
    # Creates a goal to send to the action server.
    goal = mi_accion.msg.FibonacciGoal(orden=order)
    # Sends the goal to the action server.
    client.send_goal(goal)
    estado_pub = rospy.Publisher('/estado_accion', String, queue_size=10)
    rate = rospy.Rate(1)
    
    while client.get_state() in [actionlib.GoalStatus.PENDING, actionlib.GoalStatus.ACTIVE]:
        estado_pub.publish('en proceso')
        rate.sleep()
        
    # Waits for the server to finish performing the action.
    client.wait_for_result()
    # Prints out the result of executing the action
    return client.get_result() # A FibonacciResult

if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('fibonacci_client_py')
        order = rospy.get_param('orden',20)
        result = fibonacci_client(order)
        print("Result:", ', '.join([str(n) for n in result.secuencia_final]))
    except rospy.ROSInterruptException:
        pass