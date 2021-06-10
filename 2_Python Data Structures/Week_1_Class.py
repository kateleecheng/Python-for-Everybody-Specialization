#Week_1_Class.py

fruit='banana'
letter=fruit[1]
print(letter)

x=3
w=fruit[x-1]
print(w)

fruit='banana'
x=len(fruit)
print(x)
#6

fruit='banana'
index=0
while index<len(fruit):
    letter=fruit[index]
    print(index, letter)
    index=index+1

fruit='banana'
for letter in fruit:
    print(letter)

index=0
while index<len(fruit):
    letter=fruit[index]
    print(letter)
    index=index+1

word='banana'
count=0
for letter in word:
    if letter=='a':
        count=count+1
print(count)

s='Monty Python' #space also count
#from where to where
print(s[0:4]) #upto but not included 4
#Mont
print(s[6:7])
#p
print(s[6:20])
#Python
print(s[:2])
#Mo
print(s[8:])
#thon
print(s[:])
#Monty Python
