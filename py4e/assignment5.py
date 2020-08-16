import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
results=list()
api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = address
    print('Retrieving', url)

    data = urllib.request.urlopen(url, context=ctx).read()
    print('Retrieved', len(data), 'characters')

    tree = ET.fromstring(data)

    counts = tree.findall('comments/comment/count')
    print("Count: "+ str(len(counts)))

    co=0
    for count in counts:
        co=co+int(count.text)
    print("Sum:"+str(co))
