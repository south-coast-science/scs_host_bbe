#!/usr/bin/env python3

"""
Created on 26 Dec 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from scs_host.sys.host_serial import HostSerial


# --------------------------------------------------------------------------------------------------------------------

serial = HostSerial(4, 115200, True)
print(serial)

try:
    serial.open(1.0, 1.0)
    print(serial)

    serial.write_line("hello world!")
    serial.write_line("goodbye world!")

finally:
    serial.close()
    print(serial)
