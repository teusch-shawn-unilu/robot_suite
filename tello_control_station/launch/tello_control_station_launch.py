import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python import get_package_share_directory
from launch.actions import OpaqueFunction
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    pkg_dir = get_package_share_directory("remote_controller")
    default_param_file = os.path.join(pkg_dir, "config", "params.yaml")
    params_file_arg = DeclareLaunchArgument(
        "params_file", default_value=str(default_param_file)
    )
    
    params_file = LaunchConfiguration("params_file")

    unitree_driver_function = Node(
        package="tello_hand_tracker",
        executable="hand_tracker_node",
        parameters=[params_file],
        output="screen",
    )

    return LaunchDescription([params_file_arg, unitree_driver_function])
