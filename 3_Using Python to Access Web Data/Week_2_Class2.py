#Week_2_Class2.py

import re
x='My 2 favourite numbers are 19 and 42'
y=re.findall('[0-9]+',x) #give out a list
print(y)

#[0-9] = one or more digits

y=re.findall('[AEIOU]+',x)
print(y)

x='From: Using the : character'
y=re.findall('^F.+:',x)
#One or more character
#push outward as possibke(last :)
print(y)
#['From: Using the :']

x='From: Using the : character'
y=re.findall('^F.+?:',x)
#one or more character but not greedy(Stop at first :)
print(y)
#['From:']

x='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y=re.findall('\S+@\S+',x)
print(y)
#['stephen.marquard@uct.ac.za']

x='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y=re.findall('^From (\S+@\S+)',x)
#Demanding starting from [From] but only need string in ()
print(y)
#['stephen.marquard@uct.ac.za']

lin='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y=re.findall('@([^ ]*)',lin)
#@ = look for @
#[^ ] = Match non-blank character (Anything but space)
#[ ] = Not
#* = Match many of them
print(y)
#['uct.ac.za']

y=re.findall('^From .*@([^ ]*)',lin)
print(y)
#['uct.ac.za']

hand=open('mbox-short.txt')
numlist=list()
for line in hand:
    line=line.rstrip()
    stuff=re.findall('X-DSPAM-Confidence: (+)',line)
    if len(stuff) !=1:
        continue
    num=float(stuff[0])
    numlist.append(num)
print(numlist)
print('Maximum:', max(numlist))
#Maximum: 0.9907

x='We just received $10.00 for cookies.'
y=re.findall('\$[0-9.]+',x)
print(y)
#['$10.00']
