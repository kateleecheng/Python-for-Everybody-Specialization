#Week_5_Asm.py
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
    email=words[1]
    lst.append(email)
    #pieces=email.split('@')
    #print(pieces[0])
    #for pieces[0] in pieces:
    #    counts[pieces[0] ]=counts.get(pieces[0],0)+1
    count=count+1
    #print(email)

#print(lst)

for ppl in lst:
    counts[ppl]=counts.get(ppl,0)+1
#print(counts)

bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count

print(bigword,bigcount)
