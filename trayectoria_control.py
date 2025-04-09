import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
import time

class TrayectoriaControl(Node):

    def __init__(self):
        super().__init__('trayectoria_control')
        self.cmd_vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)

    def generar_trayectoria(self, tipo: int):
        msg = Twist()

        if tipo == 0:
            self.detener(msg)  # Detener el robot cuando el tipo es 0
        elif tipo == 2:
            self.linea(msg)
        elif tipo == 3:
            self.triangulo(msg)
        elif tipo == 4:
            self.cuadrado(msg)
        elif tipo == 5:
            self.pentagono(msg)
        elif tipo == 6:
            self.hexagono(msg)
        elif tipo == 7:
            self.heptagono(msg)
        elif tipo == 8:
            self.octagono(msg)
        elif tipo == 9:
            self.nonagono(msg)
        else:
            self.get_logger().warn(f"Tipo {tipo} no reconocido, el número debe estar entre 0 y 9.")

    def mover(self, linear_x, angular_z, duration_sec):
        msg = Twist()

        # Asegurándonos que los valores sean siempre del tipo float
        msg.linear.x = float(linear_x)
        msg.angular.z = float(angular_z)

        self.cmd_vel_pub.publish(msg)
        self.get_logger().info(f"Movimiento: linear.x = {linear_x}, angular.z = {angular_z}")
        time.sleep(duration_sec)

    def linea(self, msg: Twist):
        self.get_logger().info("Trayectoria: Línea")
        self.mover(0.2, 0.0, 5)  # Avanzar en línea recta durante 5 segundos

    def triangulo(self, msg: Twist):
        self.get_logger().info("Trayectoria: Triángulo")
        for _ in range(3):
            self.mover(0.2, 0.0, 5)  # Avanzar
            self.mover(0.0, float(3.14/3), 2)  # Girar 120 grados
        self.mover(0.0, 0.0, 0)

    def cuadrado(self, msg: Twist):
        self.get_logger().info("Trayectoria: Cuadrado")
        for _ in range(4):
            self.mover(0.2, 0.0, 5)  # Avanzar
            self.mover(0.0, float(3.14/2), 2)  # Girar 90 grados
        self.mover(0.0, 0.0, 0)

    def pentagono(self, msg: Twist):
        self.get_logger().info("Trayectoria: Pentágono")
        for _ in range(5):
            self.mover(0.2, 0.0, 5)  # Avanzar
            self.mover(0.0, float(2*math.pi/5), 2)  # Girar 72 grados

    def hexagono(self, msg: Twist):
        self.get_logger().info("Trayectoria: Hexágono")
        for _ in range(6):
            self.mover(0.2, 0.0, 5)  # Avanzar
            self.mover(0.0, float(2*math.pi/6), 2)  # Girar 60 grados

    def heptagono(self, msg: Twist):
        self.get_logger().info("Trayectoria: Heptágono")
        for _ in range(7):
            self.mover(0.2, 0.0, 5)  # Avanzar
            self.mover(0.0, float(2*math.pi/7), 2)  # Girar 51.43 grados

    def octagono(self, msg: Twist):
        self.get_logger().info("Trayectoria: Octágono")
        for _ in range(8):
            self.mover(0.2, 0.0, 5)  # Avanzar
            self.mover(0.0, float(2*math.pi/8), 2)  # Girar 45 grados

    def nonagono(self, msg: Twist):
        self.get_logger().info("Trayectoria: Nonágono")
        for _ in range(9):
            self.mover(0.2, 0.0, 5)  # Avanzar
            self.mover(0.0, float(2*math.pi/9), 2)  # Girar 40 grados

    def detener(self, msg: Twist):
        """ Detener el robot por completo """
        msg.linear.x = 0.0
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 0.0

        self.cmd_vel_pub.publish(msg)
        self.get_logger().info("Robot detenido.")

def main(args=None):
    rclpy.init(args=args)
    node = TrayectoriaControl()
    try:
        while rclpy.ok():
            tipo = int(input("Ingresa el número de lados de la trayectoria (0-9): "))
            node.generar_trayectoria(tipo)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
