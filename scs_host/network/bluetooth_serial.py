"""
Created on 12 May 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""


# --------------------------------------------------------------------------------------------------------------------

# noinspection PyUnusedLocal
class BluetoothSerial(object):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def monitor(cls, handler):
        raise NotImplementedError


    @classmethod
    def stop(cls):
        raise NotImplementedError


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, handler):
        raise NotImplementedError


    def run(self):
        raise NotImplementedError


    # ----------------------------------------------------------------------------------------------------------------

    def __read(self, fd):
        raise NotImplementedError


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        raise NotImplementedError

