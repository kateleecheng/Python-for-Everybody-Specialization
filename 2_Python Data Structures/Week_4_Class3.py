#Week_4_Class3.py
abc='With three words'
stuff=abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])

for w in stuff:
    print(w)

line='A lot                  of space'
etc=line.split()
print(etc)#['A', 'lot', 'of', 'space']

line='first;second;third'
thing=line.split()
print(thing)#['first;second;third']
print(len(thing))#1

thing=line.split(';')
print(thing)#['first',second','third']
print(len(thing))#3

fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From '):
        continue
    words=line.split()
    print(words[2])

line='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words=line.split()
print(words)
email=words[1]
pieces=email.split('@')
print(pieces[1])
