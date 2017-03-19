"""
Created on 11 Nov 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

https://pypi.python.org/pypi/paho-mqtt
http://www.hivemq.com/blog/mqtt-client-library-paho-python
http://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels

mosquitto_pub -h mqtt.opensensors.io -i <DeviceID> -t /users/<UserName>/<TopicName> \
-m 'This is a test message' -u <UserName> -P <Device Password>

mosquitto_pub -h mqtt.opensensors.io -i 5402 -t /users/southcoastscience-dev/test/text \
-m 'hello' -u southcoastscience-dev -P cPhbitmp
"""

import time

import paho.mqtt.client as paho

import paho.mqtt.subscribe as subscribe


# --------------------------------------------------------------------------------------------------------------------

class MQTTClient(object):
    """
    classdocs
    """

    __PORT =        1883
    __TIMEOUT =     120

    __PUB_QOS =     1
    __SUB_QOS =     1


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self):
        """
        Constructor
        """
        self.__host = None
        self.__client_id = None
        self.__auth = None

        self.__client = None


    # ----------------------------------------------------------------------------------------------------------------

    def connect(self, host, client_id, username, password):         # only required for publish
        # ident for subscribe...
        self.__host = host
        self.__client_id = client_id
        self.__auth = {'username': username, 'password': password}

        # paho client...
        self.__client = paho.Client(client_id)

        self.__client.username_pw_set(username, password)
        self.__client.connect(host, MQTTClient.__PORT)

        self.__client.loop_start()


    def disconnect(self):
        self.__client.loop_stop()


    # ----------------------------------------------------------------------------------------------------------------

    def publish(self, topic, payload, timeout):
        msg_info = self.__client.publish(topic, str(payload), MQTTClient.__PUB_QOS)

        end_time = time.time() + timeout

        while time.time() < end_time:
            if msg_info.is_published():
                return True

            time.sleep(0.1)

        return False


    def subscribe(self, topic):     # TODO: update to threaded version?
        while True:
            message = subscribe.simple(topic, MQTTClient.__SUB_QOS, 1, False, self.__host, MQTTClient.__PORT,
                                       self.__client_id, MQTTClient.__TIMEOUT, None, self.__auth)

            payload = message.payload.decode()

            yield (payload)


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "MQTTClient:{host:%s, client_id:%s, auth:%s}" % (self.__host, self.__client_id, self.__auth)
