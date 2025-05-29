#!/usr/bin/env python3

import rospy
from random import random
from p2pkg.msg import Mensaje1
from geometry_msgs.msg import Pose
import sys
from datetime import datetime

def publisher():
    rospy.init_node('nodopub_ejercicio2', anonymous=True)
    pub = rospy.Publisher('/topic_ejercicio2', Mensaje1, queue_size=10)
    rate = rospy.Rate(1)  # Publicar 1 vez por segundo

    if len(sys.argv) < 2:
        rospy.logerr("Debe proporcionar un número como argumento")
        return
    
    numero = int(sys.argv[1])  # Argumento de entrada

    while not rospy.is_shutdown():
        msg = Mensaje1()
        msg.numero = numero
        msg.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        msg.posicion.position.x = random()
        msg.posicion.position.y = random()
        msg.posicion.position.z = random()
        msg.posicion.orientation.x = random()
        msg.posicion.orientation.y = random()
        msg.posicion.orientation.z = random()
        msg.posicion.orientation.w = random()

        rospy.loginfo(f"Publicado: Fecha: {msg.fecha}, Número: {msg.numero}, PositionX: {msg.posicion.position.x}, OrientationW: {msg.posicion.orientation.w}")
        
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
