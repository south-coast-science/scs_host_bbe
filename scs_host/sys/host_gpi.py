"""
Created on 22 Dec 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

https://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black/using-the-bbio-library
"""

from scs_host.sys.host_gpio import HostGPIO


# TODO: add lock functionality

# --------------------------------------------------------------------------------------------------------------------

class HostGPI(HostGPIO):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, pin):
        """
        Constructor
        """
        self.__pin = pin

        HostGPIO.setup(self.__pin, HostGPIO.IN)


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def state(self):
        return HostGPIO.input(self.__pin)


    def wait(self, edge):
        HostGPIO.wait_for_edge(self.__pin, edge)        # TODO: do a generator one - change of state?


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "HostGPI:{pin:%s, state:%d}" % (self.__pin, self.state)

