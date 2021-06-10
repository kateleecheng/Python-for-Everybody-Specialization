#Week_7_Class.py
n=5
while n>0:
    print(n)
    n=n-1
print('Blastoff')
print(n)

while True:
    line=input('>')
    if line == 'done':
        break
    print(line)
print('Done!')

while True:
    line=input('> ')
    if line[0] == '#':
        continue #back to while loop
    if line =='done':
        break #end the loop
    print(line)
print('Done!')
