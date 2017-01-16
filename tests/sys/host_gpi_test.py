#!/usr/bin/env python3

"""
Created on 22 Dec 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from scs_host.sys.host_gpi import HostGPI

import Adafruit_BBIO.GPIO as GPIO


# --------------------------------------------------------------------------------------------------------------------

try:
    gpio = HostGPI("P8_10")
    print(gpio)

    gpio.wait(GPIO.RISING)
    print(gpio)

    print('\a')

finally:
    GPIO.cleanup()
