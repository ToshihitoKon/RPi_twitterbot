#!/usr/bin/env python
# coding: UTF-8

from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth1Session
import requests
import subprocess
import json

url = "https://stream.twitter.com/1.1/statuses/filter.json"
tweet_url = "https://api.twitter.com/1.1/statuses/update.json"

with open('token.json', 'r') as f:
    TOKEN = json.load(f)

auth = OAuth1(**TOKEN)
twitter = OAuth1Session(**TOKEN)
r = requests.post(url, auth=auth, stream=True, data={'track':'@Tkon_bot'})

print("ready.")
for line in r.iter_lines():
    if line != '':
        #print(line.decode('utf-8'))
        try:
            data = json.loads(line.decode('utf-8'))
        except json.decoder.JSONDecodeError:
            continue

        get_time = subprocess.check_output('date').decode('utf-8')
        print('@'+data['user']['screen_name']+':'+data['text'])
        textv = data['text'].split(' ')
        try:
            if textv[0] != '@Tkon_bot' :
                continue

            if data['user']['screen_name'] == 'Tkon_sec':
                if textv[1] == 'help':
                    twitter.post(tweet_url, params={"status":"@Tkon_sec help, play, stop, repeat[on off]", "in_reply_to_status_id": data['id']})
                    continue
                elif textv[1] == 'stop':
                    subprocess.call('mpc stop', shell=True)
                    ms = 'music stopped.'
                elif textv[1] == 'play':
                    subprocess.call('mpc play', shell=True)
                    ms = 'music play.'
                elif textv[1] == 'repeat':
                    if textv[2] == 'off' :
                        subprocess.call('mpc repeat off', shell=True)
                        ms = 'set music repeat off.'
                    else :
                        subprocess.call('mpc repeat on', shell=True)
                        ms = 'set music repeat on.'
                elif textv[1] == 'sleep' :
                    subprocess.call('nohup /home/temama/twitter/stop.sh > /tmp/noh.log 2>&1 &', shell=True)
                    ms = 'set sleep timer.'
                elif textv[1] == 'playlist':
                    if textv[2] == 'marble' :
                        subprocess.call('mpc clear; mpc load marble; mpc play', shell=True)
                        ms = 'set playlist. [marble]'
                    elif textv[2] == 'el' :
                        subprocess.call('mpc clear; mpc load easylistening; mpc play', shell=True)
                        ms = 'set playlist. [EasyListening]'
                else:
                    twitter.post(tweet_url, params={ "status":"@"+data['user']['screen_name']+" "+get_time+"command not found: "+textv[1], "in_reply_to_status_id": data['id']})
                    continue

                twitter.post(tweet_url, params={"status":"@"+data['user']['screen_name']+" "+get_time+"OK. "+ms, "in_reply_to_status_id": data['id'] })
            else :
                if textv[1] == 'ばぶー':
                    twitter.post(tweet_url, params={"status":"@"+data['user']['screen_name']+" "+get_time+"おぎゃあああああああああああああ！！！", "in_reply_to_status_id": data['id'] })
                else :
                    twitter.post(tweet_url, params={"status":"@"+data['user']['screen_name']+" "+get_time+"usase: ばぶー", "in_reply_to_status_id": data['id'] })
        except IndexError :
            twitter.post(tweet_url, params={"status":"@"+data['user']['screen_name']+" "+get_time+"Sorry, can't parse command.", "in_reply_to_status_id": data['id'] })
            continue
