"""
Created on 10 Aug 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import os
import random
import time

from scs_host.lock.lock_timeout import LockTimeout
from scs_host.sys.host import Host


# --------------------------------------------------------------------------------------------------------------------

class Lock(object):
    """
    a general-purpose mutex
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def init(cls):
        """
        Establish the /run/lock/southcoastscience root.
        Should be invoked on class load.
        """
        try:
            os.mkdir(Host.SCS_LOCK)
            os.chmod(Host.SCS_LOCK, 0o777)
        except FileExistsError:
            pass


    @classmethod
    def acquire(cls, name, timeout=1.0):
        """
        Acquire a lock with the given name.
        Raises a LockTimeout exception if the lock could not be acquired before timeout.
        """
        end_time = time.time() + timeout

        while not cls.__assert(name):
            pid = cls.pid(name)

            # process exists?...
            if not cls.__process_exists(pid):
                cls.clear(name, pid)
                continue

            # wait...
            if time.time() > end_time:
                raise LockTimeout(name, cls.pid(name))

            time.sleep(random.uniform(0.000001, 0.001))


    @classmethod
    def exists(cls, name):
        """
        Returns True if a lock is asserted for the given name and this process' pid.
        """
        return os.path.isdir(cls.__name_dir(name))


    @classmethod
    def pid(cls, name):
        """
        Returns the pid for the lock with the given name, or None if there is no lock.
        """
        try:
            names = [os.listdir(cls.__name_dir(name))]

        except FileNotFoundError:
            return None

        try:
            if len(names) == 0:
                return None

            return int(names[0][0])

        except IndexError:
            return None


    @classmethod
    def release(cls, name):
        """
        Releases the lock for the given name and process' pid.
        Returns True if there was a lock.
        """
        try:
            os.rmdir(cls.__ident_dir(name, os.getpid()))
            os.rmdir(cls.__name_dir(name))
            return True

        except FileNotFoundError:
            return False


    @classmethod
    def clear(cls, name, pid):
        """
        Releases the lock for the given name and pid.
        Returns True if there was a lock.
        """
        try:
            os.rmdir(cls.__ident_dir(name, pid))
            os.rmdir(cls.__name_dir(name))
            return True

        except FileNotFoundError:
            return False


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def __process_exists(cls, pid):
        if pid is None:
            return False

        try:
            os.kill(pid, 0)
            return True

        except OSError:
            return False


    @classmethod
    def __assert(cls, name):
        name_dir = cls.__name_dir(name)
        ident_dir = cls.__ident_dir(name, os.getpid())

        try:
            os.mkdir(name_dir)
            os.mkdir(ident_dir)

            os.chmod(name_dir, 0o777)
            os.chmod(ident_dir, 0o777)
            return True

        except FileExistsError:
            return False


    @classmethod
    def __name_dir(cls, name):
        return Host.SCS_LOCK + name


    @classmethod
    def __ident_dir(cls, name, pid):
        return cls.__name_dir(name) + "/" + str(pid)


# --------------------------------------------------------------------------------------------------------------------

Lock.init()     # TODO: put .init() in package init throughout
