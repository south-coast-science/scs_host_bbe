"""
Created on 12 May 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""


# --------------------------------------------------------------------------------------------------------------------

# noinspection PyUnusedLocal
class BluetoothConnection(object):
    """
    classdocs
    """

    WAITING = 1
    CONNECTED = 2
    DISCONNECTED = 3
    STOPPED = 4
    FAILED = 0


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def enable(cls):
        raise NotImplementedError


    @classmethod
    def monitor(cls):
        raise NotImplementedError


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, pipe_input):
        raise NotImplementedError


    def run(self):
        raise NotImplementedError


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        raise NotImplementedError

