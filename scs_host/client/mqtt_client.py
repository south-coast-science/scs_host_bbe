"""
Created on 11 Nov 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

https://pypi.python.org/pypi/paho-mqtt
http://www.hivemq.com/blog/mqtt-client-library-paho-python


mosquitto_pub -h mqtt.opensensors.io -i <DeviceID> -t /users/<UserName>/<TopicName> -m 'This is a test message' \
-u <UserName> -P <Device Password>

mosquitto_pub -h mqtt.opensensors.io -i 5402 -t /users/southcoastscience-dev/test/text -m 'hello' \
-u southcoastscience-dev -P cPhbitmp
"""

import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe


# --------------------------------------------------------------------------------------------------------------------

class MQTTClient(object):
    """
    classdocs
    """

    __PORT =        1883
    __TIMEOUT =     60

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


    def connect(self, host, client_id, user_id, password):
        self.__host = host
        self.__client_id = client_id
        self.__auth = {'username': user_id, 'password': password}


    # ----------------------------------------------------------------------------------------------------------------

    def publish(self, topic, payload):
        publish.single(topic, payload, MQTTClient.__PUB_QOS, False, self.__host, MQTTClient.__PORT,
                       self.__client_id, MQTTClient.__TIMEOUT, None, self.__auth)


    def subscribe(self, topic):
        while True:
            message = subscribe.simple(topic, MQTTClient.__SUB_QOS, 1, False, self.__host, MQTTClient.__PORT,
                                       self.__client_id, MQTTClient.__TIMEOUT, None, self.__auth)

            payload = message.payload.decode()

            yield (payload)


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "MQTTClient:{host:%s, client_id:%s, auth:%s}" % (self.__host, self.__client_id, self.__auth)
