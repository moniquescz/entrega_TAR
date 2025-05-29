#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import time
import sys
import math

#Método principal de creación de figuras
def mover_robot(tipo_movimiento):
    rospy.init_node('movimiento', anonymous=True)
    pub = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=10)
    vel = Twist()

    time.sleep(2)
    #Dibujar una línea
    if tipo_movimiento == 0:
        rospy.loginfo("Avanzando 2 metros")
        vel.linear.x = 0.2  # m/s
        distancia = 2  # metros
        tiempo = distancia / vel.linear.x
        t0 = rospy.Time.now().to_sec()
        while (rospy.Time.now().to_sec() - t0) < tiempo:
            pub.publish(vel)
        vel.linear.x = 0
        pub.publish(vel)

    #Dibujar triángulo
    elif tipo_movimiento == 1:
        rospy.loginfo("Dibujando un triángulo equilátero")
        for _ in range(3):
            mover(pub, 0.2, 3)  # Lado del triángulo
            girar(pub, 120)  # Ángulo de 120º

    #Dibujar cuadrado
    elif tipo_movimiento == 2:
        rospy.loginfo("Dibujando un cuadrado")
        for _ in range(4):
            mover(pub, 0.2, 1)  # Lado del cuadrado
            girar(pub, 90)  # Ángulo de 90º

    #Dibujar infinito
    elif tipo_movimiento == 3:
        rospy.loginfo("Dibujando un infinito")
        mover(pub, 0.2, 0.5)
        girar(pub, 120)
        mover(pub, 0.2, 1.0)
        girar(pub, -120)
        mover(pub, 0.2, 0.5)
        girar(pub, -120)
        mover(pub, 0.2, 1.0)
        girar(pub, 120)
    #Aparcar el vehículo
    elif tipo_movimiento == 4:
        rospy.loginfo("Aparcando...")
        mover(pub, 0.2, 1.5)
        girar(pub, -90)
        mover(pub, 0.2, 1.5)
        girar(pub, -180)


    else:
        rospy.logwarn("Movimiento no válido. Usa 0, 1, 2, 3 o 4.")

#Método para mover el robot una distancia usando tiempos
def mover(pub, velocidad, distancia):
    vel = Twist()
    vel.linear.x = velocidad
    tiempo = distancia / velocidad
    t0 = rospy.Time.now().to_sec()
    while (rospy.Time.now().to_sec() - t0) < tiempo:
        pub.publish(vel)
    vel.linear.x = 0
    pub.publish(vel)

#Método para girar el robot unos ángulos usando tiempo
def girar(pub, angulo):
    vel = Twist()
    vel.angular.z = math.radians(angulo) / 2  # Ajustar velocidad de giro
    tiempo = abs(math.radians(angulo) / vel.angular.z)
    t0 = rospy.Time.now().to_sec()
    while (rospy.Time.now().to_sec() - t0) < tiempo:
        pub.publish(vel)
    vel.angular.z = 0
    pub.publish(vel)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        tipo_movimiento = int(sys.argv[1])
        mover_robot(tipo_movimiento)
    else:
        rospy.logwarn("Uso: rosrun p3_pkg movimiento.py <tipo_movimiento>")
