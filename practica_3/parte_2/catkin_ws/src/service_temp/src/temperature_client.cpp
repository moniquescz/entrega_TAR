#include "rclcpp/rclcpp.hpp"
#include "service_temp/srv/convert_temp.hpp"
#include <chrono>
#include <cstdlib>
#include <memory>

using namespace std::chrono_literals;

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);

  if (argc != 3) {
    RCLCPP_ERROR(rclcpp::get_logger("rclcpp"), "Uso: cliente <temperatura> <tipo_conversion>");
    return 1;
  }

  auto node = rclcpp::Node::make_shared("temperature_client");
  auto client = node->create_client<service_temp::srv::ConvertTemp>("convert_temperature");

  while (!client->wait_for_service(1s)) {
    RCLCPP_INFO(node->get_logger(), "Esperando al servicio...");
  }

  auto request = std::make_shared<service_temp::srv::ConvertTemp::Request>();
  request->input_temp = std::stod(argv[1]);
  request->conversion_type = argv[2];

  auto result = client->async_send_request(request);

  if (rclcpp::spin_until_future_complete(node, result) ==
      rclcpp::FutureReturnCode::SUCCESS)
  {
    RCLCPP_INFO(node->get_logger(), "Resultado: %.2f", result.get()->converted_temp);
  } else {
    RCLCPP_ERROR(node->get_logger(), "Fallo al llamar al servicio");
  }

  rclcpp::shutdown();
  return 0;
}
