#Week_4_Asm2.py

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

n=17

html = urlopen(' http://py4e-data.dr-chuck.net/known_by_Kaitlin.html', context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags=soup('a') #list of  anchor text
lst=list()
for tag in tags:
    #print(tag.get('href',None))
    lst.append(tag.get('href',None))
print(lst[n])

for loop in range(6):
    html = urlopen(lst[n], context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    tags=soup('a') #list of  anchor text
    lst=list()
    for tag in tags:
        #print(tag.get('href',None))
        lst.append(tag.get('href',None))
    print(lst[n])
