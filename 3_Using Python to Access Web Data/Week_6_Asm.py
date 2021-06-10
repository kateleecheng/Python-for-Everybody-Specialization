#Week_6_Asm.py
#http://py4e-data.dr-chuck.net/comments_1238694.json
import json
import urllib.request, urllib.parse, urllib.error

url = input("Enter - ")
uh = urllib.request.urlopen(url)
data = uh.read()

info=json.loads(data)
#print(info)
total=0
for item in info['comments']:
    #print('Name',item['name'])
    #print('Attribute',int(item['count']))
    total=total+int(item['count'])
print(total)
