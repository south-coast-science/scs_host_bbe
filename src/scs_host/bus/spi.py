"""
Created on 4 Jul 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

http://wiki.minnowboard.org/Projects/AdaFruit_GPIO
https://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black/spi
https://github.com/adafruit/adafruit-beaglebone-io-python/blob/master/source/spimodule.c

https://groups.google.com/forum/#!topic/beagleboard/x6VjN_q00c4

/boot/uEnv.txt...
cape_disable=bone_capemgr.disable_partno=BB-BONELT-HDMI,BB-BONELT-HDMIN
cape_enable=bone_capemgr.enable_partno=BB-SPIDEV0,BB-SPIDEV1

chmod a+rw /sys/devices/platform/bone_capemgr/slots
"""

from Adafruit_BBIO.SPI import SPI as ASPI

from scs_host.lock.lock import Lock


# --------------------------------------------------------------------------------------------------------------------

class SPI(object):
    """
    classdocs
    """
    __LOCK_TIMEOUT =        1.0


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, bus, device, mode, max_speed):
        """
        Constructor
        """

        self.__bus = bus
        self.__device = device
        self.__mode = mode
        self.__max_speed = max_speed

        self.__connection = None


    # ----------------------------------------------------------------------------------------------------------------

    def open(self):
        Lock.acquire(SPI.__name__ + str(self.__bus), SPI.__LOCK_TIMEOUT)

        self.__connection = ASPI(self.__bus, self.__device)

        self.__connection.mode = self.__mode
        self.__connection.msh = self.__max_speed


    def close(self):
        if self.__connection is None:
            return

        self.__connection.close()
        self.__connection = None

        Lock.release(SPI.__name__ + str(self.__bus))


    # ----------------------------------------------------------------------------------------------------------------

    def xfer(self, args):
        self.__connection.xfer(args)


    def read_bytes(self, count):
        return self.__connection.readbytes(count)


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "SPI:{bus:%d, device:%s, mode:%d, max_speed:%d, connection:%s}" % \
               (self.__bus, self.__device, self.__mode, self.__max_speed, self.__connection)
