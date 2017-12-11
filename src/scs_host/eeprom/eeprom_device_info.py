"""
Created on 27 Jan 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

http://elinux.org/Beagleboard:Cape_Expansion_Headers#Cape_EEPROM_Contents
"""


# --------------------------------------------------------------------------------------------------------------------

class EEPROMDeviceInfo(object):
    """
    classdocs
    """

    HEADER = b'\xAA\x55\x33\xEE'
    REV = b'A1'

    HEADER_SIZE = 4
    REV_SIZE = 2
    NAME_SIZE = 32
    VERSION_SIZE = 4
    MANUFACTURER_SIZE = 16
    PART_NUMBER_SIZE = 16
    NUMBER_OF_PINS_SIZE = 2
    SERIAL_NUMBER_SIZE = 12
    PIN_USAGE_SIZE = 148
    VDD_3V3_CURRENT_SIZE = 2
    VDD_5V_CURRENT_SIZE = 2
    SYS_5V_CURRENT_SIZE = 2
    DC_SUPPLIED_SIZE = 2

    AVAILABLE_SIZE = 32543


    # ----------------------------------------------------------------------------------------------------------------

    """
    Load a .eep image
    """
    @classmethod
    def construct_from_image(cls, image):
        # TODO: implement construct_from_image()
        pass


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, content):
        """W
        Constructor
        """
        self.__content = content


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def content(self):
        return self.__content


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "EEPROMDeviceInfo:{content:%s}" % self.content
