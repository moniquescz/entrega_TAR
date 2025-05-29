#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry
import matplotlib
matplotlib.use('Agg')  # Usa un backend sin interfaz gráfica
import matplotlib.pyplot as plt

# Lista para almacenar posiciones
pos_x = []
pos_y = []

def odom_callback(msg):
    """Callback que guarda la posición del robot."""
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y

    pos_x.append(x)
    pos_y.append(y)

    rospy.loginfo(f"Robot Position: x={x:.2f}, y={y:.2f}")

def save_trajectory():
    """Guarda la trayectoria en un archivo PNG."""
    if not pos_x or not pos_y:
        rospy.logwarn("No hay datos de trayectoria para guardar.")
        return

    plt.figure()
    plt.plot(pos_x, pos_y, marker="o", linestyle="-", label="Trayectoria")
    plt.xlabel("Posición X (m)")
    plt.ylabel("Posición Y (m)")
    plt.title("Trayectoria del Robot")
    plt.legend()
    plt.grid()

    save_path = "/workspace/catkin_ws/src/p3_pkg/trayectoria.png"
    plt.savefig(save_path)
    rospy.loginfo(f"Trayectoria guardada en {save_path}")

def main():
    """Inicializa el nodo y se suscribe a /odom."""
    rospy.init_node("dibuja_mov", anonymous=True)
    rospy.Subscriber("/odom", Odometry, odom_callback)

    rospy.loginfo("Registrando posiciones... Espera unos segundos o presiona Ctrl+C para detener.")

    # Ejecuta el nodo y espera que el usuario lo detenga (Ctrl+C)
    rospy.spin()  # Mantiene el nodo activo y procesando mensajes

    # Una vez detenido el nodo, guarda la trayectoria
    save_trajectory()

if __name__ == "__main__":
    main()
