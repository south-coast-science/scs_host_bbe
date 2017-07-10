#!/usr/bin/env python3

"""
Created on 28 Jun 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import sys

from scs_core.data.localized_datetime import LocalizedDatetime

from scs_core.sampler.sampler import Sampler

from scs_host.sync.schedule_runner import ScheduleRunner


# --------------------------------------------------------------------------------------------------------------------

class TestSampler(Sampler):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, sem_name):
        """
        Constructor
        """
        Sampler.__init__(self, sem_name)


    # ----------------------------------------------------------------------------------------------------------------

    def sample(self):
        return 'SAMPLE ' + LocalizedDatetime.now().as_iso8601()


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "TestSampler:{runner:%s}" % self.runner


# --------------------------------------------------------------------------------------------------------------------
# run...

runner = ScheduleRunner('scs-gases', True)

sampler = TestSampler(runner)
print(sampler, file=sys.stderr)

sys.stderr.flush()

try:
    for sample in sampler.samples():
        print(sample, file=sys.stderr)
        sys.stderr.flush()

except KeyboardInterrupt:
    pass
