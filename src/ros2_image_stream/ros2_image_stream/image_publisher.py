import rclpy
from rclpy.node import Node
import cv2
import base64
from std_msgs.msg import String  # Change to String message type
from cv_bridge import CvBridge

class ImagePublisher(Node):
    def __init__(self):
        super().__init__('image_publisher')
        self.publisher_ = self.create_publisher(String, 'image_frame', 10)  # Change to String message type
        self.timer = self.create_timer(0.1, self.publish_frame)  # 10 FPS
        self.cap = cv2.VideoCapture(0)  # Open webcam
        self.bridge = CvBridge()

    def publish_frame(self):
        ret, frame = self.cap.read()
        if ret:
            _, buffer = cv2.imencode('.jpg', frame)
            jpg_as_text = base64.b64encode(buffer).decode('utf-8')
            ros_image = String(data=jpg_as_text)
            self.publisher_.publish(ros_image)

    def destroy_node(self):
        self.cap.release()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = ImagePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
