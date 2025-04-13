#!/usr/bin/env python3

import rospy
from p2pkg.msg import Mensaje1

def callback(msg):
    rospy.loginfo(f"Recibido: Fecha: {msg.fecha}, Número: {msg.numero}, PositionX: {msg.posicion.position.x}, OrientationW: {msg.posicion.orientation.w}")

def subscriber():
    rospy.init_node('nodosub_ejercicio2', anonymous=True)
    rospy.Subscriber('/topic_ejercicio2', Mensaje1, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass
