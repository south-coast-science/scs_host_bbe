"""
Created on 28 Jun 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Warning: only one sampler per semaphore

http://semanchuk.com/philip/posix_ipc/#semaphore
https://pymotw.com/2/multiprocessing/basics.html
"""

import multiprocessing
import sys
import time

import posix_ipc

# from scs_core.data.localized_datetime import LocalizedDatetime
from scs_core.sync.interval_timer import IntervalTimer


# --------------------------------------------------------------------------------------------------------------------

class Scheduler(object):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, schedule):
        """
        Constructor
        """
        self.__schedule = schedule


    # ----------------------------------------------------------------------------------------------------------------

    def run(self):
        jobs = []

        # prepare...
        for item in self.schedule.items:
            target = SchedulerItem(item)
            job = multiprocessing.Process(name=item.name, target=target.run)
            job.daemon = True

            jobs.append(job)

        # run...
        for job in jobs:
            job.start()

        # wait...
        if len(jobs) > 0:
            jobs[0].join()


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def schedule(self):
        return self.__schedule


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "Scheduler:{schedule:%s}" % self.schedule


# --------------------------------------------------------------------------------------------------------------------

class SchedulerItem(object):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, item):
        """
        Constructor
        """
        self.__item = item


    # ----------------------------------------------------------------------------------------------------------------

    def run(self):
        sem = posix_ipc.Semaphore(self.item.name, flags=posix_ipc.O_CREAT)
        timer = IntervalTimer(self.item.interval)

        while timer.true():
            # print('%s: %s' % (self.item.name, LocalizedDatetime.now().as_iso8601()), file=sys.stderr)
            # sys.stderr.flush()

            # enable...
            sem.release()

            time.sleep(0.01)        # release period: hand semaphore to sampler

            try:
                # disable...
                sem.acquire(self.item.interval)

            except posix_ipc.BusyError:
                # release...
                sem.release()
                print('ItemScheduler.run: %s: release' % self.item.name, file=sys.stderr)


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def item(self):
        return self.__item


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "SchedulerItem:{item:%s}" % self.item
