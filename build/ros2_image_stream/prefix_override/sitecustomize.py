import sys
if sys.prefix == '/Users/hares/miniconda3/envs/ros_env':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/Users/hares/Desktop/infor2025/robot/rospose/install/ros2_image_stream'
