#Week_4_Class.py
print([1,24,76])
print(['red','yellow','blue'])
print(['red','24','98,6'])
print([1,[5,6],7]) #3elements
print([]) #empty list

lotto=[2,14,26,41,63]
print(lotto)
lotto[2]=28
print(lotto)

x=[1,2,'joe',99]
print(len(x))

print(range(4)) #gives 4 numbers from 0-3
friends=['Joseph','Glenn','Sally']
print(len(friends))

print(range(len(friends)))
#range(0, 3) 0,1,2

for i in range(len(friends)): #counted loop
    friend=friends[i]
    print('Happy New Year:', friend)
