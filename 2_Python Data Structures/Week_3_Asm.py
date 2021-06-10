#Week_2_Asm.py
fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    line=line.rstrip()
    nn=line.upper()
    print(nn)
