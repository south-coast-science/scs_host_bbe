"""
Created on 20 Oct 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import socket
import time


# --------------------------------------------------------------------------------------------------------------------

class SocketSender(object):
    """
    classdocs
    """

    __TIMEOUT =         4.0         # seconds
    __BUFFER_SIZE =     1024        # bytes

    __ACK =             "ACK"


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, host, port, verbose=False):
        """
        Constructor
        """
        self.__verbose = verbose

        self.__address = (host, port)

        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.connect(self.__address)


    # ----------------------------------------------------------------------------------------------------------------

    def sender(self):
        while True:
            message = (yield)

            self.__send(message)


    def close(self):
        if self.__verbose:
            print("SocketSender: disconnect.")

        self.__socket.close()

        if self.__verbose:
            print("SocketSender: closed.")


    # ----------------------------------------------------------------------------------------------------------------

    def __send(self, message):
        # send...
        self.__socket.send(message.encode())

        # wait for ACK...
        timeout = time.time() + SocketSender.__TIMEOUT

        while self.__socket.recv(SocketSender.__BUFFER_SIZE).decode() != SocketSender.__ACK:
            time.sleep(0.001)

            if time.time() > timeout:
                break


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def address(self):
        return self.__address


    @property
    def verbose(self):
        return self.__verbose


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "SocketSender:{address:%s, verbose:%s}" % (str(self.address), self.verbose)
