"""
Created on 16 Nov 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""


# --------------------------------------------------------------------------------------------------------------------

class Host(object):
    """
    TI Sitara AM3358AZCZ100 processor
    """

    I2C_EEPROM =        2
    I2C_SENSORS =       2

    DFE_EEPROM_ADDR =   0x54

    DFE_EEP_IMAGE =     "/home/debian/SCS/dfe_cape.eep"     # hard-coded path

    SCS_LOCK =          "/run/lock/southcoastscience/"      # hard-coded path

    SCS_TMP =           "/tmp/southcoastscience/"           # hard-coded path

    __SCS_CONF =        "/home/debian/SCS/conf/"            # hard-coded path
    __SCS_OSIO =        "/home/debian/SCS/osio/"            # hard-coded path


    # ----------------------------------------------------------------------------------------------------------------

    @staticmethod
    def enable_eeprom_access():
        # nothing needs to be done
        pass


    @staticmethod
    def mcu_temp():
        return None


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def conf_dir(cls):
        return cls.__SCS_CONF


    @classmethod
    def osio_dir(cls):
        return cls.__SCS_OSIO
