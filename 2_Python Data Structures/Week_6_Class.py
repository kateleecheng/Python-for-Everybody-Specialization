#Week_6_Class.py

x=('Glenn','Sally','Joseph')
print(x[2])

y=(1,9,2)
print(y)
print(max(y))

(x,y)=(4,'fred')
print(y)

(a,b)=(99,98)
print(a)

d=dict()
d['csev']=2
d['cwen']=4
for(k,v) in d.items():
    print(k,v)
#csev 2
#cwen 4
tups=d.items()
print(tups)
#dict_items([('csev', 2), ('cwen', 4)])

(0,1,2)<(5,1,2)
#True
(0,1,2000000)<(0,3,4)
#True
('Jones','Sally')<('Jones','Sam')
#True
('Jones','Sally')>('Adam','Sam')
#True

d={'a':10,'b':1,'c':22}
print(d.items())
#dict_items([('a', 10), ('b', 1), ('c', 22)])
print(sorted(d.items()))
#[('a', 10), ('b', 1), ('c', 22)]

d={'a':10,'b':1,'c':22}
t=sorted(d.items())

for k,v in sorted(d.items()): #in key order
    print(k,v)
[(10, 'a'), (1, 'b'), (22, 'c')]
#in value order
c={'a':10,'b':1,'c':22}
tmp=list()
for k,v in c.items():
    tmp.append((v,k))#creat a list of tuple
print(tmp)
#[(10, 'a'), (1, 'b'), (22, 'c')]
tmp=sorted(tmp,reverse=True)
#[(22, 'c'), (10, 'a'), (1, 'b')]


#The top 10 most common words
fhand=open('romeo.txt')
counts=dict()
for line in fhand:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

lst=list()
for key,val in counts.items():
    newtup=(val,key)
    lst.append(newtup)

lst=sorted(lst,reverse=True)

for val,key in lst[:10]:
    print(key,val)

#######shorter Version
c={'a':10,'b':1,'c':22}
print(sorted([(v,k)for k,v in c.items()]))
#[(1, 'b'), (10, 'a'), (22, 'c')]
