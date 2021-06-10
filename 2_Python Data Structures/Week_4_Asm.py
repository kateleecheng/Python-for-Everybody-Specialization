#Week_4_Asm.py
fname = input("Enter file name: ")
fh = open(fname)
rfh=fh.read()
#print(rfh)
nn=rfh.split()
#print(nn)
nn.sort()
#print(nn)
count=0
lst = list()
for words in nn:
    if nn[count]!=nn[count-1]:
        #print(nn[count])
        lst.append(nn[count])
    count=count+1
print(lst)
