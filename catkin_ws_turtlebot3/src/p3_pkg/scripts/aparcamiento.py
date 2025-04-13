#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import sys
import math
from tf.transformations import euler_from_quaternion

# Publicador para enviar comandos de velocidad
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
vel_msg = Twist()

# Diccionario para almacenar la posición y orientación actual del robot
current_pose = {'x': 0.0, 'y': 0.0, 'yaw': 0.0}

# Callback para actualizar la posición y orientación del robot a partir de la odometría
def odom_callback(msg):
    global current_pose
    current_pose['x'] = msg.pose.pose.position.x
    current_pose['y'] = msg.pose.pose.position.y

    # Convertir la orientación de cuaternión a ángulos de Euler
    orientation_q = msg.pose.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (_, _, yaw) = euler_from_quaternion(orientation_list)
    current_pose['yaw'] = yaw

# Función para calcular la velocidad en función del tiempo y la distancia
def velocidad(t, vel_max, dist_max):
    return abs(vel_max * math.sin(math.pi * t / (dist_max * 8)))

# Función para detener el robot
def detener():
    vel_msg.linear.x = 0.0
    vel_msg.linear.y = 0.0
    vel_msg.linear.z = 0.0

    vel_msg.angular.x = 0.0
    vel_msg.angular.y = 0.0
    vel_msg.angular.z = 0.0

    pub.publish(vel_msg)

# Función para mover el robot en línea recta usando la odometría
def mover_x_odometria(x, vel_max, usar_aceleracion):
    start_x = current_pose['x']
    start_y = current_pose['y']
    t0 = rospy.get_time()
    vel = vel_max

    rate = rospy.Rate(100)  # Frecuencia de 100 Hz
    while not rospy.is_shutdown():
        t_now = rospy.get_time()
        dx = current_pose['x'] - start_x
        dy = current_pose['y'] - start_y
        distancia_recorrida = math.sqrt(dx**2 + dy**2)

        # Verificar si se alcanzó la distancia deseada
        if distancia_recorrida >= x:
            break

        # Ajustar la velocidad si se usa aceleración
        if usar_aceleracion:
            t_total = t_now - t0
            vel = velocidad(t_total, vel_max, x)

        vel_msg.linear.x = vel
        vel_msg.angular.z = 0.0
        pub.publish(vel_msg)

        rate.sleep()

    detener()
    rospy.sleep(2)

# Función para rotar el robot usando la odometría
def rotar_odometria(ang_deg, vel):
    ang_rad = math.radians(ang_deg)
    start_yaw = current_pose['yaw']
    target_yaw = start_yaw + ang_rad

    # Normalizar el ángulo objetivo
    target_yaw = math.atan2(math.sin(target_yaw), math.cos(target_yaw))

    vel_msg.linear.x = 0.0
    vel_msg.angular.z = vel if ang_rad > 0 else -abs(vel)

    rate = rospy.Rate(150)  # Frecuencia de 150 Hz
    while not rospy.is_shutdown():
        current_yaw = current_pose['yaw']
        diff = math.atan2(math.sin(target_yaw - current_yaw), math.cos(target_yaw - current_yaw))
        # Verificar si se alcanzó el ángulo deseado
        if abs(diff) < 0.005:
            break
        pub.publish(vel_msg)
        rate.sleep()

    detener()
    rospy.sleep(2)

# Función principal para realizar la maniobra de aparcamiento
def aparcar():
    rospy.init_node('nodo_movimiento')  # Inicializar el nodo de ROS
    rospy.Subscriber('/odom', Odometry, odom_callback)  # Suscribirse al tópico de odometría

    rospy.sleep(2)  # Esperar para asegurar que se reciban datos de odometría
    mover_x_odometria(1.5, 0.2, True)  # Mover hacia adelante 1.5 metros
    rotar_odometria(-90, -0.2)  # Rotar -90 grados
    mover_x_odometria(1.5, 0.2, True)  # Mover hacia adelante 1.5 metros
    rotar_odometria(180, 0.3)  # Rotar 180 grados

# Punto de entrada del script
if __name__ == '__main__':
    aparcar()