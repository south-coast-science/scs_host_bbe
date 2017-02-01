"""
Created on 5 Jul 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

https://www.raspberrypi.org/forums/viewtopic.php?f=32&t=134997
https://github.com/raspberrypi/weather-station/blob/master/i2c_base.py

https://blogs.ncl.ac.uk/francisfranklin/2014/03/23/using-i2c-with-the-raspberry-pi-step-1-modules-and-packages/
speed: /etc/modprobe.d/I2C.conf

http://ftp.de.debian.org/debian/pool/main/i/i2c-tools/
file: i2c-tools-3.1.1/include/linux/i2c-dev.h
"""

import fcntl
import io

from scs_host.lock.lock import Lock


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

    __FR = None
    __FW = None


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def open(cls, bus):
        if cls.__FR is not None and cls.__FW is not None:
            return

        cls.__FR = io.open("/dev/i2c-%d" % bus, "rb", buffering=0)      # hard-coded path
        cls.__FW = io.open("/dev/i2c-%d" % bus, "wb", buffering=0)      # hard-coded path


    @classmethod
    def close(cls):
        if cls.__FW is not None:
            cls.__FW.close()
            cls.__FW = None

        if cls.__FR is not None:
            cls.__FR.close()
            cls.__FR = None


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def start_tx(cls, device):
        if cls.__FR is None or cls.__FW is None:
            raise RuntimeError("I2C.start_tx: bus is not open.")

        Lock.acquire(I2C.__name__, 1.0, False)

        fcntl.ioctl(cls.__FR, I2C.__I2C_SLAVE, device)
        fcntl.ioctl(cls.__FW, I2C.__I2C_SLAVE, device)


    @classmethod
    def end_tx(cls):
        Lock.release(I2C.__name__)


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def read(cls, count):
        read_bytes = list(I2C.__FR.read(count))
        return read_bytes[0] if count == 1 else read_bytes


    @classmethod
    def read_cmd(cls, cmd, count):
        cls.write(cmd)
        return cls.read(count)


    @classmethod
    def read_cmd16(cls, cmd16, count):
        cls.write16(cmd16)
        return cls.read(count)


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def write(cls, *values):
        I2C.__FW.write(bytearray(values))


    @classmethod
    def write16(cls, *value16s):
        write_bytes = bytearray()

        for value16 in value16s:
            write_bytes.append(value16 >> 8)
            write_bytes.append(value16 & 0xff)

        I2C.__FW.write(write_bytes)


    @classmethod
    def write_addr(cls, addr, *values):
        I2C.__FW.write(bytearray([addr]) + bytearray(values))


    @classmethod
    def write_addr16(cls, addr, *values):
        addr_msb = addr >> 8
        addr_lsb = addr & 0xff

        I2C.__FW.write(bytearray([addr_msb, addr_lsb]) + bytearray(values))
