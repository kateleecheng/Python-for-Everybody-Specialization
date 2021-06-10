#Week_2_Class.py

stuff='Hello\nWorld!'
print(stuff)

stuff='X\nY'
print(stuff)

print(len(stuff))
#3 (newline(\n) is one charater)

xfile=open('mbox-short.txt') #cheese is a sequence(ordered set)
#for cheese in xfile:
    #print(cheese)

fhand=open('mbox-short.txt')
count=0
for line in fhand:
    count=count+1
print('Line count:', count)

fhand=open('mbox-short.txt')
inp=fhand.read() #read whole file into single string
print(len(inp))
print(inp[:20])

fhand=open('mbox-short.txt')
for line in fhand:
    if line.startswith('From'):
        print(line)
#Print function add a new line afterwards
#orginal file has new line too
#From: zqian@umich.edu/n
#/n
#From rjlowe@iupui.edu Fri Jan  4 15:46:24 2008/n
#/n
#From: rjlowe@iupui.edu/n

fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip() #remove right space
    if line.startswith('From'):
        print(line)

fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From'):
        continue#not interested line just skip
    print(line)

fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if not'@uct.ac.za'in line:
        continue
    print(line)

fname=input('Enter the file name: ')
fhand=open(fname)
count=0
for line in fhand:
    if line.startswith('Subject:'):
        count=count+1
print('There were', count, 'subject lines in', fname)


fname=input('Enter the file name: ')
try:
    fhand=open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
count=0
for line in fhand:
    if line.startswith('Subject:'):
        count=count+1
print('There were', count, 'subject lines in', fname)
