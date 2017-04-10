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

import json
import time

from collections import OrderedDict

import paho.mqtt.client as paho

from scs_core.data.json import JSONify
from scs_core.data.publication import Publication


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

    def __init__(self, subscriber=None):        # TODO: handle multiple subscriptions
        """
        Constructor
        """
        self.__client = None
        self.__subscriber = subscriber


    # ----------------------------------------------------------------------------------------------------------------

    def connect(self, host, client_id, username, password):
        # paho client...
        self.__client = paho.Client(client_id)

        # event handling...
        self.__client.on_connect = self.on_connect
        self.__client.on_message = self.on_message

        # connect...
        self.__client.username_pw_set(username, password)
        self.__client.connect(host, MQTTClient.__PORT)

        # start thread...
        self.__client.loop_start()


    def disconnect(self):
        self.__client.loop_stop()


    # ----------------------------------------------------------------------------------------------------------------

    def publish(self, publication, timeout):
        payload = JSONify.dumps(publication.payload)

        msg_info = self.__client.publish(publication.topic, payload, MQTTClient.__PUB_QOS)

        end_time = time.time() + timeout

        while time.time() < end_time:
            if msg_info.is_published():
                return True

            time.sleep(0.1)

        return False


    # ----------------------------------------------------------------------------------------------------------------

    # noinspection PyUnusedLocal
    def on_connect(self, client, userdata, flags, rc):
        if self.__subscriber:
            self.__client.subscribe(self.__subscriber.topic, qos=MQTTClient.__SUB_QOS)


    # noinspection PyUnusedLocal
    def on_message(self, client, userdata, msg):
        if self.__subscriber:
            payload = msg.payload.decode()
            payload_jdict = json.loads(payload, object_pairs_hook=OrderedDict)

            self.__subscriber.handler(Publication(self.__subscriber.topic, payload_jdict))


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "MQTTClient:{subscriber:%s}" % self.__subscriber


# --------------------------------------------------------------------------------------------------------------------

class MQTTSubscriber(object):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, topic, handler):
        """
        Constructor
        """
        self.__topic = topic
        self.__handler = handler


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def topic(self):
        return self.__topic


    @property
    def handler(self):
        return self.__handler


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "MQTTSubscriber:{topic:%s, handler:%s}" % (self.topic, self.handler)
