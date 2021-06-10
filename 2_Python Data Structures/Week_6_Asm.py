#Week_6_Asm.py
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count=0
counts=dict()
lst = list()
for line in handle:
    line=line.rstrip()
    if not line.startswith('From '):
        continue
    words=line.split()
    time=words[5]
    #print(time)
    hrs_lst=time.split(':')
    hrs=hrs_lst[0]
    #print(hrs)
    lst.append(hrs)

for hr in lst:
    counts[hr]=counts.get(hr,0)+1
#print(counts)

for k,v in sorted(counts.items()):
    print(k,v)
