#!/usr/bin/env python3

import sys
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException

from battery_act.action import Battery  # Ajusta si tu action tiene otro nombre


class BatteryClient(Node):

    def __init__(self):
        super().__init__('battery_client')
        self._action_client = ActionClient(self, Battery, 'battery_monitor')
        self._goal_handle = None
        self._shutdown_requested = False

    def cancel_done(self, future):
        cancel_response = future.result()
        if len(cancel_response.goals_canceling) > 0:
            self.get_logger().info('Goal successfully canceled')
        else:
            self.get_logger().info('Goal failed to cancel')

        rclpy.shutdown()

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Objetivo rechazado.')
            return

        self.get_logger().info('Objetivo aceptado')
        self._goal_handle = goal_handle
        get_result_future = goal_handle.get_result_async()
        get_result_future.add_done_callback(self.get_result_callback)

    def feedback_callback(self, feedback_msg):
        porcentaje_actual = feedback_msg.feedback.current_percentage
        self.get_logger().info(f'Feedback: batería actual {porcentaje_actual}%')


    def send_goal(self, porcentaje_objetivo):
        self.get_logger().info('Esperando al servidor de acción...')
        self._action_client.wait_for_server()

        goal_msg = Battery.Goal()
        goal_msg.target_percentage = porcentaje_objetivo

        self.get_logger().info(f'Enviando objetivo: {porcentaje_objetivo}%')
        self._send_goal_future = self._action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def cancel_goal(self):
        self.get_logger().info('Solicitando cancelación del objetivo...')
        future = self._goal_handle.cancel_goal_async()
        future.add_done_callback(self.cancel_done)


    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f'Resultado recibido: {result.warning}')
        self._shutdown_requested = True


def main(args=None):
    if len(sys.argv) < 2:
        print(f"Uso: {sys.argv[0]} <porcentaje_objetivo>")
        sys.exit(1)

    porcentaje = int(sys.argv[1])
    if porcentaje < 0 or porcentaje > 100:
        print("El porcentaje debe estar entre 0 y 100")
        sys.exit(1)

    rclpy.init(args=args)
    client = BatteryClient()
    client.send_goal(porcentaje)

    try:
        while rclpy.ok() and not client._shutdown_requested:
            rclpy.spin_once(client, timeout_sec=0.1)
    except KeyboardInterrupt:
        client.get_logger().info('Ctrl+C pulsado: solicitando cancelación del objetivo...')
        client.cancel_goal()
    except ExternalShutdownException:
        pass
    finally:
        if rclpy.ok():  # Evita llamar shutdown dos veces
            client.destroy_node()
            rclpy.shutdown()


if __name__ == '__main__':
    main()
