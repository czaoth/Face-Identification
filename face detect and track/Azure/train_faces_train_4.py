########### Python 2.7 #############
import httplib, urllib, base64
from keys import SubscriptionKey

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': SubscriptionKey,
}

personGroupId = "0"

params = urllib.urlencode({
})

body = str({})

try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/persongroups/" + personGroupId + "/train?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))