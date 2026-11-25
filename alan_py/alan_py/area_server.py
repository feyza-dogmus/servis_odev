import rclpy
from rclpy.node import Node
from alan_interfaces.srv import RectangleArea


class AlanSunucu(Node):
    def __init__(self):
        super().__init__('rectangle_area_server')
        self.srv = self.create_service(
            RectangleArea, 'rectangle_area', self.istek_isle)
        self.get_logger().info('Rectangle area service ready.')

    def istek_isle(self, request, response):
        if request.width < 0 or request.height < 0:
            response.area = 0.0
            response.success = False
            self.get_logger().warn(
                f'Negatif deger reddedildi: {request.width}, {request.height}')
        else:
            response.area = request.width * request.height
            response.success = True
            self.get_logger().info(
                f'{request.width} x {request.height} = {response.area}')
        return response


def main(args=None):
    rclpy.init(args=args)
    node = AlanSunucu()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
