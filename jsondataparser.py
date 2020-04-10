import urllib.request
import json

address = input('Enter location: ')
print ('Retrieving', address)

uh = urllib.request.urlopen(address)
data = uh.read()
print ('Retrieved', len(data), 'characters')

info = json.loads(data)
print ('Count:', len(info['comments']))

total = 0

for i in range(len(info['comments'])):
    total += int(info['comments'][i]['count'])
print ("Sum:", total)