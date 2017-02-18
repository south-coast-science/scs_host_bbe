"""
Created on 9 Nov 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import http.client

import urllib.parse


# --------------------------------------------------------------------------------------------------------------------

class HTTPClient(object):
    """
    classdocs
    """

    __STATUS_OK =           200
    __STATUS_CREATED =      201
    __STATUS_NO_CONTENT =   204


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self):
        """
        Constructor
        """
        self.__conn = None
        self.__host = None


    def connect(self, host):
        self.__conn = http.client.HTTPSConnection(host)
        self.__host = host


    def close(self):
        if self.__conn:
            self.__conn.close()


    # ----------------------------------------------------------------------------------------------------------------

    def get(self, path, payload, headers):
        # data...
        params = urllib.parse.urlencode(payload) if payload else None
        query = path + '?' + params if params else path

        # print("query:%s" % query)

        # request...
        self.__conn.request("GET", query, None, headers)
        response = self.__conn.getresponse()

        # response...
        if response.status != HTTPClient.__STATUS_OK:
            raise RuntimeError("HTTPClient.get: status:%d reason:%s" % (response.status, response.reason))

        data = response.read()

        return data.decode()


    def post(self, path, payload, headers):
        # request...
        self.__conn.request("POST", path, payload, headers)
        response = self.__conn.getresponse()

        # response...
        if response.status != HTTPClient.__STATUS_CREATED:
            raise RuntimeError("HTTPClient.post: status:%d reason:%s" % (response.status, response.reason))

        data = response.read()

        return data.decode()


    def put(self, path, payload, headers):
        # data...
        encoded_payload = urllib.parse.urlencode(payload) if payload else None

        # request...
        self.__conn.request("PUT", path, encoded_payload, headers)
        response = self.__conn.getresponse()

        # response...
        if response.status != HTTPClient.__STATUS_OK:
            raise RuntimeError("HTTPClient.put: status:%d reason:%s" % (response.status, response.reason))

        data = response.read()

        return data.decode()


    def delete(self, path, headers):
        # request...
        self.__conn.request("DELETE", path, "", headers)
        response = self.__conn.getresponse()

        # response...
        if response.status != HTTPClient.__STATUS_NO_CONTENT:
            raise RuntimeError("HTTPClient.delete: status:%d reason:%s" % (response.status, response.reason))

        data = response.read()

        return data.decode()


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "HTTPClient:{host:%s}" % self.__host
