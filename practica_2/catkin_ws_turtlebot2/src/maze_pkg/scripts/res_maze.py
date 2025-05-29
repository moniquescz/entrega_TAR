#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import math
import numpy as np

#Métodos de movimiento y giro basados en tiempo
def girar(pub, angulo):
    vel = Twist()
    vel.angular.z = math.radians(angulo) / 2
    tiempo = abs(math.radians(angulo) / vel.angular.z)
    t0 = rospy.Time.now().to_sec()
    while (rospy.Time.now().to_sec() - t0) < tiempo and not rospy.is_shutdown():
        pub.publish(vel)
    pub.publish(Twist())

def girar_y_avanzar(pub, angular, velocidad=0.1):
    vel = Twist()
    vel.linear.x = velocidad
    vel.angular.z = angular
    pub.publish(vel)

#Método que dado un rango obtiene el menor valor de esa región
def get_region_mean(ranges, center_index, width=20):
    start = max(0, center_index - width // 2)
    end = min(len(ranges), center_index + width // 2)
    region = [r for r in ranges[start:end] if not math.isinf(r) and not math.isnan(r)]
    if not region:
        return float('inf')
    return np.min(region)

class SeguidorParedIzquierda:
    def __init__(self):
        rospy.init_node('seguidor_pared_izquierda')
        self.pub = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=10)
        self.sub = rospy.Subscriber('/scan', LaserScan, self.scan_callback, queue_size=1, buff_size=2**16)
        self.last_scan = None
        self.detecto_pared = False

    #Método callback para actualizar los valores leídos del lidar
    def scan_callback(self, msg):
        self.last_scan = msg

    def avanzar(self, velocidad=0.2):
        vel = Twist()
        vel.linear.x = velocidad
        self.pub.publish(vel)

    def detener(self):
        self.pub.publish(Twist())

    #Método para obtener menor valor del lidar
    def procesar_lidar(self):
        if self.last_scan is None:
            return None, None

        ranges = self.last_scan.ranges
        num_ranges = len(ranges)

        front_index = num_ranges // 2
        left_index = 639

        frente = get_region_mean(ranges, front_index, width=40)
        izquierda = get_region_mean(ranges, left_index, width=2)

        rospy.loginfo(f"[FR] {frente:.2f} | [IZQ] {izquierda:.2f}")
        return frente, izquierda

    #Método principal de resolución
    def run(self):
        rate = rospy.Rate(9)
        while not rospy.is_shutdown():
            frente, izquierda = self.procesar_lidar()
            if frente is None:
                rate.sleep()
                continue

            distancia_pared = 0.65

            # Inicio, moverse recto hasta encontrar la pared
            if not self.detecto_pared:
                if frente < distancia_pared:
                    self.detener()
                    rospy.loginfo("Pared detectada al frente. Giro inicial a la izquierda.")
                    girar(self.pub, -90)
                    self.detecto_pared = True
                else:
                    self.avanzar()
                rate.sleep()
                continue
            # Si detectamos una pared al frente, se realiza un giro total a la derecha, para seguirla
            elif frente < distancia_pared:
                self.detener()
                rospy.loginfo("Pared de frente. Giro a la derecha.")
                girar(self.pub, -90)

            # Si la distancia a la izquierda es muy elevada es porque hay que realizar un giro de 180 grados en movimiento
            elif izquierda > 1.5:
                girar_y_avanzar(self.pub,0.3,0.3)

            # Condiciones para mantener al robot en un umbral de distancia entre 0.75 y 1.0 respecto a la pared que sigue
            elif izquierda > 1.0:
                girar_y_avanzar(self.pub,0.1,0.2)
            
            elif izquierda < 0.75:
                girar_y_avanzar(self.pub,-0.1,0.2)

            # En cualquier otro caso giramos
            else:
                self.avanzar()

            rate.sleep()
            # Reseteamos las velocidades
            girar_y_avanzar(self.pub,0,0)

if __name__ == '__main__':
    try:
        robot = SeguidorParedIzquierda()
        robot.run()
    except rospy.ROSInterruptException:
        pass
