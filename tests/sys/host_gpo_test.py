#!/usr/bin/env python3

"""
Created on 22 Dec 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import time

from scs_host.sys.host_gpo import HostGPO


# --------------------------------------------------------------------------------------------------------------------

try:
    gpo = HostGPO("P9_12", HostGPO.LOW)        # P8_10
    print(gpo)

    time.sleep(1)

    gpo.state = HostGPO.HIGH
    print(gpo)

    time.sleep(1)

    gpo.state = HostGPO.LOW
    print(gpo)

    time.sleep(1)

finally:
    HostGPO.cleanup()
