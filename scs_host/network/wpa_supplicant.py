"""
Created on 12 May 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""


# --------------------------------------------------------------------------------------------------------------------

# noinspection PyUnusedLocal
class WPASupplicant(object):
    """
    classdocs
    """

    KEY_MGMT = None


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_entry(cls, entry):
        raise NotImplementedError


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, ssid, psk, key_mgmt):
        raise NotImplementedError


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        raise NotImplementedError


    def as_entry(self):
        raise NotImplementedError


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def ssid(self):
        raise NotImplementedError


    @property
    def psk(self):
        raise NotImplementedError


    @property
    def key_mgmt(self):
        raise NotImplementedError


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        raise NotImplementedError
