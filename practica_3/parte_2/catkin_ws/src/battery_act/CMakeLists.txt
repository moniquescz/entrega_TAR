cmake_minimum_required(VERSION 3.8)
project(battery_act)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(action_msgs REQUIRED)

## Generar la interfaz de acción
rosidl_generate_interfaces(${PROJECT_NAME}
  "action/Battery.action"
  DEPENDENCIES builtin_interfaces action_msgs
)

## Instalar scripts Python
install(
  PROGRAMS
    battery_act/battery_charger.py
    battery_act/battery_client.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_export_dependencies(rosidl_default_runtime)
ament_package()
