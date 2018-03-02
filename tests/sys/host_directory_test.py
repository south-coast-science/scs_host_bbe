#!/usr/bin/env python3

"""
Created on 2 Mar 2018

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from scs_host.sys.host import Host


# --------------------------------------------------------------------------------------------------------------------

home_dir = Host.home_dir()
print("home_dir: %s" % home_dir)

print("-")

try:
    lock_dir = Host.lock_dir()
    print("lock_dir: %s" % lock_dir)
except NotImplementedError:
    print("lock_dir: None")

try:
    tmp_dir = Host.tmp_dir()
    print("tmp_dir: %s" % tmp_dir)
except NotImplementedError:
    print("tmp_dir: None")

try:
    command_dir = Host.command_dir()
    print("command_dir: %s" % command_dir)
except NotImplementedError:
    print("command_dir: None")

print("-")

scs_dir = Host.scs_dir()
print("scs dir: %s" % scs_dir)

conf_dir = Host.conf_dir()
print("conf dir: %s" % conf_dir)

aws_dir = Host.aws_dir()
print("aws dir: %s" % aws_dir)

osio_dir = Host.osio_dir()
print("osio dir: %s" % osio_dir)

print("-")
