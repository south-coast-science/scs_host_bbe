#!/usr/bin/env python3

"""
Created on 11 Nov 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

mosquitto_pub -h mqtt.opensensors.io -i <DeviceID> -t /users/<UserName>/<TopicName> -m 'This is a test message' -u <UserName> -P <Device Password>
mosquitto_pub -h mqtt.opensensors.io -i 5402 -t /users/southcoastscience-dev/test/text -m 'hello' -u southcoastscience-dev -P cPhbitmp

"""

from scs_host.client.mqtt_client import MQTTClient


# --------------------------------------------------------------------------------------------------------------------

username = "southcoastscience-dev"
print("username:%s" % username)

client_id = "5402"                      # text-test
print("client_id:%s" % client_id)

password = "cPhbitmp"
print("password:%s" % password)

print("-")

host = "mqtt.opensensors.io"
print("host:%s" % host)

topic = "/users/southcoastscience-dev/test/text"
print("topic:%s" % topic)

payload = "python message 11"
print("payload:%s" % payload)

print("-")


# --------------------------------------------------------------------------------------------------------------------

client = MQTTClient()
client.connect(host, client_id, username, password)
print(client)
print("-")

client.publish(topic, payload)
