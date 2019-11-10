import requests
import json

apiKey = 'f1f9586376acdc8348dda04bc42bf48eec0b8bee'
url = 'https://api.github.com/repos/paulacduffy/week06lab'

filename ="repo.json"

response = requests.get(url, auth=('token',apiKey))

repoJSON = response.json()
#print (response.json())

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)
