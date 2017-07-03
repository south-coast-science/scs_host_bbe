"""
Created on 28 Jun 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Warning: only one sampler per semaphore!

http://semanchuk.com/philip/posix_ipc/#semaphore
https://pymotw.com/2/multiprocessing/basics.html
"""

import multiprocessing
import sys
import time

import posix_ipc

from scs_core.data.localized_datetime import LocalizedDatetime
from scs_core.sync.interval_timer import IntervalTimer


# --------------------------------------------------------------------------------------------------------------------

class Scheduler(object):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, schedule, verbose=False):
        """
        Constructor
        """
        self.__schedule = schedule
        self.__verbose = verbose

        self.__jobs = []


    # ----------------------------------------------------------------------------------------------------------------

    def run(self):
        # prepare...
        for item in self.schedule.items:
            target = SchedulerItem(item, self.verbose)
            job = multiprocessing.Process(name=item.name, target=target.run)
            job.daemon = True

            self.__jobs.append(job)

        # run...
        for job in self.__jobs:
            job.start()

        # wait...
        if len(self.__jobs) > 0:
            self.__jobs[0].join()


    def terminate(self):
        for job in self.__jobs:
            job.terminate()


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def schedule(self):
        return self.__schedule


    @property
    def verbose(self):
        return self.__verbose


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "Scheduler:{schedule:%s, verbose:%s}" % (self.schedule, self.verbose)


# --------------------------------------------------------------------------------------------------------------------

class SchedulerItem(object):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, item, verbose=False):
        """
        Constructor
        """
        self.__item = item
        self.__verbose = verbose


    # ----------------------------------------------------------------------------------------------------------------

    def run(self):
        sem = posix_ipc.Semaphore(self.item.name, flags=posix_ipc.O_CREAT)
        timer = IntervalTimer(self.item.interval)

        while timer.true():
            if self.verbose:
                print('%s: run' % self.item.name, file=sys.stderr)
                sys.stderr.flush()

            # enable...
            sem.release()

            time.sleep(0.01)        # release period: hand semaphore to sampler

            try:
                # disable...
                sem.acquire(self.item.interval)

            except posix_ipc.BusyError:
                # release...
                sem.release()

                print('%s: release' % self.item.name, file=sys.stderr)
                sys.stderr.flush()


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def item(self):
        return self.__item


    @property
    def verbose(self):
        return self.__verbose


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "SchedulerItem:{item:%s, verbose:%s}" % (self.item, self.verbose)
