#! /usr/bin/env python3
import rosbag
import sys
#import csi_utils.constants as constants
#import csi_utils.transform_utils as transform_utils
#import csi_utils.pipeline_utils as pipeline_utils

from os.path import join
import os
import tqdm
import numpy as np
import argparse

#from ..dcgr.dcgr_debug.scripts import Original, Modified

# Create the parser
parser = argparse.ArgumentParser(description='Process CSI data from a ROS bag file.')

# Add arguments
parser.add_argument('--bag_file', type=str, required=True, help='Path to the input ROS bag file')

# Parse the arguments
args = parser.parse_args()

#create .npz file for python
export_npz = True
#create .mat file for matlab
export_mat = True


#path to a bag file
print("Loading bag...")
bag = rosbag.Bag(args.bag_file)

#dir to output processed data
out = "~/data/"

channels = {}
times = {}
aoas = {}
rssis = {}
profs = {}
aoa_sensors = {}
rx = None

topics = list(bag.get_type_and_topic_info()[1].keys())
print(f"Topics in the bag file: {topics}")

tof = np.empty((64, 4, 0))

# rssi_vals = []

for topic, msg, t in bag.read_messages():
    
    if topic == '/sensor/data':
        tof = np.append(tof, np.array(msg.data).reshape(64,4, 1), axis=2)


print(f"/sensor/data {tof.shape}")

np.save(args.bag_file[:-4], tof)

# def feedbackFilter(x, a0, b1):
#     y = np.zeros_like(x)
#     y[0] = a0 * x[0]
#     for i in range(1, len(x)):
#         y[i] = a0 * x[i] + b1 * y[i-1]
#     return y

# y = feedbackFilter(tof[60,3,:], 0.25, 0.25)





# from matplotlib import pyplot as plt
# import ipywidgets as widgets

# @widgets.interact(b1=widgets.FloatSlider(min=-1.0, max=1.0, step=0.01, value=0.8))
# def execute(b1=0.8):
#     impulseResponse = feedbackFilter(tof[60,3,:], 1.0, b1)
    
#     fig, axes = plt.subplots(1, 2, figsize=(16,6))
#     ax = axes[0]
#     ax.plot(np.arange(tof.shape[2]), tof[60,3,:], label="Channel 0")
#     ax.plot(np.arange(tof.shape[2]), y, label="Channel 1")
#     # ax.plot(impulse, 'bo-')
#     # ax.set_xlabel('Sample count')
#     # ax.set_ylabel('Amplitude')
#     # ax.set_ylim(-0.1, 1.1)
#     # ax.set_xlim(-0.5, 10)
#     # ax.set_title("Impulse")
#     # ax.grid(which='both', axis='both')
    
#     # ax = axes[1]
#     # ax.plot(impulseResponse, 'ro-')
#     # ax.set_xlabel('Sample count')
#     # ax.set_ylim(-1.1, 1.1)
#     # ax.set_xlim(-0.5, 50)
#     # ax.set_title("Impulse Response")
#     # ax.grid(which='both', axis='both')

#     plt.show



# # # plt.connect("key_press_event", on_key)

# # plt.plot(np.arange(tof.shape[2]), tof[60,3,:], label="Channel 0")
# # plt.plot(np.arange(tof.shape[2]), y, label="Channel 1")
# # plt.plot(np.arange(tof.shape[2]), tof[0,1,:], label="Channel 1")
# # plt.plot(np.arange(tof.shape[2]), tof[0,2,:], label="Channel 2")
# # plt.plot(np.arange(tof.shape[2]), tof[0,3,:], label="Channel 3")
# # plt.axis('equal')
# # plt.show()