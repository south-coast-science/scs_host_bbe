'''
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
'''

from Adafruit_BBIO.SPI import SPI


# TODO: put tx lock in open / close

# --------------------------------------------------------------------------------------------------------------------

class BBIOSPI(object):
    '''
    classdocs
    '''

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, device, mode, max_speed):
        '''
        Constructor
        '''

        self.__device = device
        self.__mode = mode
        self.__max_speed = max_speed

        self.__bus = None


    # ----------------------------------------------------------------------------------------------------------------

    def open(self):
        self.__bus = SPI(0, self.__device)

        self.__bus.mode = self.__mode
        self.__bus.msh = self.__max_speed


    def close(self):
        self.__bus.close()


    # ----------------------------------------------------------------------------------------------------------------

    def xfer(self, args):
        self.__bus.xfer(args)


    def read_bytes(self, count):
        return self.__bus.readbytes(count)


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "HostSPI:{device:%s, mode:%d, max_speed:%d}" % (self.__device, self.__mode, self.__max_speed)

