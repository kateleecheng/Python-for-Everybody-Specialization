#Week_2_Asm.py
import re

hand=open('regex_sum_1238689.txt')
numlist=list()
for line in hand:
    line=line.rstrip()
    stuff=re.findall('[0-9]+',line)
    #print(stuff)
    numlist=stuff+numlist

#print(numlist)
i=0
for i in  range(0, len(numlist)):
    numlist[i]=int(numlist[i])
    i=i+1

#print(numlist)
total=sum(numlist)
print(total)
