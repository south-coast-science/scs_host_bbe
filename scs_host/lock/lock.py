"""
Created on 10 Aug 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import os
import random
import sys
import threading
import time

from scs_host.lock.lock_timeout import LockTimeout


# --------------------------------------------------------------------------------------------------------------------

class Lock(object):
    """a general-purpose semaphore"""

    __ROOT =    "/run/lock/southcoastscience/"


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def init(cls):
        """
        Establish the /run/lock/southcoastscience/ root.
        Should be invoked on class load.
        """
        try:
            os.mkdir(cls.__ROOT, 0o777)   # all can write - in case the directory was created by su process # TODO: fails on BBe
        except FileExistsError:
            pass


    # TODO: add lock breaker on (long) timeout

    @classmethod
    def acquire(cls, name, timeout=1.0, verbose=False):
        """
        Acquire a lock with the given name.
        Raises a LockTimeout exception if the lock could not be acquired before timeout.
        """
        end_time = time.time() + timeout

        while not cls.__assert(name):
            if verbose:
                print("Lock.acquire: waiting for lock: " + name, file=sys.stderr)

            if time.time() > end_time:
                raise LockTimeout(name, cls.ident(name))

            time.sleep(random.uniform(0.000001, 0.001))


    @classmethod
    def exists(cls, name):
        """
        Returns True if a lock is asserted for the given name and current pID-tID.
        """
        return os.path.isdir(cls.__ident_dir(name))


    @classmethod
    def ident(cls, name):
        """
        Returns the ident for the lock with the given name, or None if there is no lock.
        The ident is the string "pID-tID", or None.
        """
        try:
            names = [os.listdir(cls.__name_dir(name))]

            if len(names) == 0:
                return None

            return names[0][0]
        except RuntimeError:
            return None


    @classmethod
    def release(cls, name):
        """
        Releases the lock for the given name and current pID-tID, if there is one.
        Returns True if there was a lock, and it was released.
        """
        try:
            if not cls.exists(name):
                return False

            os.rmdir(cls.__ident_dir(name))
            os.rmdir(cls.__name_dir(name))
            return True

        except FileNotFoundError:
            pass


    @classmethod
    def clear(cls, name):
        """
        Releases the lock for the given name, irrespective of pID-tID.
        Returns True if there was a lock, and it was cleared.

        Warning: clear is a last resort - it can have unpredictable consequences for other threads.
        """
        try:
            os.rmdir(cls.__name_dir(name) + "/" + cls.ident(name))
            os.rmdir(cls.__name_dir(name))
            return True

        except FileNotFoundError:
            pass


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def __assert(cls, name):
        try:
            os.mkdir(cls.__name_dir(name), 0o777)   # all can write - in case the directory was created by su process # TODO: fails on BBe
            os.mkdir(cls.__ident_dir(name), 0o777)   # all can write - in case the directory was created by su process # TODO: fails on BBe
            return True

        except FileExistsError:
            return False


    @classmethod
    def __name_dir(cls, name):
        return cls.__ROOT + name


    @classmethod
    def __ident_dir(cls, name):
        return cls.__name_dir(name) + "/" + str(os.getpid()) + "-" + str(threading.current_thread().ident)


# --------------------------------------------------------------------------------------------------------------------

Lock.init()
