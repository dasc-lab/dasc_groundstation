import rclpy
from rclpy.node import Node
from PyQt5.QtWidgets import QApplication, QWidget


from dasc_msgs.msg import RobotInfo, GroundStationStatus, GroundStationCommand

class DASCGroundStation(Node):
    
    def __init__(self):
        super().__init__('dasc_groundstation')
        self.gs_status_pub_ = self.create_publisher(GroundStationStatus, 'dasc_gs/status', 10)
        self.gs_command_pub_ = self.create_publisher(GroundStationStatus, 'dasc_gs/command', 10)
        self.timer_ = self.create_timer(0.5, self.timer_callback)
        
    def timer_callback(self):
        msg = GroundStationStatus()
        msg.timestamp = self.get_clock().now().nanoseconds
        msg.localization_type = 0
        msg.stop_all = False
        msg.emergency_stop = False
        self.gs_status_pub_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    app = QApplication([])
    window = QWidget()
    window.show()
    dasc_gs = DASCGroundStation()
    rclpy.spin(dasc_gs)
    
    rclpy.shutdown()
    

if __name__ == '__main__':
    main()