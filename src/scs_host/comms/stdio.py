"""
Created on 27 May 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

A stdio abstraction, implementing ProcessComms
"""

import sys

from scs_core.sys.process_comms import ProcessComms


# --------------------------------------------------------------------------------------------------------------------

class StdIO(ProcessComms):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def prompt(cls, prompt_str):
        print(prompt_str, end="")
        sys.stdout.flush()

        line = sys.stdin.readline()
        sys.stdout.flush()

        return line.strip()


    # ----------------------------------------------------------------------------------------------------------------

    def connect(self, wait_for_availability=True):
        pass


    def close(self):
        sys.stdout.flush()


    # ----------------------------------------------------------------------------------------------------------------

    def read(self):
        for line in sys.stdin:
            yield line.strip()


    def write(self, message, wait_for_availability=True):       # message should be flushed on close
        print(message.strip())


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
            return "StdIO:{}"
