#include "rclcpp/rclcpp.hpp"
#include "service_temp/srv/convert_temp.hpp"
#include <memory>

using std::placeholders::_1;
using std::placeholders::_2;

class TemperatureServer : public rclcpp::Node
{
public:
  TemperatureServer() : Node("temperature_server")
  {
    service_ = this->create_service<service_temp::srv::ConvertTemp>(
      "convert_temperature",
      std::bind(&TemperatureServer::convert_temperature, this, _1, _2));
  }

private:
  void convert_temperature(
    const std::shared_ptr<service_temp::srv::ConvertTemp::Request> request,
    std::shared_ptr<service_temp::srv::ConvertTemp::Response> response)
  {
    if (request->conversion_type == "Cel_to_Far") {
      response->converted_temp = (request->input_temp * 9.0 / 5.0) + 32.0;
    } else if (request->conversion_type == "Far_to_Cel") {
      response->converted_temp = (request->input_temp - 32.0) * 5.0 / 9.0;
    } else {
      RCLCPP_WARN(this->get_logger(), "Tipo de conversión no válido");
      response->converted_temp = request->input_temp;
    }

    RCLCPP_INFO(this->get_logger(), "Solicitud: %.2f %s -> %.2f",
                request->input_temp,
                request->conversion_type.c_str(),
                response->converted_temp);
  }

  rclcpp::Service<service_temp::srv::ConvertTemp>::SharedPtr service_;
};

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<TemperatureServer>());
  rclcpp::shutdown();
  return 0;
}
