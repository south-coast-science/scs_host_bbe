"""
Created on 4 Nov 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md

sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
"""

import socket
import subprocess

from collections import OrderedDict

from scs_core.data.json import JSONable


# --------------------------------------------------------------------------------------------------------------------

class Hostname(JSONable):
    """
    classdocs
    """

    __HOSTNAME_FILE =       "/etc/hostname"
    __HOSTS_FILE =          "/etc/hosts"


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def find(cls):
        # operational...
        operational = socket.gethostname()

        # specified...
        p = subprocess.Popen(['sudo', 'cat', cls.__HOSTNAME_FILE], stdout=subprocess.PIPE)
        response = p.communicate()

        specified = response[0].decode().strip()

        return Hostname(operational, specified)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, operational, specified):
        """
        Constructor
        """
        self.__operational = operational
        self.__specified = specified


    # ----------------------------------------------------------------------------------------------------------------

    def specify(self, specified):
        # TODO: implement specify(..)
        pass


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['op'] = self.operational
        jdict['spec'] = self.specified

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def operational(self):
        return self.__operational


    @property
    def specified(self):
        return self.__specified


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "Hostname:{operational:%s, specified:%s}" % (self.operational, self.specified)
