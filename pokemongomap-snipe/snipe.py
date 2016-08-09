import requests
import json
import pprint
import os
import time

while True:
    url = "http://pokesnipers.com/api/v1/pokemon.json"    
    response = requests.request("GET", url)    
    obj = json.loads(response.text)['results']
    
    for elem in obj:
        print (elem)
        lat, lon = elem['coords'].split(',')      
        os.system("curl -X POST 'http://YOUR-MAP-CONTAINER-NAME:5000/next_loc?lat=" + lat + "&lon=" + lon+ "'")
        time.sleep(60)
        
            
