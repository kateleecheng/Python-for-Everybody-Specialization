#Week_2_Class.py

#hand=open('mbox-short.txt')
#or line in hand:
#    line=line.rstrip()
    #if line.find('From')>=0:
        #print(line)

import re

hand=open('mbox-short.txt')
for line in hand:
    line=line.rstrip()
    if re.search('From',line): #library.function(re.research)
        print(line)

#hand=open('mbox-short.txt')
#or line in hand:
#    line=line.rstrip()
    #if line.startswith('From'):
        #print(line)
import re

hand=open('mbox-short.txt')
for line in hand:
    line=line.rstrip()
    if re.search('^From',line):
        print(line)

#^X.*: (returnT/F)
#any character start with X and many character many time between :
#^=start with:
#.=any character
#*=many time

#^X-\S+:
#^=start with:
#\S=non white space character
#+=one or more times
