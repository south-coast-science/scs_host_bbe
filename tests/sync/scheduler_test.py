#!/usr/bin/env python3

"""
Created on 28 Jun 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

https://pymotw.com/2/multiprocessing/basics.html
"""

from collections import OrderedDict

from scs_core.sync.schedule import Schedule
from scs_core.sync.schedule import ScheduleItem

from scs_host.sync.scheduler import Scheduler


# --------------------------------------------------------------------------------------------------------------------

item1 = ScheduleItem('scs-gases', 10, 1)
print(item1)

item2 = ScheduleItem('scs-particulates', 10, 2)
print(item2)

item3 = ScheduleItem('scs-climate', 20, 1)
print(item3)

items = OrderedDict([(item1.name, item1), (item2.name, item2), (item3.name, item3)])
print(items)
print("-")

schedule = Schedule(items)
print(schedule)
print("-")


# --------------------------------------------------------------------------------------------------------------------

heartbeat = Scheduler(schedule)
print(heartbeat)
print("-")

try:
    heartbeat.run()

except KeyboardInterrupt:
    pass
