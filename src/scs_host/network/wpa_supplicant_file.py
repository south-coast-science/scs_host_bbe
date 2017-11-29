"""
Created on 12 May 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""


# --------------------------------------------------------------------------------------------------------------------

# noinspection PyUnusedLocal
class WPASupplicantFile(object):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def init(cls):
        raise NotImplementedError


    @classmethod
    def read(cls):
        raise NotImplementedError


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, headers, supplicants):
        raise NotImplementedError


    def write(self):
        raise NotImplementedError

    # ----------------------------------------------------------------------------------------------------------------

    def insert(self, supplicant):
        raise NotImplementedError


    def remove(self, ssid):
        raise NotImplementedError

    # ----------------------------------------------------------------------------------------------------------------

    @property
    def headers(self):
        raise NotImplementedError


    @property
    def supplicants(self):
        raise NotImplementedError


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        raise NotImplementedError
