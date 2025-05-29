#!/usr/bin/env python3


import threading
import time

import rclpy
from rclpy.action import ActionServer, CancelResponse, GoalResponse
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import ExternalShutdownException
from rclpy.executors import MultiThreadedExecutor
from rclpy.node import Node
from battery_act.action import Battery


class BatteryChargerServer(Node):
    def __init__(self):
        super().__init__('battery_charger')
        self._goal_handle = None
        self._goal_lock = threading.Lock()
        self._action_server = ActionServer(
            self,
            Battery,
            'battery_monitor',
            execute_callback=self.execute_callback,
            goal_callback=self.goal_callback,
            handle_accepted_callback=self.handle_accepted_callback,
            cancel_callback=self.cancel_callback,
            callback_group=ReentrantCallbackGroup()
        )
        self._current_battery = 100

    def destroy(self):
        self.get_logger().info('Destruyendo el servidor de acción...')
        self._action_server.destroy()
        super().destroy_node()

    def handle_accepted_callback(self, goal_handle):
        with self._goal_lock:
            if self._goal_handle is not None and self._goal_handle.is_active:
                self.get_logger().info('Cancelando el objetivo anterior antes de aceptar uno nuevo.')
                self._goal_handle.abort()
            self._goal_handle = goal_handle
        self.get_logger().info('Nuevo objetivo aceptado.')
        goal_handle.execute()


    def cancel_callback(self, goal_handle):
        self.get_logger().info('Cancelación solicitada.')
        return CancelResponse.ACCEPT


    def execute_callback(self, goal_handle):
        self._current_battery = 100
        target = goal_handle.request.target_percentage
        self.get_logger().info(f'Comenzando descarga hacia {target}%')

        feedback_msg = Battery.Feedback()
        while self._current_battery > target:
            if not goal_handle.is_active:
                self.get_logger().info('Abortando ejecución, el objetivo ya no está activo.')
                return Battery.Result()

            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().info('Request de cancelación recibido, abortando ejecución.')
                return Battery.Result()

            time.sleep(1)
            self._current_battery -= 5
            feedback_msg.current_percentage = self._current_battery
            self.get_logger().info(f'Batería actual: {self._current_battery}%')
            goal_handle.publish_feedback(feedback_msg)


        result = Battery.Result()
        if self._current_battery <= 20:
            result.warning = '¡Advertencia! Batería críticamente baja.'
        else:
            result.warning = 'Se está agotando la batería. Conecte el cargador.'
        self.get_logger().info('Objetivo alcanzado.')
        with self._goal_lock:
            if not goal_handle.is_active:
                self.get_logger().info('Goal aborted')
                return Battery.Result()

            goal_handle.succeed()

        return result



    def goal_callback(self, goal_request):
        self.get_logger().info(f'Recibido objetivo: {goal_request.target_percentage}%')
        return GoalResponse.ACCEPT






def main(args=None):
    try:
        rclpy.init(args=args)
        action_server = BatteryChargerServer()

        # We use a MultiThreadedExecutor to handle incoming goal requests concurrently
        executor = MultiThreadedExecutor()
        executor.add_node(action_server)
        executor.spin()
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()
