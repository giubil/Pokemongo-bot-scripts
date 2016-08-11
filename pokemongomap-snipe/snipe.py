import requests
import json
import math
import time
import sys
import os

import pprint

url = "http://188.165.224.208:49001/socket.io/"
headers = {
           'origin': "http://www.pokespawns.be",
           'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
           'accept': "*/*",
           'referer': "http://www.pokespawns.be/",
           'accept-encoding': "gzip, deflate, sdch",
           'accept-language': "en-US,en;q=0.8,fr;q=0.6,pl;q=0.4",
          }

def encode():
    alphabet = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_')
    length = 64
    num = time.time()*1000
    encoded = ''
    while num > 0:
        encoded = alphabet[int(num % length)] + encoded
        num = math.floor(num / length)
    return encoded

def generate_querystring(sid=None):
    if sid:
        return {"EIO":"3","transport":"polling","t": encode(), "sid": sid}
    else:
        return {"EIO":"3","transport":"polling","t": encode()}


class Pokespawns(object):
    sid = None
    def __init__(self):
        self.get_sid()
    def get_sid(self):
        # Only return sid if we don't have one
        if self.sid is not None:
            return self.sid
        response = requests.get(url, headers=headers, params=generate_querystring())
        try:
            obj = json.loads(response.text[response.text.find('{'):])
        except Exception, ex:
            print "error loading json: {}".format(ex)
        self.sid = obj['sid']
    def get_pokemons(self):
        if not self.sid:
            print "missing sid value for some reason... exiting"
            sys.exit(1)
        # request poke data with a POST
        payload = "8:40/pokes"
        post_request = requests.post(url, headers=headers, data=payload, params=generate_querystring(self.sid))
        if post_request.text == "ok":
            #print "Got OK while requesting pokemons, fetching them.."
            get_response = requests.get(url, params=generate_querystring(self.sid))
            obj = json.loads(get_response.text[get_response.text.find('['):])[1]
            self.sid = None
            print json.dumps(obj)
            return obj

class Snipe():
    def __init__(self):
        self.obj_list = None
    def get_IV_list(self, dict_list):
        ret_list = []
        for elem in dict_list:
            if elem['IV'] is not None:
                ret_list.append(elem)
                ret_list[-1]['IV'] = int(ret_list[-1]['IV'])
        if len(ret_list) == 0:
            return dict_list
        return sorted(ret_list, key=lambda k: k['IV'], reverse=True)
    def pop_and_snipe(self, dict_list):
        dict_list = self.get_IV_list(dict_list)
        for elem in dict_list:
            os.system("curl -X POST 'http://YOUR-MAP-CONTAINER-NAME:5000/next_loc?lat={0}&lon={1}'".format(elem['lat'], elem['lon']))
            time.sleep(60)
        pprint.pprint(dict_list)

pokelist = Pokespawns()
snipe = Snipe()

while True:
    pokelist.get_sid()
    objs = pokelist.get_pokemons()
    snipe.pop_and_snipe(objs)
 
