import urllib.request, urllib.parse, urllib.error
import json

su=0
tn=0
url=input('Enter location: ')
uh=urllib.request.urlopen(url)
data=uh.read().decode()
print("Retrieving", url)
js = json.loads(data)
print("Retrieved", len(data), "characters")
for item in js['comments']:
    su+= int(item['count'])
    tn+=1
print('Count:', tn)
print("Sum:", su)
