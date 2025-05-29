#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import sys
import math
from tf.transformations import euler_from_quaternion

# Publicador para enviar comandos de velocidad al robot
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
vel_msg = Twist()
# Diccionario para almacenar la posición y orientación actual del robot
current_pose = {'x': 0.0, 'y': 0.0, 'yaw': 0.0}

# Callback para actualizar la posición y orientación del robot usando la odometría
def odom_callback(msg):
    global current_pose
    current_pose['x'] = msg.pose.pose.position.x
    current_pose['y'] = msg.pose.pose.position.y

    # Convertir la orientación de cuaternión a ángulos de Euler
    orientation_q = msg.pose.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (_, _, yaw) = euler_from_quaternion(orientation_list)
    current_pose['yaw'] = yaw

# Función para calcular la velocidad con aceleración sinusoidal
def velocidad(t, vel_max, dist_max):
    return abs(vel_max * math.sin(math.pi * t / (dist_max * 8)))

# Detener el robot
def detener():
    vel_msg.linear.x = 0.0
    vel_msg.linear.y = 0.0
    vel_msg.linear.z = 0.0

    vel_msg.angular.x = 0.0
    vel_msg.angular.y = 0.0
    vel_msg.angular.z = 0.0

    pub.publish(vel_msg)

# Mover el robot en línea recta una distancia x
def mover_x(x, vel_max, usar_aceleracion):
    vel_msg.linear.y = 0.0
    vel_msg.angular.z = 0.0

    t0 = rospy.get_time()
    t_prev = rospy.get_time()
    t_now = rospy.get_time()
    distancia = 0
    vel = vel_max
    while (distancia < x):
        t_now = rospy.get_time()
        if (usar_aceleracion):
            vel = velocidad((t_now - t0), vel_max, x)
            distancia += (t_now - t_prev) * vel
        else:
            distancia = (t_now - t0) * vel
        
        vel_msg.linear.x = vel
        pub.publish(vel_msg)

        t_prev = t_now
    
    detener()
    rospy.sleep(2)

# Rotar el robot un ángulo específico
def rotar(ang, vel):
    rospy.sleep(2)
    vel_msg.linear.x = 0.0
    vel_msg.angular.z = vel

    t0 = rospy.get_time()
    angulo = 0
    pub.publish(vel_msg)
    
    while (abs(angulo - math.radians(ang)) > 0.005):
        t1 = rospy.get_time()
        angulo = (t1 - t0) * vel
        
    detener()
    rospy.sleep(2)

# Mover el robot en línea recta usando odometría
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

        if distancia_recorrida >= x:
            break

        if usar_aceleracion:
            t_total = t_now - t0
            vel = velocidad(t_total, vel_max, x)

        vel_msg.linear.x = vel
        vel_msg.angular.z = 0.0
        pub.publish(vel_msg)

        rate.sleep()

    detener()
    rospy.sleep(2)

# Rotar el robot un ángulo específico usando odometría
def rotar_odometria(ang_deg, vel):
    ang_rad = math.radians(ang_deg)
    start_yaw = current_pose['yaw']
    target_yaw = start_yaw + ang_rad

    # Normalizar el ángulo objetivo entre -pi y pi
    target_yaw = math.atan2(math.sin(target_yaw), math.cos(target_yaw))

    vel_msg.linear.x = 0.0
    vel_msg.angular.z = vel if ang_rad > 0 else -abs(vel)

    rate = rospy.Rate(100)  # Frecuencia de 100 Hz
    while not rospy.is_shutdown():
        current_yaw = current_pose['yaw']
        diff = math.atan2(math.sin(target_yaw - current_yaw), math.cos(target_yaw - current_yaw))
        if abs(diff) < 0.03:  # Tolerancia para detener la rotación
            break
        pub.publish(vel_msg)
        rate.sleep()

    detener()
    rospy.sleep(2)

# Función principal para mover el robot en diferentes trayectorias
def mover_robot(n, iteraciones):
    rospy.init_node('nodo_movimiento')
    rospy.Subscriber('/odom', Odometry, odom_callback)

    # Línea recta
    if (n == 0):
        for i in range(iteraciones):
            rospy.sleep(2)
            mover_x_odometria(2, 0.2, False)

    # Triángulo equilátero
    if (n == 1):
        for i in range(iteraciones):
            rospy.sleep(2)
            mover_x_odometria(3, 0.2, True)
            rotar_odometria(120, 0.2)
            mover_x_odometria(3, 0.2, True)
            rotar_odometria(120, 0.2)
            mover_x_odometria(3, 0.2, True)
            rotar_odometria(120, 0.2)

    # Cuadrado
    if (n == 2):
        for i in range(iteraciones):
            rospy.sleep(2)
            mover_x_odometria(1, 0.2, True)
            rotar_odometria(90, 0.2)
            mover_x_odometria(1, 0.2, True)
            rotar_odometria(90, 0.2)
            mover_x_odometria(1, 0.2, True)
            rotar_odometria(90, 0.2)
            mover_x_odometria(1, 0.2, True)
            rotar_odometria(90, 0.2)
    
    # Infinito
    if (n == 3):
        for i in range(iteraciones):
            rospy.sleep(2)
            mover_x_odometria(0.5, 0.2, True)
            rotar_odometria(120, 0.2)
            mover_x_odometria(1, 0.2, True)
            rotar_odometria(-120, -0.2)
            mover_x_odometria(0.5, 0.2, True)
            rotar_odometria(-120, -0.2)
            mover_x_odometria(1, 0.2, True)
            rotar_odometria(120, 0.2)

if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            print("Uso: rosrun p3_pkg movimiento.py <comando>")
            sys.exit(1)

        n = int(sys.argv[1])  # Tipo de trayectoria
        iteraciones = int(sys.argv[2])  # Número de iteraciones
        mover_robot(n, iteraciones)

    except rospy.ROSInterruptException:
        pass