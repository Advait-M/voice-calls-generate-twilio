# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
import json
with open('secrets.json') as handle:
    secrets = json.loads(handle.read())
account_sid = secrets["account_sid"]
auth_token = secrets["auth_token"]
client = Client(account_sid, auth_token)

import xml.etree.cElementTree as ET

root = ET.Element("Response")
# say = ET.SubElement(root, "Say")
customText = "This is a test message."
ET.SubElement(root, "Say", voice="alice").text = customText

tree = ET.ElementTree(root)
tree.write("filename.xml")


# from twilio.twiml.voice_response import VoiceResponse, Say

# response = VoiceResponse()
# response.say('Chapeau!', voice='woman', language='fr')

# print(response)

call = client.calls.create(
                        url='filename.xml',
                        to=secrets["to"],
                        from_=secrets["from"]
                    )

print(call.sid)
