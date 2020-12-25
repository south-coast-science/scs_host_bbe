"""
Created on 5 Jul 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

http://ftp.de.debian.org/debian/pool/main/i/i2c-tools/
file: i2c-tools-3.1.1/include/linux/i2c-dev.h

Change i2c bus frequency on BeagleBone Black
http://randymxj.com/?p=538
"""

import fcntl
import io
import time

from scs_host.lock.lock import Lock
from scs_host.sys.host import Host


# --------------------------------------------------------------------------------------------------------------------

class I2C(object):
    """
    I2C bus abstraction over UNIX /dev/i2c-n
    """
    __I2C_SLAVE =           0x0703

    __I2C_SLAVE_FORCE =     0x0706
    __I2C_TENBIT =          0x0704
    __I2C_FUNCS =           0x0705
    __I2C_RDWR =            0x0707
    __I2C_PEC =             0x0708
    __I2C_SMBUS =           0x0720

    __LOCK_TIMEOUT =        2.0

    # ----------------------------------------------------------------------------------------------------------------

    Sensors = None
    Utilities = None
    EEPROM = None

    @classmethod
    def init(cls):
        bus = cls(Host.I2C_COMMON)

        cls.Sensors = bus
        cls.Utilities = bus
        cls.EEPROM = bus


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, bus):
        self.__bus = bus

        self.__fr = None
        self.__fw = None


    # ----------------------------------------------------------------------------------------------------------------

    def open(self):
        self.open_for_bus(self.__bus)


    def open_for_bus(self, bus):
        if self.__fr is not None and self.__fw is not None:
            if bus != self.__bus:
                raise RuntimeError("attempt to open bus %s when bus %s is already open" % (bus, self.__bus))
            return

        self.__fr = io.open("/dev/i2c-%d" % bus, "rb", buffering=0)
        self.__fw = io.open("/dev/i2c-%d" % bus, "wb", buffering=0)


    def close(self):
        if self.__fw is not None:
            self.__fw.close()
            self.__fw = None

        if self.__fr is not None:
            self.__fr.close()
            self.__fr = None


    # ----------------------------------------------------------------------------------------------------------------

    def start_tx(self, device):
        if self.__fr is None or self.__fw is None:
            self.open_for_bus(self.__bus)

        Lock.acquire(self.__class__.__name__, self.__LOCK_TIMEOUT)

        fcntl.ioctl(self.__fr, self.__I2C_SLAVE, device)
        fcntl.ioctl(self.__fw, self.__I2C_SLAVE, device)


    def end_tx(self):
        Lock.release(self.__class__.__name__)


    # ----------------------------------------------------------------------------------------------------------------

    def read(self, count):
        read_bytes = list(self.__fr.read(count))
        return read_bytes[0] if count == 1 else read_bytes


    def read_cmd(self, cmd, count, wait=None):
        try:
            iter(cmd)
            self.write(*cmd)

        except TypeError:
            self.write(cmd)

        if wait is not None:
            time.sleep(wait)

        return self.read(count)


    def read_cmd16(self, cmd16, count, wait=None):
        self.write16(cmd16)

        if wait is not None:
            time.sleep(wait)

        if count < 1:
            return []

        return self.read(count)


    # ----------------------------------------------------------------------------------------------------------------

    def write(self, *values):
        self.__fw.write(bytearray(values))


    def write16(self, *value16s):
        write_bytes = bytearray()

        for value16 in value16s:
            write_bytes += bytes([value16 >> 8])
            write_bytes += bytes([value16 & 0xff])

        self.__fw.write(write_bytes)


    def write_addr(self, addr, *values):
        self.__fw.write(bytearray([addr]) + bytes(values))


    def write_addr16(self, addr, *values):
        addr_msb = addr >> 8
        addr_lsb = addr & 0xff

        self.__fw.write(bytearray([addr_msb, addr_lsb]) + bytes(values))


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def bus(self):
        return self.__bus


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "I2C:{bus:%s, fr:%s, fw:%s}" % (self.bus, self.__fr, self.__fw)
