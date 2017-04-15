#!/usr/bin/env python3

"""
Created on 15 Apr 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from scs_host.sys.host import Host


# --------------------------------------------------------------------------------------------------------------------

serial_number = Host.serial_number()

print("serial_number:[%s]" % serial_number)
