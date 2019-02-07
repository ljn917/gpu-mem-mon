#!/usr/bin/env python3

# need package: py3nvml
# if you use python 2, you need nvidia-ml-py and change the import

from __future__ import print_function

# import pynvml
import py3nvml.py3nvml as pynvml
import datetime


pynvml.nvmlInit()
print("Driver Version:", pynvml.nvmlSystemGetDriverVersion())

deviceCount = pynvml.nvmlDeviceGetCount()

for i in range(deviceCount):
    handle = pynvml.nvmlDeviceGetHandleByIndex(i)
    print("Device {}: {}".format(i, pynvml.nvmlDeviceGetName(handle)))

pynvml.nvmlShutdown()
