#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry
import matplotlib.pyplot as plt
import signal
import sys

# Listas para almacenar las posiciones x e y del robot
x_positions = []
y_positions = []

# Callback que se ejecuta cuando se recibe un mensaje en el tópico /odom
def odom_callback(msg):
    # Extraer las posiciones x e y del mensaje de odometría
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    
    # Registrar las posiciones en el log de ROS
    rospy.loginfo(f"Logged robot Position: x={x:.2f}, y={y:.2f}")
    
    # Agregar las posiciones a las listas
    x_positions.append(x)
    y_positions.append(y)

# Manejador de señal para capturar la interrupción (Ctrl+C)
def signal_handler(sig, frame):
    # Ignorar señales adicionales mientras se procesa la actual
    signal.signal(sig, signal.SIG_IGN)

    # Graficar las posiciones almacenadas
    plt.plot(x_positions, y_positions, 'o')
    plt.xlabel('x')  # Etiqueta del eje x
    plt.ylabel('y')  # Etiqueta del eje y
    plt.grid()       # Mostrar la cuadrícula
    plt.axis('equal') # Escala igual en ambos ejes
    plt.show()       # Mostrar la gráfica

    # Salir del programa
    sys.exit(0)

if __name__ == '__main__':
    # Configurar el manejador de señal para SIGINT (Ctrl+C)
    signal.signal(signal.SIGINT, signal_handler)
    
    # Inicializar el nodo de ROS
    rospy.init_node("odometry_listener")
    
    # Suscribirse al tópico /odom para recibir mensajes de odometría
    rospy.Subscriber("/odom", Odometry, odom_callback)
    
    # Mantener el nodo en ejecución
    rospy.spin()