#!/usr/bin/env python3

"""
Created on 17 Mar 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import os

from scs_host.lock.lock import Lock


# --------------------------------------------------------------------------------------------------------------------

resource = "test"

print("resource: %s" % resource)
print("pid: %s" % os.getpid())

# --------------------------------------------------------------------------------------------------------------------

print("attempt 1...")
Lock.acquire(resource, 2)
print("OK")
print("-")


print("attempt 2...")
Lock.acquire(resource, 2)
print("OK")
print("-")
