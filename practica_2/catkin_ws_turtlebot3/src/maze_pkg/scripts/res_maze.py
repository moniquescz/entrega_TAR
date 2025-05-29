#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
import math
from tf.transformations import euler_from_quaternion
import threading

# Publicador para enviar comandos de velocidad
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
vel_msg = Twist()
current_pose = {'x': 0.0, 'y': 0.0, 'yaw': 0.0}  # Posición actual del robot

# Índices de las lecturas del LiDAR para diferentes direcciones
front_index = 0
left_index = 89
right_index = 269
left_index_control_1 = 99
left_index_control_2 = 79

correction_threshold = 0.01  # Umbral para corrección de trayectoria

ranges = []  # Almacena las lecturas del LiDAR

# Función para detener el robot
def detener():
    vel_msg.linear.x = 0.0
    vel_msg.linear.y = 0.0
    vel_msg.linear.z = 0.0

    vel_msg.angular.x = 0.0
    vel_msg.angular.y = 0.0
    vel_msg.angular.z = 0.0

    pub.publish(vel_msg)

# Función para avanzar el robot a una velocidad específica
def avanzar(vel):
    vel_msg.linear.x = vel
    vel_msg.linear.y = 0.0
    vel_msg.linear.z = 0.0

    vel_msg.angular.x = 0.0
    vel_msg.angular.y = 0.0
    vel_msg.angular.z = 0.0

    pub.publish(vel_msg)

# Función para girar el robot un ángulo específico
def girar(ang_deg, vel):
    ang_rad = math.radians(ang_deg)  # Convertir ángulo a radianes
    start_yaw = current_pose['yaw']
    target_yaw = start_yaw + ang_rad

    vel_msg.linear.x = 0.0
    vel_msg.linear.y = 0.0
    vel_msg.linear.z = 0.0

    vel_msg.angular.x = 0.0
    vel_msg.angular.y = 0.0
    vel_msg.angular.z = vel if ang_rad > 0 else -abs(vel)

    pub.publish(vel_msg)

    # Ajustar el ángulo objetivo dentro del rango [-pi, pi]
    target_yaw = math.atan2(math.sin(target_yaw), math.cos(target_yaw))

    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
        current_yaw = current_pose['yaw']
        diff = math.atan2(math.sin(target_yaw - current_yaw), math.cos(target_yaw - current_yaw))
        if abs(diff) < 0.02:  # Detenerse cuando se alcanza el ángulo objetivo
            break
        rate.sleep()

# Funciones para giros específicos
def girar_90_derecha(vel):
    girar(-90, vel)

def girar_90_izquierda(vel):
    girar(90, vel)

def girar_5_derecha(vel):
    girar(-5, vel)

def girar_5_izquierda(vel):
    girar(5, vel)

# Callback para actualizar la posición actual del robot usando Odometry
def odom_callback(msg):
    global current_pose
    current_pose['x'] = msg.pose.pose.position.x
    current_pose['y'] = msg.pose.pose.position.y

    orientation_q = msg.pose.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (_, _, yaw) = euler_from_quaternion(orientation_list)
    current_pose['yaw'] = yaw

# Callback para actualizar las lecturas del LiDAR
def lidar_callback(data):
    global ranges
    ranges = data.ranges

# Función para seguir la pared derecha
def seguir_pared_derecha():
    global ranges
    
    zona_abierta_contador = 0  # Contador para detectar espacios abiertos
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        if len(ranges) < 330:  # Verificar si las lecturas del LiDAR son suficientes
            continue

        # Obtener distancias relevantes del LiDAR
        a = ranges[left_index_control_1]
        b = ranges[left_index_control_2]
        right_wall = ranges[right_index] < 1.5
        front_wall = ranges[front_index] < 0.5
        left_wall = ranges[left_index] < 1.5

        # Verificar si está en un espacio abierto
        if not front_wall and not right_wall and not left_wall:
            zona_abierta_contador += 1
        else:
            zona_abierta_contador = 0

        if zona_abierta_contador > 200:  # Si está en un espacio abierto por mucho tiempo
            rospy.loginfo("¡He llegado al final del laberinto! :D")
            detener()
            break

        # CASO 1: Solo pared al frente → giro 90º derecha y avanzar
        if front_wall and not right_wall:
            rospy.loginfo("Pared al frente → giro 90° a la derecha")
            girar_90_derecha(0.2)
            avanzar(0.2)
            continue

        # CASO 2: Pared frontal y derecha → girar 90º izquierda y avanzar
        if front_wall and right_wall:
            rospy.loginfo("Pared al frente y a la derecha → girar 90º a la izquierda")
            girar_90_izquierda(0.2)
            avanzar(0.2)
            continue

        # CASO 3: Solo pared a la derecha → avanzar
        # CASO 4: Ninguna pared → avanzar
        if (not front_wall and right_wall) or (not front_wall and not right_wall):
            if (not front_wall and right_wall):
                rospy.loginfo("Solo pared a la derecha → avanzar")
            else:
                rospy.loginfo("No pared al frente ni derecha → avanzar")
            
            if (math.isinf(a) or math.isinf(b)):  # Si las lecturas son infinitas
                avanzar(0.2)
                continue
            else:
                vel_msg.linear.x = 0.2
                vel_msg.angular.z = 0.0

                # Corregir trayectoria si no está alineado con la pared
                if (abs(a - b)) > correction_threshold:
                    rospy.logwarn("Recorrido no alineado a la pared, corrigiendo trayectoria")
                    if (a > b):
                        vel_msg.angular.z = -0.05
                    elif (a < b):
                        vel_msg.angular.z = 0.05

                pub.publish(vel_msg)

                rate.sleep()

# Nodo principal
if __name__ == '__main__':
    rospy.init_node('lidar_viewer', anonymous=True)
    rospy.Subscriber("/scan", LaserScan, lidar_callback)  # Suscriptor al LiDAR
    rospy.Subscriber('/odom', Odometry, odom_callback)  # Suscriptor a Odometry

    # Hilo para ejecutar la función de seguir la pared derecha
    thread = threading.Thread(target=seguir_pared_derecha)
    thread.daemon = True
    thread.start()

    rospy.spin()  # Mantener el nodo activo