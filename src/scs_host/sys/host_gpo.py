"""
Created on 22 Dec 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

https://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black/using-the-bbio-library
"""


from scs_host.sys.host_gpio import HostGPIO


# TODO: add lock functionality

# --------------------------------------------------------------------------------------------------------------------

class HostGPO(HostGPIO):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, pin, state):
        """
        Constructor
        """
        self.__pin = pin
        self.__state = None

        HostGPIO.setup(self.__pin, HostGPO.OUT)

        self.state = state


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def state(self):
        return self.__state


    @state.setter
    def state(self, state):
        self.__state = state

        HostGPIO.output(self.__pin, self.__state)


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "HostGPO:{pin:%s, state:%d}" % (self.__pin, self.__state)
