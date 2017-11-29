"""
Created on 30 May 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

A network socket abstraction, implementing ProcessComms
"""

import socket
import time

from scs_core.sys.process_comms import ProcessComms


# --------------------------------------------------------------------------------------------------------------------

class NetworkSocket(ProcessComms):
    """
    classdocs
    """

    __TIMEOUT =         4.0         # seconds
    __BUFFER_SIZE =     1024        # bytes
    __BACKLOG =         5

    __ACK =             "ACK"


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, host, port=2000):        # a receiving socket should have host ''
        """
        Constructor
        """
        self.__address = (host, port)

        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__conn = None


    # ----------------------------------------------------------------------------------------------------------------

    def connect(self, wait_for_availability=True):
        while True:
            try:
                self.__socket.connect(self.__address)
                break

            except ConnectionRefusedError as ex:
                if not wait_for_availability:
                    raise ConnectionRefusedError(ex)

                time.sleep(0.1)


    def close(self):
        try:
            if self.__conn:
                self.__conn.close()
        except RuntimeError:
            pass

        try:
            self.__socket.close()
        except RuntimeError:
            pass


    # ----------------------------------------------------------------------------------------------------------------

    def read(self):
        # socket...
        self.__socket.bind(self.__address)
        self.__socket.listen(NetworkSocket.__BACKLOG)

        self.__conn, _ = self.__socket.accept()

        # data...
        while True:
            message = self.__conn.recv(NetworkSocket.__BUFFER_SIZE).decode().strip()

            if len(message) == 0:
                break

            yield message


    def write(self, message, wait_for_availability=True):
        while True:
            try:
                # data...
                self.__socket.send(message.encode())

                # wait for ACK...
                timeout = time.time() + NetworkSocket.__TIMEOUT

                while self.__socket.recv(NetworkSocket.__BUFFER_SIZE).decode() != NetworkSocket.__ACK:
                    time.sleep(0.001)

                    if time.time() > timeout:
                        break

                break

            except BrokenPipeError as ex:
                if not wait_for_availability:
                    raise ConnectionRefusedError(ex)

                self.close()

                time.sleep(0.1)

                self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.connect(True)


    # ----------------------------------------------------------------------------------------------------------------

    def ack(self):
        self.__conn.send(str(NetworkSocket.__ACK).encode())


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "NetworkSocket:{address:%s, socket:%s}" % (self.__address, self.__socket)
