#Week_5_Asm2.py
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input("Enter - ")
uh = urllib.request.urlopen(url)
data = uh.read()

stuff=ET.fromstring(data)
total=0
lst=stuff.findall('comments/comment') #list of text
#print('User count:', len(lst))
for item in lst:
    #print(item.find('name').text)
    #print(item.find('count').text)
    total=total+int(item.find('count').text)

print(total)
