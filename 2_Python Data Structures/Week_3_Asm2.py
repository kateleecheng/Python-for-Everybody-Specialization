#Week_2_Asm2.py
fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    spacepos=line.find(' ')
    fnum=float(line[spacepos:].strip())
    total=total+fnum
    count=count+1
print("Average spam confidence:", total/count)
