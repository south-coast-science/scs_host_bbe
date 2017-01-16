#!/usr/bin/env python3

"""
Created on 9 Nov 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from scs_host.client.http_client import HTTPClient


# --------------------------------------------------------------------------------------------------------------------

host = "api.opensensors.io"
print("host:%s" % host)

headers = {"Accept": "application/json", "Authorization": "api-key 43308b72-ad41-4555-b075-b4245c1971db"}
print("headers:%s" % headers)

path = "/v1/orgs/south-coast-science-dev/topics"
print("path:%s" % path)


# --------------------------------------------------------------------------------------------------------------------

client = HTTPClient()
client.connect(host)
print(client)

try:
    data = client.get(path, None, headers)
    print(data)

except Exception as ex:
    raise ex

finally:
    client.close()

