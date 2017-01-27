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

    SCS_CONF = "/home/debian/SCS/conf/"         # hard-coded path
    SCS_OSIO = "/home/debian/SCS/osio/"         # hard-coded path


    # ----------------------------------------------------------------------------------------------------------------

    @staticmethod
    def enable_eeprom_access():
        # nothing needs to be done
        pass


    @staticmethod
    def mcu_temp():
        # TODO: implement mcu_temp()
        return None
