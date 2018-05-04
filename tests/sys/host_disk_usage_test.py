#!/usr/bin/env python3

"""
Created on 29 Apr 2018

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from scs_host.sys.host import Host


# --------------------------------------------------------------------------------------------------------------------

home_dir = Host.home_dir()
print("home_dir: %s" % home_dir)

du = Host.disk_usage(home_dir)
print("du: %s" % du)

