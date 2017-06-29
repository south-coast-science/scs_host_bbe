"""
Created on 28 Jun 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Warning: only one sampler per semaphore

http://semanchuk.com/philip/posix_ipc/#semaphore
"""

import sys
import time

import posix_ipc

from abc import abstractmethod


# --------------------------------------------------------------------------------------------------------------------

class Sampler(object):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, name):
        """
        Constructor
        """
        self.__name = name


    # ----------------------------------------------------------------------------------------------------------------

    @abstractmethod
    def sample(self):
        pass


    def samples(self):
        sem = posix_ipc.Semaphore(self.name, flags=posix_ipc.O_CREAT)

        # reset...
        while sem.value > 0:
            sem.acquire()

        while True:
            try:
                # start...
                sem.acquire()
                print('%s: sampler 2: started' % self.name, file=sys.stderr)
                sys.stderr.flush()

                yield self.sample()

            finally:
                # done...
                sem.release()
                print('%s: sampler 3: done' % self.name, file=sys.stderr)
                print('-', file=sys.stderr)
                sys.stderr.flush()

                time.sleep(0.1)   # must be longer than the release period and shorter than the sampling interval


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def name(self):
        return self.__name


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "Sampler:{name:%s}" % self.name
