"""
Created on 12 May 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""


# --------------------------------------------------------------------------------------------------------------------

# noinspection PyUnusedLocal
class WiFiStation(object):
    """
    classdocs
    """

    @classmethod
    def find_all(cls):
        raise NotImplementedError


    @classmethod
    def exists(cls, ssid):
        raise NotImplementedError


    @classmethod
    def find_connected(cls):
        raise NotImplementedError


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, ssid=None, encryption=None, quality=None, security=None, is_connected=None):
        raise NotImplementedError


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        raise NotImplementedError


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def ssid(self):
        raise NotImplementedError


    @property
    def encryption(self):
        raise NotImplementedError


    @property
    def quality(self):
        raise NotImplementedError


    @property
    def security(self):
        raise NotImplementedError


    @property
    def is_connected(self):
        raise NotImplementedError


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        raise NotImplementedError
