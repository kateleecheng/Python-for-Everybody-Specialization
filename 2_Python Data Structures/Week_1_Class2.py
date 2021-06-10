#Week_1_Class2.py

a='Hello'
b=a+'There'
print(b) #no space

c=a+' '+'There'
print(c) #have space

fruit='banana'
'n'in fruit
'm'in fruit
'nan'in fruit
if 'a' in fruit:
    print('Found it')

greet='Hello Bob'
zap=greet.lower() #a lowercase copy wont change the original
print(zap)
print(greet)
print('Hi There'.lower())

fruit='banana'
pos=fruit.find('na')
print(pos)
#2 (start from 0)
aa=fruit.find('z')
print(aa)
#not found = -1

greet='Hello Bob'
nnn=greet.upper()
print(nnn)
www=greet.lower()
print(www)

greet="Hello Bob"
nstr=greet.replace('Bob','Jane')
print(nstr)
nstr=greet.replace('o','X')
print(nstr)

greet='     Hello Bob     '
print(greet.lstrip()) #remove space from left
print(greet.rstrip()) #remove space from right
print(greet.strip()) #remove space from both side

line='Please have a nice day'
line.startswith('Please')
#True
line.startswith('p')
#False

data='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos=data.find('@')
print(atpos) #21
sppos=data.find(' ',atpos) #data behind atpos
print(sppos) #31
host=data[atpos+1:sppos]
print(host)
