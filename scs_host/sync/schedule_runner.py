"""
Created on 28 Jun 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Warning: only one sampler per semaphore!

http://semanchuk.com/philip/posix_ipc/#semaphore
"""

import sys
import time

import posix_ipc

from scs_core.sync.runner import Runner


# --------------------------------------------------------------------------------------------------------------------

class ScheduleRunner(Runner):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, name, verbose=False):
        """
        Constructor
        """
        self.__name = name
        self.__verbose = verbose


    # ----------------------------------------------------------------------------------------------------------------

    def reset(self):
        sem = posix_ipc.Semaphore(self.name, flags=posix_ipc.O_CREAT)

        while sem.value > 0:
            sem.acquire()           # clear excessive semaphore counts


    def samples(self, sampler):
        sem = posix_ipc.Semaphore(self.name, flags=posix_ipc.O_CREAT)

        # reset...
        self.reset()

        while True:
            try:
                # start...
                sem.acquire()

                if self.verbose:
                    print('%s: start' % self.name, file=sys.stderr)
                    sys.stderr.flush()

                yield sampler.sample()

            finally:
                # done...
                sem.release()

                if self.verbose:
                    print('%s: done' % self.name, file=sys.stderr)
                    sys.stderr.flush()

                time.sleep(0.1)     # must be longer than the release period and shorter than the sampling interval


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def name(self):
        return self.__name


    @property
    def verbose(self):
        return self.__verbose


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "ScheduleRunner:{name:%s, verbose:%s}" % (self.name, self.verbose)
