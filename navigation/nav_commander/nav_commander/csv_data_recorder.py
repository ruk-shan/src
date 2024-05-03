import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from nav_msgs.msg import Odometry
from geometry_msgs.msg import *
import time


import csv


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        # self.get_logger().info(msg.pose.pose)
        # print (f"position X > {msg.pose.pose.position.x}")
        # print (f"position Y > {msg.pose.pose.position.y}")
        # print (f"position Z > {msg.pose.pose.position.z}")
        # print (f"orientation X > {msg.pose.pose.orientation.x}")
        # print (f"orientation Y > {msg.pose.pose.orientation.y}")
        # print (f"orientation Z > {msg.pose.pose.orientation.z}")
        # print (f"orientation W > {msg.pose.pose.orientation.w}")
        # print (f"time sec > {msg.header.stamp.sec}")
        # print (f"time nanosec > {msg.header.stamp.nanosec}")
        csv_to_write = [str(time.time()),msg.header.stamp.sec,msg.header.stamp.nanosec,
                        msg.pose.pose.position.x,msg.pose.pose.position.y,msg.pose.pose.position.z,
                        msg.pose.pose.orientation.x,msg.pose.pose.orientation.y,msg.pose.pose.orientation.z,msg.pose.pose.orientation.w]
        print(csv_to_write)
        
        with open('/home/rmf/ROS/IsaacSim-ros_workspaces/humble_ws/src/navigation/nav_commander/nav_commander/data.csv', mode = 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(csv_to_write)
            print ("file updated")


def main(args=None):
    rclpy.init(args=args)

    #create csv
    with open('/home/rmf/ROS/IsaacSim-ros_workspaces/humble_ws/src/navigation/nav_commander/nav_commander/data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["time_real","time sec","time nanosec","position X", "position Y", "position Z", "orientation X","orientation Y","orientation Z","orientation W"]
        writer.writerow(field)
    print ("file created")
    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()