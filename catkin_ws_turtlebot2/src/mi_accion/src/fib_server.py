#! /usr/bin/env python3
import rospy
import actionlib
import mi_accion.msg
class FibonacciAction(object):
    # create messages that are used to publish feedback/result
    _feedback = mi_accion.msg.FibonacciFeedback()
    _result = mi_accion.msg.FibonacciResult()
    def __init__(self, name):
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, mi_accion.msg.FibonacciAction, execute_cb=self.execute_cb, auto_start = False)
        self._as.start()
    def execute_cb(self, goal):
        # helper variables
        r = rospy.Rate(1)
        success = True
        # append the seeds for the fibonacci sequence
        self._feedback.secuencia_actual = []
        self._feedback.secuencia_actual.append(0)
        self._feedback.secuencia_actual.append(1)
        # publish info to the console for the user
        rospy.loginfo('%s: Ejecutando, creando una secuencia de fibonacci de orden %i con semilla%i, %i' % (self._action_name, goal.orden, self._feedback.secuencia_actual[0], self._feedback.secuencia_actual[1]))
        # start executing the action
        for i in range(1, goal.orden):
        # check that preempt has not been requested by the client
            if self._as.is_preempt_requested():
                rospy.loginfo('%s: Cancelado' % self._action_name)
                self._as.set_preempted()
                success = False
                break
            self._feedback.secuencia_actual.append(self._feedback.secuencia_actual[i] + self._feedback.secuencia_actual[i-1])
            # publish the feedback
            self._as.publish_feedback(self._feedback)
            # this step is not necessary, the sequence is computed at 1 Hz for demonstration purposes
            r.sleep()
        if success:
            self._result. secuencia_final= self._feedback.secuencia_actual
            rospy.loginfo('%s: Completado' % self._action_name)
            self._as.set_succeeded(self._result)
if __name__ == '__main__':
    rospy.init_node('fibonacci')
    server = FibonacciAction(rospy.get_name())
    rospy.loginfo('Accion Fibonacci lanzada y esperando un objetivo!')
    rospy.spin()