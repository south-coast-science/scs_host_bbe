"""
Created on 12 May 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""


# --------------------------------------------------------------------------------------------------------------------

class WiFiConnection(object):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def enable(cls):
        raise NotImplementedError


    @classmethod
    def disable(cls):
        raise NotImplementedError


    @classmethod
    def connect(cls, ssid):
        raise NotImplementedError
