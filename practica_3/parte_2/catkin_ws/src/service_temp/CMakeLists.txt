cmake_minimum_required(VERSION 3.8)
project(service_temp)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Buscar dependencias necesarias
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# Generar el servicio personalizado
rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/ConvertTemp.srv"
)

# Ejecutables
add_executable(temperature_server src/temperature_server.cpp)
ament_target_dependencies(temperature_server rclcpp)
# Vínculo con las interfaces generadas
rosidl_target_interfaces(temperature_server ${PROJECT_NAME} "rosidl_typesupport_cpp")

add_executable(temperature_client src/temperature_client.cpp)
ament_target_dependencies(temperature_client rclcpp)
rosidl_target_interfaces(temperature_client ${PROJECT_NAME} "rosidl_typesupport_cpp")

# Instalación
install(TARGETS
  temperature_server
  temperature_client
  DESTINATION lib/${PROJECT_NAME}
)

ament_export_dependencies(rosidl_default_runtime)
ament_package()
