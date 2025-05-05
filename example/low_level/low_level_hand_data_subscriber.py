"""
Subscribes to and prints low-level data from the B1 robot's dexterous hands using Python.

This script listens to the specific topic where the robot publishes detailed
hand sensor data, including finger angles, forces, currents, temperatures,
status, and error codes for each finger joint. It then prints this received data
to the standard output.
"""
from booster_robotics_sdk_python import ChannelFactory, B1HandDataSubscriber, HandReplyData
import time

def handler(hand_data_msg):
    print("Received hand message:")
    for i, data in enumerate(hand_data_msg.hand_data):
        print(f" seq:{data.seq} angle{data.angle}, force:{data.force}, current:{data.current}, status:{data.status}, temp:{data.temp}, error:{data.error}")
    print(f" hand index:{hand_data_msg.hand_index} hand type:{hand_data_msg.hand_type} ")
    print("done")


def main():
    ChannelFactory.Instance().Init(0)
    channel_subscriber = B1HandDataSubscriber(handler)
    channel_subscriber.InitChannel()
    print("init handler")
    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()
