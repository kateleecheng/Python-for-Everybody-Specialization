#Week_5_Class2.py

#counting
ccc=dict()
ccc['csev']=1
ccc['cwen']=1
print(ccc)
#{'csev': 1, 'cwen': 1}
ccc['cwen']=ccc['cwen']+1
print(ccc)
#{'csev': 1, 'cwen': 2}

counts=dict()
names=['csev','cwen','csev','zqian','cwen']
for name in names:
    if name not in counts:
        counts[name]=1
    else:
        counts[name]=counts[name]+1
print(counts)
#{'csev': 2, 'cwen': 2, 'zqian': 1}

counts2=dict()
names2=['csev','cwen','csev','zqian','cwen']
for name in names2:
    counts2[name]=counts2.get(name,0)+1 #[namw,0] get current count of the name or 0
print(counts2)
#{'csev': 2, 'cwen': 2, 'zqian': 1}

name=input('Enter file:')
handle=open(name)

counts=dict()
for line in handle:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count

print(bigword,bigcount)

stuff = dict()
print(stuff.get('candy',-1))
