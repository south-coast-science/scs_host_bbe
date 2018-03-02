"""
Created on 16 Nov 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

http://dumb-looks-free.blogspot.co.uk/2014/05/beaglebone-black-bbb-revision-serial.html

"""

import os
import socket
import subprocess

from scs_core.sys.node import Node


# --------------------------------------------------------------------------------------------------------------------

class Host(Node):
    """
    TI Sitara AM3358AZCZ100 processor
    """

    OS_ENV_PATH =           'SCS_ROOT_PATH'

    I2C_EEPROM =            2
    I2C_SENSORS =           2

    DFE_EEPROM_ADDR =       0x50
    DFE_UID_ADDR =          0x58


    # ----------------------------------------------------------------------------------------------------------------
    # devices...

    __OPC_SPI_BUS =         0                                   # based on Adafruit_BBIO.SPI
    __OPC_SPI_DEVICE =      0                                   # based on Adafruit_BBIO.SPI

    __NDIR_SPI_BUS =        1                                   # based on Adafruit_BBIO.SPI
    __NDIR_SPI_DEVICE =     0                                   # based on Adafruit_BBIO.SPI

    __GPS_DEVICE =          1                                   # hard-coded path

    __NDIR_USB_DEVICE =     '/dev/ttyUSB0'                      # hard-coded path

    __PSU_DEVICE =          5                                   # hard-coded path


    # ----------------------------------------------------------------------------------------------------------------
    # directories...

    __DEFAULT_HOME_DIR =    '/home/debian'                      # hard-coded abs path
    __LOCK_DIR =            '/run/lock/southcoastscience'       # hard-coded abs path
    __TMP_DIR =             '/tmp/southcoastscience'            # hard-coded abs path

    __SCS_DIR =             'SCS'                               # hard-coded rel path

    __COMMAND_DIR =         'cmd'                               # hard-coded rel path
    __CONF_DIR =            'conf'                              # hard-coded rel path
    __AWS_DIR =             'aws'                               # hard-coded rel path
    __OSIO_DIR =            'osio'                              # hard-coded rel path
    __DFE_EEP_IMAGE =       'dfe_cape.eep'                      # hard-coded rel path


    # ----------------------------------------------------------------------------------------------------------------

    @staticmethod
    def serial_number():
        serial = os.popen("hexdump -e '8/1 \"%c\"' /sys/bus/i2c/devices/0-0050/eeprom -s 16 -n 12").readline()

        return serial


    @staticmethod
    def power_cycle():
        subprocess.call(['sudo', 'reboot'])     # TODO: control the power cycle feature on the PSU


    @staticmethod
    def enable_eeprom_access():
        # nothing needs to be done?
        pass


    @staticmethod
    def mcu_temp():
        return None


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def gps_device(cls):
        return cls.__GPS_DEVICE             # we might have to search for it instead


    @classmethod
    def ndir_usb_device(cls):
        return cls.__NDIR_USB_DEVICE        # we might have to search for it instead


    @classmethod
    def psu_device(cls):
        return cls.__PSU_DEVICE             # we might have to search for it instead


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def name(cls):
        return socket.gethostname()


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def ndir_spi_bus(cls):
        return cls.__NDIR_SPI_BUS


    @classmethod
    def ndir_spi_device(cls):
        return cls.__NDIR_SPI_DEVICE


    @classmethod
    def opc_spi_bus(cls):
        return cls.__OPC_SPI_BUS


    @classmethod
    def opc_spi_device(cls):
        return cls.__OPC_SPI_DEVICE


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def home_dir(cls):
        return os.environ[cls.OS_ENV_PATH] if cls.OS_ENV_PATH in os.environ else cls.__DEFAULT_HOME_DIR


    @classmethod
    def lock_dir(cls):
        return cls.__LOCK_DIR


    @classmethod
    def tmp_dir(cls):
        return cls.__TMP_DIR


    @classmethod
    def scs_dir(cls):
        return os.path.join(cls.home_dir(), cls.__SCS_DIR)


    @classmethod
    def command_dir(cls):
        return os.path.join(cls.home_dir(), cls.__SCS_DIR, cls.__COMMAND_DIR)


    @classmethod
    def conf_dir(cls):
        return os.path.join(cls.home_dir(), cls.__SCS_DIR, cls.__CONF_DIR)


    @classmethod
    def aws_dir(cls):
        return os.path.join(cls.home_dir(), cls.__SCS_DIR, cls.__AWS_DIR)


    @classmethod
    def osio_dir(cls):
        return os.path.join(cls.home_dir(), cls.__SCS_DIR, cls.__OSIO_DIR)


    @classmethod
    def eep_image(cls):
        return os.path.join(cls.home_dir(), cls.__SCS_DIR, cls.__DFE_EEP_IMAGE)
