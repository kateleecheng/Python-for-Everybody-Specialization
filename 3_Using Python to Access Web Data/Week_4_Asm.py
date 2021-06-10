#Week_4_Asm.py

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

#http://py4e-data.dr-chuck.net/comments_42.html
#http://py4e-data.dr-chuck.net/comments_1238691.html
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
total=0
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    x=int(tag.contents[0])
    #print(tag.contents[0])
    total=total+x
    #print(x)
print(total)
