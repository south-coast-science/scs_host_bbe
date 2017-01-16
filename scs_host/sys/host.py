'''
Created on 16 Nov 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
'''


# --------------------------------------------------------------------------------------------------------------------

class Host(object):
    '''
    TI Sitara AM3358AZCZ100 processor
    '''

    I2C_EEPROM =        2
    I2C_SENSORS =       2

    SCS_CONF = '/home/debian/SCS/conf/'
    SCS_OSIO = '/home/debian/SCS/osio/'


    # ----------------------------------------------------------------------------------------------------------------

    @staticmethod
    def mcu_temp():
        return None
