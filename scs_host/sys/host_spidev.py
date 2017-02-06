"""
Created on 4 Jul 2016

http://tightdev.net/SpiDev_Doc.pdf
http://www.takaitra.com/posts/492

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

/boot/uEnv.txt...
cape_disable=bone_capemgr.disable_partno=BB-BONELT-HDMI,BB-BONELT-HDMIN
cape_enable=bone_capemgr.enable_partno=BB-SPIDEV0,BB-SPIDEV1

chmod a+rw /sys/devices/platform/bone_capemgr/slots
"""

import spidev


# TODO: does this work with current BBe o/s configuration?

# TODO: put tx lock in open / close

# --------------------------------------------------------------------------------------------------------------------

class HostSPIDev(object):
    """
    classdocs
    """
    __BUS = 1

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, device, mode, max_speed):
        """
        Constructor
        """

        self.__device = device
        self.__mode = mode
        self.__max_speed = max_speed

        self.__bus = None


    # ----------------------------------------------------------------------------------------------------------------

    def open(self):
        if self.__bus:
            return

        self.__bus = spidev.SpiDev()
        self.__bus.open(HostSPIDev.__BUS, self.__device)

        self.__bus.mode = self.__mode
        self.__bus.max_speed_hz = self.__max_speed


    def close(self):
        self.__bus.close()
        self.__bus = None


    # ----------------------------------------------------------------------------------------------------------------

    def xfer(self, args):
        self.__bus.xfer(args)


    def read_bytes(self, count):
        return self.__bus.readbytes(count)


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "HostSPIDev:{device:%s, mode:%d, max_speed:%d}" % (self.__device, self.__mode, self.__max_speed)



