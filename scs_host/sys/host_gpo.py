"""
Created on 22 Dec 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

https://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black/using-the-bbio-library
"""

import Adafruit_BBIO.GPIO as GPIO


# TODO: add lock functionality

# --------------------------------------------------------------------------------------------------------------------

class HostGPO(object):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, pin, state):
        """
        Constructor
        """
        self.__pin = pin

        GPIO.setup(self.__pin, GPIO.OUT)

        self.state = state


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def state(self):
        return self.__state


    @state.setter
    def state(self, state):
        self.__state = state

        GPIO.output(self.__pin, self.__state)


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "HostGPO:{pin:%s, state:%d}" % (self.__pin, self.__state)
