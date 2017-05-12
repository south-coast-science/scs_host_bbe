"""
Created on 4 Nov 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md
http://unix.stackexchange.com/questions/92799/connecting-to-wifi-network-through-command-line

sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
"""

import re
import subprocess

from collections import OrderedDict

from scs_core.data.json import JSONable


# --------------------------------------------------------------------------------------------------------------------

class Interface(JSONable):
    """
    classdocs

    eth0      Link encap:Ethernet  HWaddr b8:27:eb:a1:f8:b9
              inet addr:192.168.1.9  Bcast:192.168.1.255  Mask:255.255.255.0
              inet6 addr: fe80::26fa:583e:7d87:e803/64 Scope:Link
    """

    WIFI = "wlan0"          # TODO: needs to be in a file or something


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def find(cls, name):
        interfaces = Interface.__config(name)

        return interfaces[0] if len(interfaces) else None


    @classmethod
    def find_all(cls):
        interfaces = Interface.__config()

        return interfaces


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def __config(cls, name='-a'):
        interfaces = []
        interface = None

        p = subprocess.Popen(['ifconfig', name], stdout=subprocess.PIPE)
        response = p.communicate()

        scan = response[0].decode()

        # parse...
        for line in scan.splitlines():

            # new interface, name...
            matches = re.search(r'([0-9A-Za-z]+)\s+Link encap:', line)
            if matches:
                if interface:
                    interfaces.append(interface)

                interface = Interface()

                interface.__name = matches.group(1)

            # hw_addr...
            matches = re.search(r'HWaddr\s+([0-9a-f:]+)', line)
            if matches:
                interface.__hw_addr = matches.group(1)
                continue

            # inet addr...
            matches = re.search(r'inet addr:\s*([0-9.]+)', line)
            if matches:
                interface.__inet_addr = matches.group(1)
                continue

            # inet6_addr, scope...
            matches = re.search(r'inet6 addr:\s*([0-9a-f:/]+)\s+Scope:\s*([0-9A-Za-z]+)', line)
            if matches:
                interface.__inet6_addr = matches.group(1)
                interface.__scope = matches.group(2)

        if interface:
            interfaces.append(interface)

        return interfaces


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, name=None, scope=None, hw_addr=None, inet_addr=None, inet6_addr=None):
        """
        Constructor
        """
        self.__name = name
        self.__scope = scope
        self.__hw_addr = hw_addr
        self.__inet_addr = inet_addr
        self.__inet6_addr = inet6_addr


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['name'] = self.name
        jdict['scope'] = self.scope
        jdict['hw_addr'] = self.hw_addr
        jdict['inet_addr'] = self.inet_addr
        jdict['inet6_addr'] = self.inet6_addr

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    def connect(self, supplicant):
        """
        sudo iwconfig wlan0 essid Wifi2Home key s:ABCDE12345
        """
        pass        # TODO: implement connect(..)


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def name(self):
        return self.__name


    @property
    def scope(self):
        return self.__scope


    @property
    def hw_addr(self):
        return self.__hw_addr


    @property
    def inet_addr(self):
        return self.__inet_addr


    @property
    def inet6_addr(self):
        return self.__inet6_addr


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "Interface:{name:%s, scope:%s, hw_addr:%s, inet_addr:%s, inet6_addr:%s}" % \
                    (self.name, self.scope, self.hw_addr, self.inet_addr, self.inet6_addr)
