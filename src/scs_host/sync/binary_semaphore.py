"""
Created on 2 May 2018

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

A mutex binary semaphore abstraction over the posix_ipc.Semaphore.

https://en.wikipedia.org/wiki/Semaphore_(programming)
http://semanchuk.com/philip/posix_ipc/#semaphore
"""

import posix_ipc


# --------------------------------------------------------------------------------------------------------------------

class BinarySemaphore(object):
    """
    classdocs
    """

    __INITIAL_ACQUISITION_TIME = 1.0                    # seconds

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, name):
        """
        Constructor
        """
        self.__name = name
        self.__semaphore = posix_ipc.Semaphore(self.name, flags=posix_ipc.O_CREAT)

        try:
            self.__semaphore.acquire(self.__INITIAL_ACQUISITION_TIME)       # initial state is: acquired by creator
        except (posix_ipc.BusyError, posix_ipc.SignalError):
            pass


    # ----------------------------------------------------------------------------------------------------------------

    def acquire(self, timeout=None):                    # None timeout = wait forever (dangerous)
        self.__semaphore.acquire(timeout)

        while self.__semaphore.value > 0:
            self.__semaphore.acquire()                  # limit the value to 0 or 1


    def release(self):
        self.__semaphore.release()


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def name(self):
        return self.__name


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "BinarySemaphore:{name:%s}" % self.name
