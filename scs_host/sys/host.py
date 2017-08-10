"""
Created on 16 Nov 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

http://dumb-looks-free.blogspot.co.uk/2014/05/beaglebone-black-bbb-revision-serial.html

"""

import os
import socket
import subprocess


# --------------------------------------------------------------------------------------------------------------------

class Host(object):
    """
    TI Sitara AM3358AZCZ100 processor
    """

    I2C_EEPROM =        2
    I2C_SENSORS =       2

    DFE_EEPROM_ADDR =   0x50
    DFE_UID_ADDR =      0x58

    COMMAND_DIR =       "/home/debian/SCS/cmd/"             # hard-coded path

    DFE_EEP_IMAGE =     "/home/debian/SCS/dfe_cape.eep"     # hard-coded path

    SCS_LOCK =          "/run/lock/southcoastscience/"      # hard-coded path

    SCS_TMP =           "/tmp/southcoastscience/"           # hard-coded path


    # ----------------------------------------------------------------------------------------------------------------

    __NDIR_DEVICE =     "/dev/ttyUSB0"                      # hard-coded path

    __PSU_DEVICE =      5                                   # hard-coded path

    __SCS_CONF =        "/home/debian/SCS/conf/"            # hard-coded path
    __SCS_OSIO =        "/home/debian/SCS/osio/"            # hard-coded path


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
    def ndir_device(cls):
        return cls.__NDIR_DEVICE            # we might have to search for it instead


    @classmethod
    def psu_device(cls):
        return cls.__PSU_DEVICE            # we might have to search for it instead


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def name(cls):
        return socket.gethostname()


    @classmethod
    def conf_dir(cls):
        return cls.__SCS_CONF


    @classmethod
    def osio_dir(cls):
        return cls.__SCS_OSIO
