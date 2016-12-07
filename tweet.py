#!/usr/bin/python
# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session
import sys
import json

args = sys.argv
if len(args) == 1:
	print("error! usage: tweet [status]")
	sys.exit()

url = "https://api.twitter.com/1.1/statuses/update.json"

with open('token.json', 'r') as f:
    TOKEN = json.load(f)

text = str(args[1])
params = {"status": text + "\n#temabot"}

twitter = OAuth1Session(**TOKEN)
req = twitter.post(url, params = params)

if req.status_code == 200:
	print ("OK")
else:
	print("Error: %d" % req.status_code)
