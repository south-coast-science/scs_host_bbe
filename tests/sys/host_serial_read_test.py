#!/usr/bin/env python3

"""
Created on 26 Dec 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from scs_host.sys.host_serial import HostSerial


# --------------------------------------------------------------------------------------------------------------------

serial = HostSerial(1, 9600, False)     # the PAM7 GPS receiver
print(serial)

try:
    serial.open(2.0)
    print(serial)

    while True:
        text = serial.read_line(HostSerial.EOL, 4.0)
        print("text:[%s]" % text)

except KeyboardInterrupt:
        print("host_serial_read_test: KeyboardInterrupt")

finally:
    serial.close()
    print(serial)
